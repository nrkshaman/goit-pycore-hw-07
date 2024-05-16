from collections import UserDict
from datetime import date, datetime, timedelta
from Record import Record

class AddressBook(UserDict[str, Record]):

    def add_record(self, record:Record):
        self.data[record.name.value] = record

    def find(self, record_name:str) -> Record:
        return self.data.get(record_name)

    def delete(self, record_name:str):
        del self.data[record_name]

    def get_upcoming_birthdays(self) -> list[Record]:
        upcoming_birthdays = []
        for record in self.data.values():
            if not record.birthday:
                continue
            birthday_date:date = record.birthday.value
            birthday_this_year = birthday_date.replace(year=datetime.now().year)
            days_from_today = self.__get_days_from_today(birthday_this_year)
            #handle last 7 days of the year -> try BD next year
            if days_from_today < 0:
                birthday_next_year = birthday_date.replace(year=datetime.now().year+1)
                days_from_today = self.__get_days_from_today(birthday_next_year)
            if days_from_today <= 7:
                upcoming_birthdays.append(record)
        return upcoming_birthdays
    
    
    @staticmethod
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
    john_record.add_birthday("20.05.1999")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("24.5.9999")
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
    #book.delete("Jane")

    print("Book",book.get_upcoming_birthdays())


if __name__ == "__main__":
       main()