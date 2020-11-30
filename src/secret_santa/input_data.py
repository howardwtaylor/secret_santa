from typing import List

from household import Household
from person import Person


def assignments() -> List[Person]:
    recipients = [
        Person('Bob', '', Household.BOB_AND_NAN, '', ''), \
        Person('Nan', '', Household.BOB_AND_NAN, '', ''), \
        Person('Gordon', '', Household.GORD_AND_HEATHER, '', ''), \
        Person('Heather', '', Household.GORD_AND_HEATHER, '', ''), \
        Person('Gabriel', '', Household.GORD_AND_HEATHER, '', ''), \
        Person('Michael', '', Household.GORD_AND_HEATHER, '', ''), \
        Person('Lucas', '', Household.GORD_AND_HEATHER, '', ''), \
        Person('Samuel', '', Household.GORD_AND_HEATHER, '', ''), \
        Person('Dee', '', Household.DEE, '', ''), \
        Person('Howard', '', Household.HOW_AND_HELENE, '', ''), \
        Person('Helene', '', Household.HOW_AND_HELENE, '', ''), \
        Person('Madeline', '', Household.HOW_AND_HELENE, '', ''), \
        Person('Jeremy', '', Household.HOW_AND_HELENE, '', ''), \
        Person('Margot', '', Household.HOW_AND_HELENE, '', ''), \
        Person('Jonathan', '', Household.HOW_AND_HELENE, '', '')]

    return recipients
