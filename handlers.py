from datetime import date
from AddressBook import AddressBook
from Record import Record
from constants import *
from decorators import input_error

@input_error
def add_contact(args:list[str], contacts:AddressBook) -> str:
    name, phone, = args
    contact = contacts.find(name)
    msg =  UPDATED.format(name)
    if not contact:
        contact = Record(name)
        contacts.add_record(contact)
        msg = INFO + f" Contact {name} successfully created."
    if phone:
        contact.add_phone(phone)
    return msg

@input_error
def change_contact(args:list[str], contacts:AddressBook) -> str:
    name, old_phone, new_phone, = args
    contact = contacts.find(name)
    if not contact:
        raise KeyError
    contact.edit_phone(old_phone, new_phone)
    return UPDATED.format(name)
    
@input_error
def phone_contact(args:list[str], contacts:AddressBook) -> str:
    name, = args
    contact = contacts.find(name)
    if not contact:
        raise KeyError
    return contact.phones

def all_contact(contacts:AddressBook) -> str:
    if not contacts.data:
        return INFO + " You do not have any contacts saved"
    
    all = f"{'Name':<15}{'| Birthday':<12}{'| Phone'}\n" + "-"*42 + "\n"
    for name in contacts.data:
        phones_iter = contacts[name].phones.__iter__()
        birthday = contacts[name].birthday.value.strftime("%d.%m.%Y") if contacts[name].birthday else "-"
        all += f"{name: <15}| {birthday: <12}| {next(phones_iter)}\n"
        #
        for phone in phones_iter:
            all += f"{' ': <15}| {' ':<12}| {phone}\n"
    return all.strip()

@input_error
def add_birthday(args:list[str], contacts:AddressBook):
    name, birthday, = args
    contact = contacts.find(name)
    if not contact:
        raise KeyError
    contact.add_birthday(birthday)
    return UPDATED.format(name)

@input_error
def show_birthday(args:list[str], contacts:AddressBook):
    name, = args
    contact = contacts.find(name)
    if not contact:
        raise KeyError
    if not contact.birthday:
        return ERROR + "Conntact does not have saved birthday date"
    return contact.birthday.value.strftime("%d.%m.%Y")

@input_error
def birthdays(contacts:AddressBook):
    birthdays = contacts.get_upcoming_birthdays()
    if not contacts.data:
        return INFO + " You do not have any contacts saved"
    if not birthdays:
        return INFO + " There are no upcoming birthdays"
    
    all = f"{'Name':<15}{'| Birthday':<12}{'| Phone'}\n" + "-"*42 + "\n"
    for contact in birthdays:
        phones_iter = contact.phones.__iter__()
        all += f"{contact.name.value: <15}| {contact.birthday.value.strftime("%d.%m.%Y"):<12}| {next(phones_iter).value}\n"
        for phone in phones_iter:
            all += f"{' ': <15}| {' ':<12}| {phone.value}\n"
    return all.strip()
