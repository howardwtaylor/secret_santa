from secret_santa import input_data
from secret_santa.input_data import load_input_data
from secret_santa.person import get_other_household_members
from secret_santa.message import build_email_message_body, build_wishlist_body
from secret_santa.pick import Pick


def test_build_email_message_body():
    # FIXME replace the filename below with your own modeled after input_template.csv
    fname = '../data/taylor_secret_santa_2020.csv'
    givers = load_input_data(fname)
    giver = givers[0]
    receiver = givers[7]

    household = get_other_household_members(receiver, givers)
    print(household)

    pick = Pick(giver, receiver)

    print('----------------')
    print(build_email_message_body(pick, household))
    print('----------------')

    assert True


def test_build_wishlist_body():
    fname = '../data/taylor_secret_santa_2020.csv'
    givers = load_input_data(fname)
    giver = givers[0]
    wishlist_body = build_wishlist_body(giver)

    print('----------------')
    print(wishlist_body)
    print('----------------')
