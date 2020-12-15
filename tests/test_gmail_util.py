from secret_santa.input_data import load_input_data
from secret_santa.message import build_email_message_body
from secret_santa.gmail_util import GmailUtil
from secret_santa.person import get_other_household_members
from secret_santa.pick import Pick


def build_body() -> str:
    # FIXME replace the filename below with your own modeled after input_template.csv
    fname = '../data/taylor_secret_santa_2020.csv'
    givers = load_input_data(fname)
    giver = givers[0]
    receiver = givers[7]
    household = get_other_household_members(receiver, givers)
    pick = Pick(giver, receiver)
    return build_email_message_body(pick, household)


def test_send_ssl():

    gmail_util = GmailUtil()

    # FIXME: the two entries below need to be modified for this test to work
    recipient_name = "Your Name Here"
    recipient_addr = "ynh@hotmail.com"
    subject = "testing secret santa"
    body = build_body()
    gmail_util.sendSSL(recipient_name, recipient_addr, subject, body)

    assert True
