import copy
import time
from random import seed, randint
from typing import List

from secret_santa.person import Person
from secret_santa.pick import Pick


def identify_valid_recipients(giver: Person, remaining_recipients: List[Person]) -> List[Person]:
    valid = []
    for recipient in remaining_recipients:
        # test to see if giver and receiver are in the same household
        # current set of tests:
        #   The person's type must be one of the giver's recipient types and
        #   the giver must not be from the same household as the recipient
        if ((giver.recipient_type & recipient.person_type) and
                (giver.household != recipient.household)):
            valid.append(recipient)
    return valid


class GiftPicker:
    def __init__(self, recipients: List[Person]) -> None:
        self.recipients = recipients

    def the_choosing(self) -> (List[Pick], int):
        # sort the list of givers by the number of available recipients
        # givers = self.sortGiversByNumberOfRecipients()
        givers = copy.deepcopy(self.recipients)
        chooseAgain: bool = True
        count: int = 0
        picks = []
        while chooseAgain:
            # print("iteration " + str(count))
            picks = []
            seed(time.time())  # use time in seconds to seed RNG
            remaining_recipients = copy.deepcopy(givers)
            chooseAgain = False
            for giver in givers:
                print("Giver: " + str(giver))
                valid_recipients = identify_valid_recipients(giver, remaining_recipients)

                # print("valid recipients")
                # for validRecipient in validRecipients:
                #    print(validRecipient)

                nRecipients = len(valid_recipients)
                if nRecipients > 0:
                    recipientIndex = randint(0, nRecipients - 1)
                    recipient = valid_recipients[recipientIndex]
                    picks.append(Pick(giver, recipient))
                    remaining_recipients.remove(recipient)
                    # print("recipient = " + str(recipient))
                    # print('\n')
                else:
                    # print("Reached index " + str(idx) + " of " + str(len(givers)) + '.  Starting again...')
                    # print("list was:")
                    # for x in picks:
                    #    print('    from ' + x.giver.first + ' to ' + x.receiver.first)
                    # print("remaining givers list:")
                    # for x in range(idx, len(givers)):
                    #    print('\t' + str(givers[x]))
                    # print("remaining receivers list:")
                    # for x in remainingRecipients:
                    #    print("\t" + str(x))
                    # print('\n')
                    chooseAgain = True
                    break  # Unable to finish. start while loop again
            count += 1
        print('found picks on iteration #' + str(count) + '\n')
        return picks, (count + 1)

    # sort givers by the number of recipients to whom they can give
    def sort_givers_by_number_of_recipients(self) -> List[Person]:
        givers = []
        for giver in self.recipients:
            valid_recipients = identify_valid_recipients(giver, self.recipients)
            givers.append((giver, len(valid_recipients)))
        givers.sort(key=lambda x: x[1])
        # pick off only the first element of each tuple
        sorted_givers = [idx for idx, val in givers]
        return sorted_givers
