from input_data import load_input_data, load_previous_pick_data

from secret_santa.gmail_util import GmailUtil
from secret_santa.message import build_wishlist_body

testing = False


def main():
    global testing
    gmail_util = GmailUtil()

    # fname = '../../data/input_template.csv'
    fname = '../../data/taylor_secret_santa_2021.csv'
    people = load_input_data(fname)
    for person in people:
        if not testing:
            gmail_util.send_wishlist(person)
        else:
            print(person)


if __name__ == "__main__":
    main()
