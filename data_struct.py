from collections import UserDict
from datetime import date, datetime, timedelta
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
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    #prints Record nicely in print(AddressBook)
    def __repr__(self) -> str:
        return self.__str__()

class AddressBook(UserDict[str, Record]):

    def add_record(self, record:Record):
        self.data[record.name.value] = record

    def find(self, record_name:str) -> Record:
        return self.data[record_name]

    def delete(self, record_name:str):
        del self.data[record_name]

    def get_upcoming_birthdays(self) -> list[dict[str, str]]:
        upcoming_birthdays = []
        for record in self.data.values():
            birthday_date:date = record.birthday.value
            birthday_this_year = birthday_date.replace(year=datetime.now().year)
            congrats_date:date = self.__handle_weekedns(birthday_this_year)
            days_from_today = self.__get_days_from_today(congrats_date)
            #handle last 7 days of the year - try BD next year
            if days_from_today < 0:
                birthday_next_year = birthday_date.replace(year=datetime.now().year+1)
                congrats_date = self.__handle_weekedns(birthday_next_year)
                days_from_today = self.__get_days_from_today(congrats_date)
            if days_from_today <= 7:
                upcoming_birthdays.append({
                    "name": record.name.value, 
                    "congratulation_date":congrats_date.strftime("%d.%m.%Y")})
        return upcoming_birthdays
    
    def __handle_weekedns(birthday: date) -> date:
        if birthday.isoweekday() == 6:
            birthday += timedelta(days=2)
        elif birthday.isoweekday() == 7:
            birthday += timedelta(days=1)
        return birthday
    
    def __get_days_from_today(congrats_date:date) -> int:
        date_now = datetime.now().date()
        return (congrats_date - date_now).days
    

def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("8888888888")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for _, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    john.remove_phone("8888888888")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    print("Book",book)


if __name__ == "__main__":
       main()