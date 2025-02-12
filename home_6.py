from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Номер телефону має містити 10 цифр.")
        super().__init__(value)

    def validate_phone(self, value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name).value
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone.value)

    def remove_phone(self, phone_number):
        if phone_number in self.phones:
            self.phones.remove(phone_number)
        else:
            raise ValueError(f"Номер телефону {phone_number} не знайдено.")

    def edit_phone(self, old_number, new_number):
        if old_number in self.phones:
            Phone(new_number)
            self.phones[self.phones.index(old_number)] = new_number
        else:
            raise ValueError(f"Номер телефону {old_number} не знайдено.")

    def find_phone(self, phone_number):
        if phone_number in self.phones:
            return phone_number
        return None

    def __str__(self):
        return f"Ім'я контакту: {self.name}, телефони: {'; '.join(self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def find(self, name):
        return self.data.get(name, 'None')

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Запис для {name} не знайдено.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223334")

    print(john)  # Виведення: Ім'я контакту: John, телефони: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    print(book)
