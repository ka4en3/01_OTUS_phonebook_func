from homework_02.book.phone_book import PhoneBook
from homework_02.resources.strings import *


class Model:
    def __init__(self, data_handler):
        # Model keeps phonebook as an instance of class PhoneBook
        self.__phonebook = None
        # Model requires data_handler on creation (file, db, ...)
        self.__data_handler = data_handler

    def open_book(self) -> PhoneBook:
        # every call create a new instance of PhoneBook
        self.__phonebook = PhoneBook()
        # load data to json dict
        data = self.__data_handler.load_data_to_dict()

        for cid, contact in data.items():
            new_contact = Contact(cid)
            for key, value in contact.items():
                key = key.strip().lower()
                if key in FIELDS_MAP.values():
                    setattr(new_contact, key, value)

            self.__phonebook.add_to_book(new_contact)

        return self.__phonebook if self.book_is_opened() else None

    def get_book(self) -> PhoneBook:
        return self.__phonebook

    def book_is_opened(self) -> bool:
        return self.__phonebook and not self.__phonebook.is_empty()

    def save_book(self):
        self.__data_handler.save_data_to_file(self.__phonebook.get_book_as_dict())

    def add_new_contact(self, input_new_contact: dict) -> bool:
        # generating next contact_id
        next_id = self.__phonebook.get_max_id() + 1
        # create new object of Contact
        new_contact = Contact(str(next_id))

        for key, value in input_new_contact.items():
            key = key.strip().lower()
            if key in FIELDS_MAP.values():
                setattr(new_contact, key, value)

        self.__phonebook.add_to_book(new_contact)

        return next_id

    def edit_contact(self, edit_id: str, input_edit_contact: dict) -> bool:
        edit_contact = self.find_contact_by_id(edit_id)
        if edit_contact:
            for key, value in input_edit_contact.items():
                key = key.strip().lower()
                if key in FIELDS_MAP.values():
                    setattr(edit_contact, key, value)
            return True

        return False

    def find_contact_by_id(self, edit_id: str) -> Contact:
        return self.__phonebook.get_contact_by_id(edit_id)

    def find_contact_by_str(self, str_to_find: str) -> list[Contact]:
        # for cont_id, contact in self.__phonebook.get_book_as_dict.items():
        #     found = 0
        #     for key, value in contact.items():
        #         if str(key).strip().lower() not in ("comment", "комментарий"):  # ignoring "Comment" field
        #             for word in str(value).strip().lower().split(sep=" "):
        #                 if inp in word:
        #                     print_contact(cont_id)
        #                     found = 1
        #                     break
        #         if found: break
        return []



