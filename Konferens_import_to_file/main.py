from Konferens import Booking
from cmd import Cmd

MENU_TEXT = "########### Menu ###########\n" \
            "1: Visa tillängliga rum     \n" \
            "2: Boka ett rum             \n" \
            "3: Ta bort bokning          \n" \
            "4: Spara bokade rum till fil\n" \
            "############################\nInput: "
class Menu(Cmd):
    prompt = MENU_TEXT

    def __init__(self):
        super().__init__()
        self.booking = Booking()

        self.cmdloop()

    def do_1(self, args):
        self.booking.print_all_rooms()

    def do_2(self, args):
        self.booking.add_to_booking()

    def do_3(self, args):
        self.booking.remove_from_booking()

    def do_4(self, args):
        self.booking.finalize_booking()

if __name__ == "__main__":
    Menu()
