"""
Imports
"""
import time
import random
import string
import colorama
from colorama import Fore, Style
from words import easy_words, medium_words, hard_words, special_words
import hangman
colorama.init()


# Veriables
score = 0


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

    if level == "E":
        return word_e
    elif level == "M":
        return word_m
    elif level == "H":
        return word_h
    elif level == "S":
        return word_s
    else:
        print("A mistake has happened, try again")


def game():
    """
    Function for the actul game play
    a random word using single letters guesses with a
    specific number of lives to get to the correct
    hidden word.
    """
    global lives
    global score
    global guess
    global word
    lives = level_difficulty()
    time.sleep(1)
    choosen()
    word = get_word()
    word_col = Fore.BLUE + Style.BRIGHT + word + Fore.WHITE
    alphabet = set(string.ascii_lowercase)
    needed_letters = set(word)
    guessed_letters = set()
    separator()
    time.sleep(0.5)

    while len(needed_letters) > 0 and lives > 0:
        guess = []
        for letter in word:
            if letter == ' ':
                guess.append(' ')
                # Added append first to show the space between 2 word
                # Then discard it from the list of needed letters
                needed_letters.discard(letter)
            elif letter in guessed_letters:
                guess.append(letter)
            else:
                guess.append('_')

        if level == "E":
            print(hangman.__E_LIVES__[lives])
        elif level == "M":
            print(hangman.__M_LIVES__[lives])
        elif level == "H":
            print(hangman.__H_LIVES__[lives])
        else:
            print(hangman.__S_LIVES__[lives])

        print('The current word: ', ' '.join(guess))

        user_guessed = input("""
Please write a letter here:\n""").lower().strip(' ')

        if user_guessed in alphabet - guessed_letters:
            guessed_letters.add(user_guessed)
            if user_guessed in needed_letters:
                needed_letters.remove(user_guessed)
                print('\nYou are so smart,', user_guessed, 'is in the word')

            else:
                lives = lives - 1
                print(f"""
Oh no, {user_guessed} is not in the word, try again!""")

        elif user_guessed in guessed_letters:
            print("\nYou've tried this letter already. Please try another.")

        else:
            print('\nInvalid character used! please type in a valid letter.')

        separator()

    if lives == 0:
        if level == "E":
            print(hangman.__E_LIVES__[lives])
        elif level == "M":
            print(hangman.__M_LIVES__[lives])
        elif level == "H":
            print(hangman.__H_LIVES__[lives])
        else:
            print(hangman.__S_LIVES__[lives])


def level_difficulty():
    """
    Choose level difficulty
    """
    green = Fore.GREEN + "easy" + Fore.WHITE
    green_e = Fore.GREEN + "E" + Fore.WHITE
    yellow = Fore.YELLOW + "medium" + Fore.WHITE
    yellow_m = Fore.YELLOW + "M" + Fore.WHITE
    red = Fore.RED + "hard" + Fore.WHITE
    red_h = Fore.RED + "H" + Fore.WHITE
    blue = Fore.BLUE + "special" + Fore.WHITE
    blue_s = Fore.BLUE + "S" + Fore.WHITE

    if score >= 32:
        print("""
         Choose one of the four levels to get started...""" + "\n")
    else:
        print("""
         Choose one of the three levels to get started...""" + "\n")
    time.sleep(0.6)
    print(f"""                        For {green} click {green_e}
                        For {yellow} click {yellow_m}
                        For {red} click {red_h}""")
    if score >= 32:
        print(f"""                  For the {blue} level click {blue_s}""")


    difficulty = True

    while difficulty:
        global level
        global level_col
        level = input(f"""
            {name} please choose a difficulty here:\n""").upper().strip(' ')
        print("")
        separator()
        time.sleep(0.4)
        if level == "E":
            level_col = Fore.GREEN + level + Fore.WHITE
            print(Fore.GREEN + r"""
                      _____
                     | ____|__ _ ___ _   _
                     |  _| / _` / __| | | |
                     | |___ (_| \__ \ |_| |
                     |_____\__,_|___/\__, |
                                     |___/
            """ + Fore.WHITE)
            lives = 5
            return lives
        elif level == "M":
            level_col = Fore.YELLOW + level + Fore.WHITE
            print(Fore.YELLOW + r"""
               __  __          _ _
              |  \/  | ___  __| (_)_   _ _ __ ___
              | |\/| |/ _ \/ _` | | | | | '_ ` _ \
              | |  | |  __/ (_| | | |_| | | | | | |
              |_|  |_|\___|\__,_|_|\__,_|_| |_| |_|
            """ + Fore.WHITE)
            lives = 7
            return lives
        elif level == "H":
            level_col = Fore.RED + level + Fore.WHITE
            print(Fore.RED + r"""
                      _   _               _
                     | | | | __ _ _ __ __| |
                     | |_| |/ _` | '__/ _` |
                     |  _  | (_| | | | (_| |
                     |_| |_|\__,_|_|  \__,_|
            """ + Fore.WHITE)
            lives = 10
            return lives
        if score >= 32:
            if level == "S":
                level_col = Fore.BLUE + level + Fore.WHITE
                print(Fore.BLUE + r"""
                 ____                  _       _
                / ___| _ __   ___  ___(_) __ _| |
                \___ \| '_ \ / _ \/ __| |/ _` | |
                 ___) | |_) |  __/ (__| | (_| | |
                |____/| .__/ \___|\___|_|\__,_|_|
                      |_|
                """ + Fore.WHITE)
                lives = 11
                return lives
        else:
            if score >= 32:
                print("""
         Please write one of the following: E, M, H or S
             to choose the difficulty level you want.
                """)
            else:
                print("""
         Please write one of the following: E, M or H
           to choose the difficulty level you want.
                """)


def choosen():
    """
    Message to show the player which level they have choosen as the game loads
    """
    separator()
    print(f"             {name} you choose {level_col} so let's get started!")
