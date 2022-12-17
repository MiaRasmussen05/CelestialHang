"""
File to store the functions for the player to give the game stars
and a review if they want to.
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('celestial_hang')


def stars():
    """
    Let the visitor give stars and review of the game
    while putting them on a spreadsheet
    """
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    print("Please take a second to give us a review between 0 and 3 stars!")
    print("Stars e.g: 2.7")
    classification = input("Give stars here:\n").strip(' ').replace(",", ".")


def validate_data(values):
    """
    Validates a given value to ensure that it is a
    number between 0 and 3.
    With it being a float to make sure
    that the input can also be 2.4 and not just a whole number.
    """
    try:
        values = float(values)
        if 0 <= values <= 3:
            return True
        else:
            return False
    except ValueError:
        return False
