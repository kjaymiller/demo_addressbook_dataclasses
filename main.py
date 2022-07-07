import addressbook
from faker import Faker

def build_addressbook(*contacts, owner):
    """Build an address book with the given contacts"""
    pass

if __name__ == "__main__":
    fake = Faker()
    name = fake.name() 
    phone = fake.phone_number()
    address = fake.address()
    notes = fake.text()
    website = fake.url()
    contact = addressbook.Person(
        name=name,
        phone=phone,
        address=address,
        notes=notes,
        website=website,
    )
    
    addressbook.AddressBook