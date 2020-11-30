from urllib.parse import urlparse

from household import Household


class Person:

    def __init__(self, first: str, last: str, household: Household, emailAddr: str, wishList: urlparse) -> None:
        self.first: str = first
        self.last: str = last
        self.household = household
        self.emailAddr = emailAddr
        self.wishListURL = urlparse(wishList)

    def __str__(self) -> str:
        return 'Person: {self.first} {self.last} at {self.household}'.format(self=self)

    def __hash__(self) -> int:
        return hash((self.first, self.last, self.household, self.emailAddr, self.wishListURL))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        elif self is other:
            return True
        else:
            return self.first == other.first and \
                   self.last == other.last and \
                   self.household == other.household and \
                   self.emailAddr == other.emailAddr and \
                   self.wishListURL == other.wishListURL
