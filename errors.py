class InvalidPhone(ValueError):
    def __init__(self, msg='Phone must be 10 digits long string', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class InvalidName(ValueError):
    def __init__(self, msg='Name must be non empty string', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class InvalidBirthday(ValueError):
    def __init__(self, msg='Invalid date format. Use DD.MM.YYYY', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)