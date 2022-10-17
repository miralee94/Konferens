from datetime import datetime

#datum = datetime.now().strftime("%Y-%m-%d %H:%M")
#print(datum)
#
#starttid = datetime.strptime(input("Välj starttid för bokningen: "),"%Y-%m-%d %H:%M")
#
#print(starttid)

tid = "fm"
if tid != "em" and tid != "fm":
    print("Du måste ange em eller fm")

print(tid)