"""
Imports
"""
import time
import random
import time
import colorama
from colorama import Fore, Style
from words import easy_words, medium_words, hard_words, special_words
import hangman
colorama.init()


def welcome_to():
    """
    Welcome to the game art
    """
    print(r"""       __        __   _                            _
       \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___
        \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \
         \ V  V /  __/ | (__ (_) | | | | | |  __/ | |_ (_) |
          \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ """)


def logo():
    """
    Celestial Hang logo
    """
    print(r"""     ____     _          _   _       _ _   _
    / ___|___| | ___ ___| |_(_) __ _| | | | | __ _ _ __   __ _
   | |   / _ \ |/ _ \ __| __| |/ _` | | |_| |/ _` | '_ \ / _` |
   | |___  __/ |  __\__ \ |_| | (_| | |  _  | (_| | | | | (_| |
    \____\___|_|\___|___/\__|_|\__,_|_|_| |_|\__,_|_| |_|\__, |
                                                         |___/ """)

    print(r"""      *   '      o           .       +         .        *
     .                   ~+   __________  +    |   '
        .   |       *      .  |/       |     - o -       +
     *    - o -               |   +    | .     |      .
            |      .   '      |        |     o             '
       +       ~+           * |        O  *       +    *
     .               *        |  '    /|\       '         .
            '              +  |       / \  .   ~~+     .    *
     *           o         .  |       *             o
     '    +    '       *      |    o       *     .      +
     ________________________/|\____________________________""" + "\n")


def welcome_player():
    """
    Input a name to have a more personalized response
    Color for the name verible
    With a message to really welcome the visitor
    Run the rules function
    """
    global name
    name_col = input("Please enter you name here:\n")
    name = Fore.MAGENTA + Style.BRIGHT + name_col + Fore.WHITE
    print("\n" + f"""                          Welcome {name}
               I hope you have fun and good luck!""" + "\n")
    time.sleep(1)
    separator()
    rules()
    separator()
    time.sleep(1)


def separator():
    """
    Function to print separators to keep the different functions separated
    """
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)


def rules():
    """
    Inform the player about the game rules
    Implement color for the rules function
    """
    print(Fore.CYAN + """                     Here comes the rules...""" "\n")
    time.sleep(1)
    print("1. Try to see if you can guess the celestial themed word" + "\n")
    time.sleep(0.6)
    print("""2. You play by inputing one letter, if the letter is in the word
   then you get another change but is the letter not then you lose a life""")
    time.sleep(0.6)
    print("""
3. Can you guess the word before the person gets hung or it's game over.""")
    time.sleep(0.6)
    print("""
4. Remeber choose the difficulty level carefully the higher you go the harder
   the word is to guess. However the more points you get as well.
   For each won game - Easy gives 1 point, Medium gives 2 points,
   Hard gives 3 points, and the special level gives 4 points""")
    time.sleep(0.6)
    print("""
5. Hidden in the scores there is a key. Are you the one that can find it
   to unlock the special level. Only one score will allow you to see the key,
   but you will still unlock the hidden level by passing it!""" + Fore.WHITE)


def get_word():
    """
    Gets and chooses a random word from words file
    out from which difficulty has been choosen
    """
    word_e = random.choice(easy_words)
    word_m = random.choice(medium_words)
    word_h = random.choice(hard_words)
    word_s = random.choice(special_words)
