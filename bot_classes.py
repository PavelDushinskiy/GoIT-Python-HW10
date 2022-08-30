from collections import UserDict


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value


class Name(Field):
    def __init(self, ):
        pass


class Phone(Field):
    def value(self) -> str:
        return self._value


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone] if phone is not None else []

    def add_phone(self, phone: Phone:
        self.phones.append(phone)

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        try:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)
        except ValueError:
            return f"{old_phone} does not exist"

    def delete_phone(self, phone: Phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            return f"{phone} does not exist"


class AddressBook(UserDict):
    def add_contact(self, name: Name, phone: Phone = None):
        contact = Record(name=name, phone=phone)
        self.data[name.value] = contact

    def add_record(self, record: 'Record'):
        self.data[record.name.value] = record

    def find_name(self, name: Name):
        try:
            return self.data[name]
        except KeyError:
            return None

    def find_phone(self, phone: Phone):
        for record in self.data.values():
            if phone in [number.value for number in record.phones]:
                return record
        return None
