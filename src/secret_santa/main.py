from input_data import load_input_data

from secret_santa.gift_picker import GiftPicker
from secret_santa.gmail_util import GmailUtil


def main():
    # fname = '../../data/input_template.csv'
    fname = '../../data/taylor_secret_santa_2020.csv'
    recipients = load_input_data(fname)

    print("Givers and Receivers:")
    # loop over all of the recipients
    for recipient in recipients:
        print(recipient)
    print('')

    # pick the gifts for the recipients
    giftPicker = GiftPicker(recipients)
    (picks, iterations) = giftPicker.the_choosing()

    gmail_util = GmailUtil()

    # report the assigned choices
    print("Secret Santa Picks:")
    for pick in picks:
        gmail_util.send_pick(pick, recipients)
        print('----------------')

    # send this year's picks to Secret Santa gmail account for posterity
    gmail_util.send_pick_list(picks, iterations)


if __name__ == "__main__":
    main()
