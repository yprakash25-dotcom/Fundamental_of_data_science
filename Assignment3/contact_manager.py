"""Program to manage contacts using Contact and ContactBook classes."""


class Contact:
    """A contact with name, phone number, and email address."""

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f"{self.name} | {self.phone} | {self.email}"


class ContactBook:
    """A simple contact book that stores and searches contacts."""

    def __init__(self) -> None:
        self.contacts: list[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def search_contact(self, search_name: str) -> list[Contact]:
        return [contact for contact in self.contacts if search_name.lower() in contact.name.lower()]

    def display_all(self) -> None:
        print("\nContact list:")
        for contact in self.contacts:
            print(contact)


if __name__ == "__main__":
    print("Contact Manager OOP Program")
    book = ContactBook()

    for i in range(1, 4):
        print(f"\nEnter contact {i} details:")
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        book.add_contact(Contact(name, phone, email))

    book.display_all()

    query = input("\nEnter a name to search: ").strip()
    matches = book.search_contact(query)
    if matches:
        print("\nSearch results:")
        for match in matches:
            print(match)
    else:
        print("No contact found.")
