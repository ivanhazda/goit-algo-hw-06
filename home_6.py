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
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number_str):
        phone = Phone(phone_number_str)
        self.phones.append(phone)

    def remove_phone(self, phone_number_str):
        phone = Phone(phone_number_str)
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError(f"Номер телефону {phone_number_str} не знайдено.")

    def edit_phone(self, old_number_str, new_number_str):
        phone = self.find_phone(old_number_str)

        if not phone:
            raise ValueError(f"Номер телефону {old_number_str} не знайдено.")
        # Створюємо новий об'єкт Phone для валідації нового номера
        new_phone = Phone(new_number_str)
        index = self.phones.index(phone)
        self.phones[index] = new_phone


    def find_phone(self, phone_str):
      for phone in self.phones:
            if phone.value == phone_str:
                return phone
      return None

    def __str__(self):
     return f"Ім'я контакту: {self.name.value}, телефони: {'; '.join(str(phone) for phone in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, 'None')

    def delete(self, name_str):
        if name_str in self.data:
            del self.data[name_str]
        else:
            raise ValueError(f"Запис для {name_str} не знайдено.")

    def __str__(self):
      if not self.data:
            return "Адресна книга порожня."
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
    print ("====================")
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223334")
    print ("====================")

    print(john)  # Виведення: Ім'я контакту: John, телефони: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    print(book)
