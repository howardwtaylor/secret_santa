import copy
import time
from random import seed, randint
from typing import List

from person import Person
from pick import Pick


def identifyValidRecipients(giver: Person, remainingRecipients: List[Person]) -> List[Person]:
    valid = []
    for recipient in remainingRecipients:
        # test to see if giver and receiver are in the same household
        if giver.household != recipient.household:
            valid.append(recipient)
    return valid


class GiftPicker:
    def __init__(self, recipients: List[Person]) -> None:
        self.recipients = recipients

    def theChoosing(self) -> List[Pick]:
        # sort the list of givers by the number of available recipients
        # givers = self.sortGiversByNumberOfRecipients()
        givers = copy.deepcopy(self.recipients)
        chooseAgain: bool = True
        count: int = 0
        while chooseAgain:
            # print("iteration " + str(count))
            picks = []
            seed(time.time())  # use time in seconds to seed RNG
            remainingRecipients = copy.deepcopy(givers)
            chooseAgain = False
            for idx in range(len(givers)):
                giver = givers[idx]
                # print("Giver: " + str(giver))
                validRecipients = identifyValidRecipients(giver, remainingRecipients)

                # print("valid recipients")
                # for validRecipient in validRecipients:
                #    print(validRecipient)

                nRecipients = len(validRecipients)
                if nRecipients > 0:
                    recipientIndex = randint(0, nRecipients - 1)
                    recipient = validRecipients[recipientIndex]
                    picks.append(Pick(giver, recipient))
                    remainingRecipients.remove(recipient)
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
        return picks

    # sort givers by the number of recipients to whom they can give
    def sortGiversByNumberOfRecipients(self) -> List[Person]:
        givers = []
        for giver in self.recipients:
            validRecipients = identifyValidRecipients(giver, self.recipients)
            givers.append((giver, len(validRecipients)))
        givers.sort(key=lambda x: x[1])
        # pick off only the first element of each tuple
        sortedGivers = [idx for idx, val in givers]
        return sortedGivers
