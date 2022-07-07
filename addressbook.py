"""This demo is an address book application"""
import dataclasses
from distutils import extension


@dataclasses.dataclass
class Address:
    """A contact entry address"""
    street_address: str = None
    city: str = None
    region: str = None
    country: str = None
    
    def __str__(self):
        """Return a multi-line string representation of the address"""
        "\n".join((self.street_address, self.city, self.region, self.country))

@dataclasses.dataclass
class BaseContact:
    """Information that both class will use"""
    name: str
    phone: str = None # String so that it will accept any format of phone number lazily
    address: Address = None
    notes: str = None
    website: str = None

@dataclasses.dataclass
class Organization(BaseContact):
    """An business or organization"""
    branches: list['Organization'] = None

@dataclasses.dataclass
class Person(BaseContact):
    """A person record with their information"""
    company: Organization = None
    title: str = None
    job_title: str = None

    def __str__(self):
        """Return a multi-line string representation of the person"""
        
        return """{self.name=}
{self.phone=}
{self.address=}
{self.notes=}
{self.website=}
"""

@dataclasses.dataclass
class AddressBook:
    owner: Person = None
    contacts: list[Person, Organization] = dataclasses.field(default_factory=list)

    def __str__(self):
        return f"Address Book for {self.owner.name}"