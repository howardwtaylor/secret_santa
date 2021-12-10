from datetime import datetime, timedelta
from secret_santa.person import Person
from secret_santa.pick import Pick
from typing import List

family = "Taylor"
signature = "H"


# set deadline to return wishlist as 2 days from now
def get_deadline() -> str:
    deadline = datetime.now() + timedelta(days=2)
    return deadline.strftime("%A, %B %d, %Y")


def build_email_message_body(pick: Pick, household_members: List[Person]) -> str:
    part1 = """\
Hello %s,

Welcome to the %s Secret Santa Gift Exchange!

For you, we picked %s from the hat.  You probably already
have contact info but in case you don't, here it is:

""" % (pick.giver.first, family, pick.receiver.first)
    if pick.receiver.email_address:
        part1 += f"    email: {pick.receiver.full_email()}\n"
    if pick.receiver.phone_number:
        part1 += f"    phone: {pick.receiver.phone_number}\n"

    if len(household_members) > 0:
        part2 = """
If you are having trouble thinking of a gift, here is a list of
other household members that you can contact for ideas:
"""
        for person in household_members:
            part2 += f'    {str(person)}\n'
    else:
        part2 = ''

    if pick.receiver.wishlist_link:
        part3 = """
If you aren't able to find a gift idea after talking with the other
people in the family, you can take a look at their wishlist:
"""
        part3 += f'    {pick.receiver.wishlist_link}\n'
    else:
        part3 = ''

    part4 = """
The target gift cost is between $30 and $50, whatever you're comfortable
paying.  If you disagree and would like to discuss altering the rules,
please let me know.  Same goes for any problems you might find with
how the secret santa process works.

Merry Christmas,
%s
""" % signature
    message = part1 + part2 + part3 + part4

    return message


def build_pick_list(picks: List[Pick], iterations: int) -> str:
    result = """
The choosing took %d iterations this year.

The picks were:

""" % iterations

    for pick in picks:
        result += f'{str(pick)}\n'
    result += '\n'
    return result


def build_wishlist_body(person: Person) -> str:
    result = """
Hello %s,

In preparation for the %s Secret Santa choosing, please verify
that the following link is still suitable and contains your
preferred gift ideas for this year.

    %s

If this is not the right wishlist, please reply to this message
with the correct link by %s.

""" % (person.first, family, person.wishlist_link, get_deadline())
    return result
