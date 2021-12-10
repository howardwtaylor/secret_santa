from datetime import datetime, timedelta
from email.utils import formataddr
import smtplib

from secret_santa.message import build_pick_list, build_email_message_body, build_wishlist_body
from secret_santa.my_secrets import gmail_fullname, gmail_username, gmail_password
from typing import List

from secret_santa.person import get_other_household_members, Person
from secret_santa.pick import Pick


def get_year() -> str:
    now = datetime.now()
    return now.strftime("%Y")


class GmailUtil:

    def __init__(self) -> None:
        # email.utils.formataddr("Fred Flintstone", "fred.flintstone@gmail.com")
        self.name = gmail_fullname
        self.username = gmail_username
        self.sender = formataddr((gmail_fullname, gmail_username))

    def send_pick(self, pick: Pick, recipients: List[Person]) -> None:
        subject = f"Secret Santa Pick for {get_year()}"
        household = get_other_household_members(pick.receiver, recipients)
        body = build_email_message_body(pick, household)
        # print(body)
        self.sendSSL(pick.giver.full_name(), pick.giver.email_address, subject, body)

    def send_pick_list(self, picks: List[Pick], iterations: int) -> None:
        subject = f"Secret Santa picks for {get_year()}"
        body = build_pick_list(picks, iterations)
        self.sendSSL(self.name, self.username, subject, body)

    def send_wishlist(self, person: Person) -> None:
        if person.wishlist_link:
            subject = f"Your Secret Santa Wishlist for {get_year()}"
            body = build_wishlist_body(person)
            self.sendSSL(person.full_name(), person.email_address, subject, body)
            print(f"Wishlist reminder sent to {person.full_name()}: {person.wishlist_link}")
        else:
            print(f"No wishlist on file for {person.full_name()}")

    def sendSSL(self, recipient_name: str, recipient_address: str, subject: str, body: str) -> None:
        recipient = formataddr((recipient_name, recipient_address))
        email_text = 'From: %s\n' % self.sender
        email_text += 'To: %s\n' % recipient
        email_text += 'Subject: %s\n' % subject
        email_text += '\n'
        email_text += body
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.ehlo()
            server.login(gmail_username, gmail_password)
            server.sendmail(self.sender, recipient, email_text)
