from secret_santa.input_data import load_input_data


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
