from fields import Birthday, Name, Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday = None

    # реалізація класу
    def add_phone(self, phone:str):
        self.phones.append(Phone(phone))

    def remove_phone(self, del_phone:str):
        self.phones.remove(self.find_phone(del_phone))

    def edit_phone(self, old_phone:str, new_phone:str):
        old = self.find_phone(old_phone)
        if old:
            old.value = new_phone

    def find_phone(self, phone:str) -> Phone | None:
        phone = list(filter(lambda p: p.value==phone, self.phones))
        return phone[0] if phone else None
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday.value if self.birthday else None}, phones: {'; '.join(p.value for p in self.phones)}"
    
    #prints Record nicely in print(AddressBook)
    def __repr__(self) -> str:
        return self.__str__()
