import input_data
from gift_picker import GiftPicker


def main():
    # define all of the inputs and return a dictionary
    # with 3 keys: addresses, households and recipients
    recipients = input_data.assignments()

    print("Givers and Receivers:")
    # loop over all of the recipients
    for x in recipients:
        print(x)
    print('')

    # pick the gifts for the recipients
    giftPicker = GiftPicker(recipients)
    picks = giftPicker.theChoosing()

    # report the assigned choices
    print("Secret Santa Picks:")
    for pick in picks:
        print(pick)
    print('')


if __name__ == "__main__":
    main()
