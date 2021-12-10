from datetime import datetime

import pandas as pd
from typing import List

from secret_santa.person import Household, Person, PersonType, find_person_by_full_name
from secret_santa.pick import Pick
from secret_santa.previous_pick import PreviousPick


def load_input_data(filename: str) -> List[Person]:
    # load data from csv as a data frame
    df = pd.read_csv(filename, delimiter=',', na_values='', comment='#',
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


def load_previous_pick_data(people: List[Person], filename: str) -> List[PreviousPick]:
    date_parse = lambda dates: [datetime.strptime(d, "%Y-%m-%d") for d in dates]
    df = pd.read_csv(filename, delimiter=',', na_values='', comment='#',
                     parse_dates=['datetime'], date_parser=date_parse,
                     converters={'giver_first': str.strip,
                                 'giver_last': str.strip,
                                 'receiver_first': str.strip,
                                 'receiver_last': str.strip})
    previous_picks = list()
    for row in df.itertuples():
        giver = find_person_by_full_name(people, row.giver_first, row.giver_last)
        receiver = find_person_by_full_name(people, row.receiver_first, row.receiver_last)
        if giver and receiver:
            previous_picks.append(PreviousPick(Pick(giver, receiver), row.datetime))
        else:
            if not giver:
                print(f'unable to find Person record as giver for {row.giver_first} {row.giver_last}. '
                      f'ignoring entry in previous_pick list.')
            if not receiver:
                print(f'unable to find Person record as receiver for {row.receiver_first} {row.receiver_last}. '
                      f'ignoring entry in previous_pick list.')
    return previous_picks
