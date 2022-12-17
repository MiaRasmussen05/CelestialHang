"""
Imports
"""
import time
import colorama
from colorama import Fore, Style
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


def separator():
    """
    Function to print separators to keep the different functions separated
    """
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
