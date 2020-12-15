from secret_santa.person import Person


class Pick:

    def __init__(self, giver: Person, receiver: Person) -> None:
        self.giver = giver
        self.receiver = receiver

    def __str__(self) -> str:
        return 'Pick: from {self.giver.first} to {self.receiver.first}'.format(self=self)

    def __hash__(self) -> int:
        return hash((self.giver, self.receiver))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pick):
            return NotImplemented
        elif self is other:
            return True
        else:
            return self.giver == other.giver and \
                   self.receiver == other.receiver
