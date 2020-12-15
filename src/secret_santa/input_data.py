import pandas as pd
from typing import List

from secret_santa.person import Household, Person, PersonType


def load_input_data(filename: str) -> List[Person]:
    # load data from csv as a data frame
    df = pd.read_csv(filename, delimiter=',', na_values='',
                     converters={'first': str.strip, 'last': str.strip,
                                 'household': str.strip, 'person_type': str.strip,
                                 'recipient_type': str.strip, 'email_address': str.strip,
                                 'phone_number': str.strip, 'wishlist': str.strip})

    # build list of Persons from data frame
    people = list()
    for row in df.itertuples():
        household = Household[row.household]
        person_type = PersonType[row.person_type]
        recipient_type = PersonType[row.recipient_type]
        people.append(Person(row.first, row.last, household, person_type,
                             recipient_type, row.email_address,
                             row.phone_number, row.wishlist))
    return people
