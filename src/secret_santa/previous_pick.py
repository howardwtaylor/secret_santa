from datetime import datetime
from typing import List

from secret_santa.person import Person
from secret_santa.pick import Pick


class PreviousPick:

    def __init__(self, pick: Pick, date: datetime) -> None:
        self.pick = pick
        self.date = date

    def __str__(self) -> str:
        return 'Previous Pick: {self.date} from {self.pick.giver.first} to {self.pick.receiver.first}'.format(self=self)

    def __hash__(self) -> int:
        return hash((self.pick, self.date))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PreviousPick):
            return NotImplemented
        elif self is other:
            return True
        else:
            return self.pick == other.pick and \
                   self.date == other.date


# return any pick with the specified giver
def find_giver_in_previous_picks(previous_picks: List[PreviousPick], giver: Person) -> List[PreviousPick]:
    result = list()
    for previous_pick in previous_picks:
        if previous_pick.pick.giver == giver:
            result.append(previous_pick)
    return result


# return any pick newer than provided datetime (as dt)
def find_valid_recent_previous_picks(previous_picks: List[PreviousPick], dt: datetime) -> List[PreviousPick]:
    result = list()
    for previous_pick in previous_picks:
        if previous_pick.date > dt:
            result.append(previous_pick)
    return result
