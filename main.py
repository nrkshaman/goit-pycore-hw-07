from AddressBook import AddressBook
from constants import *
from decorators import interrupt_error
from handlers import *

def parse_input(user_input: str):
    try:
        cmd, *args = user_input.split()
    except ValueError:
        return INVALID_COMMAND
    cmd = cmd.strip().lower()
    return cmd, *args

@interrupt_error
def main():
    contacts = AddressBook()
    print(BANNER)
    print(GREETING)
    #lambda accepts not used *args to ignore extra arguments
    command_dict = {
        "hello": lambda *args: "How can I help you?",
        "close": lambda *args: "Good bye!",
        "exit": lambda *args: "Good bye!",
        "add": lambda *args: add_contact(args, contacts),
        "all": lambda *args: all_contact(contacts),
        "change": lambda *args: change_contact(args, contacts),
        "phone": lambda *args: phone_contact(args, contacts),
        "add-birthday": lambda *args: add_birthday(args, contacts),
        "show-birthday": lambda *args: show_birthday(args, contacts),
        "birthdays": lambda *args: birthdays(contacts),
        "help": lambda *args: HELP,
    }
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        try:
            print(command_dict[command](*args))
        except:
            print(INVALID_COMMAND)

if __name__ == "__main__":
    main()
