from databas_lokaler import *

class Menu:

    MAIN_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'

1: 'Ladda in lokaler till en databas'
2: 'Visa alla lokaler'
3: 'Boka en lokal'


'För att avsluta tryck 9'
"""

    def __init__(self):
        self.db = Databas()

    def user_input(self):
        try:
            return int(input("Enter your choice [1-4]: "))
        except ValueError:
            print("\nERROR: Du måste ange siffra 1-4\n")

    def menu_choice(self, choice):
        if choice == 9:
            self.running = False
        elif choice == 1:
            self.db.ladda_in_lokaler_till_db()
        elif choice == 2:
            self.db.visa_alla_lokaler()
        elif choice == 3:
            self.db.boka()
        elif type(choice) is int:
            print(f"{choice} finns inte")

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.menu_choice(choice)
        print("Välkomment åter")

if __name__ == '__main__':
    Menu().menu_loop()

# Källa: Lesson_10, 7_menu_loop
