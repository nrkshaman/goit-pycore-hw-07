from datetime import datetime
from errors import InvalidBirthday, InvalidName, InvalidPhone

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self) -> str:
        return self.__str__()

class Name(Field):
    def __init__(self, value):
        if not (value and isinstance(value, str)):
            raise InvalidName
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not (isinstance(value, str) and len(value)==10 and value.isdecimal()):
            raise InvalidPhone
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date)
        except ValueError:
            raise InvalidBirthday