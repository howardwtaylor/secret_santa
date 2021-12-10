from secret_santa.input_data import load_input_data, load_previous_pick_data


def test_load_input_data():
    # FIXME replace the filename below with your own modeled after input_template.csv
    fname = '../data/taylor_secret_santa_2020.csv'
    data = load_input_data(fname)
    print('\n')
    for person in data:
        print(f'{person.first}, {person.last}, {person.household}, '
              f'{person.person_type},{person.recipient_type}, {person.email_address}, '
              f'{person.phone_number}, {person.wishlist_link}')
    assert True


def test_load_previous_pick_data():
    # to use these, must add FRED_AND_WILMA and BARNEY_AND_BETTY
    # to HOUSEHOLD in person.py
    # person_fname = '../data/input_template.csv'
    # previous_pick_fname = '../data/previous_pick_template.csv'
    person_fname = '../data/taylor_secret_santa_2021.csv'
    previous_pick_fname = '../data/taylor_secret_santa_previous_picks.csv'
    people_data = load_input_data(person_fname)
    previous_pick_data = load_previous_pick_data(people_data, previous_pick_fname)
    print('\n')
    for person in people_data:
        print(person)
    for previous_pick in previous_pick_data:
        print(previous_pick)
    assert True
