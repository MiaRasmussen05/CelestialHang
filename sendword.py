"""
Files to store the functions, scope and credits for the player
to be able to input their own word for review
"""
import time
import re
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


def new_words():
    """
    Let the visitor give own ideas for new words
    while putting them on a spreadsheet for review
    Run a while loop to collect a valid string of words
    Until the string of words is valid the loop reapeats itself.
    1-5 words, separated by commas.
    """
    print("                      Wait one second please!")
    time.sleep(2)
    print("""
      Before you go, do you have any words you want to add?
   Maybe a word you would like to see become apart of the game
                      Then now is your change!""")
    time.sleep(0.7)

    while True:
        question = input("""
          So do you have one or more? yes = y, no = n:\n""").lower().strip(' ')
        if question != "n":
            print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
            """)
        time.sleep(0.3)
        while True:
            if question == "y":
                print("""
If more then one word, they should be separated by commas.
Up till 5 words is permitted.
E.g: Virgo,Libra,Aries,Leo,Cancer""")
                ideas = input("\nEnter your word/s here:\n").strip(' ')
                ideas_value = ideas.split(",")
                if not re.match(r'^[\w\s]+(,\s*[\w\s]+)*$', ideas):
                    print("Please enter a valid string of words.\n")
                    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
            """)
                else:
                    if 1 <= len(ideas_value) <= 5:
                        return ideas_value
                    else:
                        print("""
        Please enter between 1 and 5 words, separated by commas\n""")
                        print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
            """)
            elif question == "n":
                print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
            """)
                return None
            else:
                print("                   I am sorry I didn't get that...")
                print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
            """)
                break
