from email.utils import formataddr
from enum import Flag, auto

from typing import List


#  FIXME: build these dynamically from the loaded household names
#  use syntax like
#    Animal = Enum('Animal', 'ANT BEE CAT DOG')
#    f = Flag('WRITING_IMPLEMENTS', 'pencil pen quill')
#    Need an "ALL" entry, too:
#    val = 0
#    for name,enum_name in f.__members__.items():
#       val |= enum_name.value
#     ---->  Can't assign an ALL entry after creation...
#     f['ALL']=val
#         TypeError: 'EnumMeta' object does not support item assignment
#
class Household(Flag):
    BOB_AND_NAN = auto()
    GORD_AND_HEATHER = auto()
    DEE = auto()
    HOW_AND_HELENE = auto()
    ROB_AND_CINDY = auto()
    ALL = BOB_AND_NAN | GORD_AND_HEATHER | DEE | HOW_AND_HELENE | ROB_AND_CINDY


#  FIXME: build these dynamically from the loaded PERSON_TYPE names
class PersonType(Flag):
    ADULT = auto()
    PARENT = auto()
    CHILD = auto()
    GRANDCHILD = auto()
    ALL = ADULT | PARENT | CHILD | GRANDCHILD


class Person:

    def __init__(self, first: str, last: str, household: Household, person_type: PersonType,
                 recipient_type: PersonType, email_address: str, phone_number: str,
                 wishlist_link: str) -> None:
        self.first: str = first
        self.last: str = last
        self.household = household
        self.person_type = person_type
        self.recipient_type = recipient_type
        self.email_address = email_address
        self.phone_number = phone_number
        self.wishlist_link = wishlist_link

    def full_name(self) -> str:
        return f'{self.first} {self.last}'

    def full_email(self) -> str:
        full_email = formataddr((self.full_name(), self.email_address))
        return f"'{full_email}'"

    def __str__(self) -> str:
        s = ''
        if self.first:
            s += self.first
        if self.last:
            s += f' {self.last}'
        s += ','
        if self.phone_number:
            s += f' {self.phone_number},'
        if self.email_address:
            s += f' {self.full_email()}'
        return s

    def __hash__(self) -> int:
        return hash((self.first, self.last, self.household, self.person_type,
                     self.recipient_type, self.email_address, self.phone_number,
                     self.wishlist_link))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        elif self is other:
            return True
        else:
            return self.first == other.first and \
                   self.last == other.last and \
                   self.household == other.household and \
                   self.person_type == other.person_type and \
                   self.recipient_type == other.recipient_type and \
                   self.email_address == other.email_address and \
                   self.phone_number == other.phone_number and \
                   self.wishlist_link == other.wishlist_link


def get_other_household_members(member: Person, family: List[Person]) -> List[Person]:
    household = list()
    for person in family:
        if (person.household == member.household) and (person != member):
            household.append(person)
    return household
