from datetime import datetime

from dateutil.relativedelta import relativedelta

from input_data import load_input_data, load_previous_pick_data

from secret_santa.gift_picker import GiftPicker
from secret_santa.gmail_util import GmailUtil
from secret_santa.previous_pick import find_valid_recent_previous_picks

testing = True


def main():
    global testing

    #
    # this is the number of years to consider previous picks.
    #
    previous_pick_years = 3

    # fname = '../../data/input_template.csv'
    fname = '../../data/taylor_secret_santa_2021.csv'
    people = load_input_data(fname)

    print("------------------- Givers and Receivers --------------")
    # loop over all of the recipients
    for person in people:
        print(person)
    print('')

    # load previous pick data
    previous_pick_fname = '../../data/taylor_secret_santa_previous_picks.csv'
    previous_pick_data = load_previous_pick_data(people, previous_pick_fname)

    print('-------------- Previous Pick List ---------------------')
    for previous_pick in previous_pick_data:
        print(previous_pick)

    # find start date for valid window of previous picks.  rewind another 6 months to be safe
    newer_than = datetime.now() - relativedelta(years=previous_pick_years) - relativedelta(months=6)
    valid_previous_picks = find_valid_recent_previous_picks(previous_pick_data, newer_than)

    # pick the gifts for the recipients
    giftPicker = GiftPicker(people, valid_previous_picks)
    (picks, iterations) = giftPicker.the_choosing()

    gmail_util = GmailUtil()

    # report the assigned choices
    print("Secret Santa Picks:")
    for pick in picks:
        if testing:
            print(str(pick))
        else:
            gmail_util.send_pick(pick, people)
            print('----------------')

    # send this year's picks to Secret Santa gmail account for posterity
    if not testing:
        gmail_util.send_pick_list(picks, iterations)


if __name__ == "__main__":
    main()
