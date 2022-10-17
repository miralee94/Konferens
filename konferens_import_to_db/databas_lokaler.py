from datetime import datetime
from operator import itemgetter
import sqlite3

class Lokal:
    def __init__(self, lokal_nr, tid, status, kontakt) -> None:
        self.lokal_nr = lokal_nr
        self.tid = tid
        self.status = status
        self.kontakt = kontakt

    def __str__(self) -> str:
        return f"{self.lokal_nr}) {self.tid}, {self.status}, {self.kontakt} "

class Databas:
    def __init__(self) -> None:
        self.con = self.connect_db()
        self.cursor = self.con.cursor()

    def connect_db(self):
        with sqlite3.connect('Lokaler.db', isolation_level=None) as conn:
            return conn

    def create_table(self):
        CREATE_TABLE_LOKALER="""CREATE TABLE IF NOT EXISTS Lokaler(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    lokalid INTEGER,
                                    tid TEXT,
                                    status TEXT,
                                    kontakt TEXT
                                )"""
        self.cursor.execute(CREATE_TABLE_LOKALER)

    def insert_data(self):
        id_list = []
        for nummer in range(1, 11):
            id_list.append((nummer, "fm", "LEDIG"))
        for nummer in range(1, 11):
            id_list.append((nummer, "em", "LEDIG"))
        
        INSERT_DATA = """INSERT INTO Lokaler (lokalid, tid, status) VALUES (?, ?, ?)"""
        self.cursor.executemany(INSERT_DATA, id_list)

    def visa_alla_lokaler(self):
        lokaler=self.cursor.execute("""SELECT * from Lokaler""").fetchall()
        
        for lokal in lokaler:
            print(Lokal(*lokal[1:5]))

    def ladda_in_lokaler_till_db(self):
        self.create_table()
        self.insert_data()

    def boka(self):
    #    dateformat = "%Y-%m-%d %H:%M"
    #    starttid = datetime.strptime(input("Välj starttid för bokningen ÅÅÅÅ-MM-DD HH:MM: "), dateformat)
    #    sluttid = datetime.strptime(input("Välj sluttid för bokningen ÅÅÅÅ-MM-DD HH:MM: "), dateformat)
        fm = "08:00 - 12:00"
        em = "13:00 - 17:00"

        lokalid = int(input("Välj id på lokalen som du vill boka (1-10): "))
        tid = input(f"Vill du boka förmiddag eller eftermiddag, ange fm för {fm} eller em för {em}: ")
        if tid != "em" and tid != "fm":
            print("Du måste ange em eller fm")
        kontakt_pers = input("Ange ditt namn: ")

        alla_lokaler = self.cursor.execute("SELECT * from Lokaler").fetchall()
        alla_lokaler = [Lokal(*lokal[1:5]) for lokal in alla_lokaler]
        for lokal in alla_lokaler:
            if lokal.lokal_nr == lokalid and lokal.tid == tid:
                if lokal.status == "BOKAD":
                    print(f"Lokalen med ID {lokalid} är redan bokad på {tid}")
                    return

        INSERT_DATA = """UPDATE Lokaler set status = ?, kontakt = ? where lokalid = ? AND tid = ?"""
        self.cursor.execute(INSERT_DATA, ("BOKAD", kontakt_pers, lokalid, tid))

        