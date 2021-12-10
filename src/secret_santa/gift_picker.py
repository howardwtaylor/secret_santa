import copy
import time
from random import seed, randint, shuffle
from typing import List

from secret_santa.person import Person
from secret_santa.pick import Pick
from secret_santa.previous_pick import PreviousPick, find_giver_in_previous_picks


def identify_valid_recipients(giver: Person, remaining_recipients: List[Person], previous_picks: List[PreviousPick]) -> \
List[Person]:
    valid = []
    print('size(remaining_recipients)=', len(remaining_recipients))
    for recipient in remaining_recipients:
        # current set of rules for a valid recipient:
        #   #1: The recipient's person type must be one of the giver's
        #       recipient types. This allows for some givers to give to only
        #       a subset of the recipients based on their type.
        #       Example:  Grandparents are going to give gifts to the
        #       grandparents no matter what, so we limit their recipient
        #       list to the ADULTs only.
        #   #2: The giver must not be from the same household as the recipient.
        #       We assume that families will have their own gift exchanges as
        #       part of their holiday celebration, so we limit the recipients
        #       to those outside their household
        #   #3: Previous picks are removed from the set of valid recipients.
        #       The management of the set of previous picks is handled by the
        #       caller but expect to see the previous N years of picks rather
        #       than all previous picks.  Limiting this to only the last N years
        #       increases the chances of a valid solution.
        if ((giver.recipient_type & recipient.person_type) and
                (giver.household != recipient.household)):
            valid.append(recipient)
    # exclude any recipients that were previous picks
    print('size(valid) after recipient_type and household exclusions=', len(valid))
    for previous_pick in previous_picks:
        if previous_pick.pick.receiver in valid:
            valid.remove(previous_pick.pick.receiver)
            print(f"removed {previous_pick.pick.receiver} from valid recipient list")
    print('size(valid) after previous pick removal=', len(valid))
    return valid


class GiftPicker:
    def __init__(self, recipients: List[Person], previous_picks: List[PreviousPick]) -> None:
        self.recipients = recipients
        self.previous_picks = previous_picks

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
            shuffle(givers)  # this may not be a good idea.
            seed(time.time())  # use time in seconds to seed RNG
            remaining_recipients = copy.deepcopy(givers)
            chooseAgain = False
            for giver in givers:
                print(f'-----------------  Count = {count} ------------------------')
                print("Giver: " + str(giver))
                giver_previous_picks = find_giver_in_previous_picks(self.previous_picks, giver)
                valid_recipients = identify_valid_recipients(giver, remaining_recipients, giver_previous_picks)

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
                    print('************ Unable to finish.  Starting again **********')
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
