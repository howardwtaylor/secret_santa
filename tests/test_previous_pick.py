from datetime import datetime, date

from secret_santa.input_data import load_input_data, load_previous_pick_data
from secret_santa.person import find_person_by_full_name
from secret_santa.previous_pick import find_giver_in_previous_picks, find_valid_recent_previous_picks


def test_find_giver_in_previous_picks():
    # to use these, must add FRED_AND_WILMA and BARNEY_AND_BETTY
    # to HOUSEHOLD in person.py
    person_fname = '../data/input_template.csv'
    previous_pick_fname = '../data/previous_pick_template.csv'
    # person_fname = '../data/taylor_secret_santa_2021.csv'
    # previous_pick_fname = '../data/taylor_secret_santa_previous_picks.csv'
    people_data = load_input_data(person_fname)
    previous_pick_data = load_previous_pick_data(people_data, previous_pick_fname)
    print('\n')
    for person in people_data:
        print(person)
    for previous_pick in previous_pick_data:
        print(previous_pick)

    giver = find_person_by_full_name(people_data, "Barney", "Rubble")
    newer_than = datetime(2019, 6, 1)  # year, month, day
    valid_previous_picks = find_valid_recent_previous_picks(previous_pick_data, newer_than)
    barney_previous_picks = find_giver_in_previous_picks(valid_previous_picks, giver)
    print("------- Previous Picks With Barney as Giver -----------")
    for previous_pick in barney_previous_picks:
        print(previous_pick)
    assert True
