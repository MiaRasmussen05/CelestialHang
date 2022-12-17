"""
All different art function for when the game is over
"""

import colorama
from colorama import Fore
colorama.init()


def game_over_art():
    """
    Game art for when the player loses a round
    """
    first = Fore.RED + "____" + Fore.WHITE
    second = Fore.RED + r"___" + Fore.WHITE
    third = Fore.RED + r"/ ___| __ _" + Fore.WHITE
    forth = Fore.RED + r"_ __ ___   ___" + Fore.WHITE
    fifth = Fore.RED + r"/ _ \__" + Fore.WHITE
    sixth = Fore.RED + "_____ _ __" + Fore.WHITE
    seventh = Fore.RED + r"| |  _ / _` | '_ ` _ \ / _ \ " + Fore.WHITE
    eight = Fore.RED + r"| | | \ \ / / _ \ '__|" + Fore.WHITE
    ninth = Fore.RED + r"| |_| | (_| | | | | | |  __/" + Fore.WHITE
    tenth = Fore.RED + r"| |_| |\ V /  __/ |" + Fore.WHITE
    eleventh = Fore.RED + r"\____|\__,_|_| |_| |_|\___|" + Fore.WHITE
    twelfth = Fore.RED + r"\___/  \_/ \___|_|" + Fore.WHITE
    print(f"""      *   '      o           .       +         .        *
    .     {first} +   '    .    ~+        {second}    *       '     +
        '{third}+{forth} * {fifth} . {sixth}    '
  *     {seventh}{eight}'  *
    ~+ .{ninth} {tenth}    .
         {eleventh}  {twelfth}  *
     +   *           o     '   .  +       *       '     o    ~+
        '    +    '       *      '    o       *     .      +
        """)


def hidden_art():
    """
    Game art for if the player finds the hidden key when they
    unlock the special level
    """
    first = Fore.YELLOW + ",------." + Fore.WHITE
    second = Fore.YELLOW + r'/   ,--.  "______________' + Fore.WHITE
    third = Fore.YELLOW + r"|   |    |                 |" + Fore.WHITE
    forth = Fore.YELLOW + r"\   '--'  .__||__|__||___'" + Fore.WHITE
    fifth = Fore.YELLOW + r'"------"' + Fore.WHITE
    print(f"""      *          o     .     .       +         .        *
     .                  ~+                +    |   '        .
        .   |       *     .     '     '      - o -       +
     *    - o -        {first}  *     .   .   |      .
            |      . {second}    .   '     '
       +       ~+   {third}  +    *
     .          .    {forth} '    .    .
            '        + {fifth}           .    ~~+     .    *
     *           o        .      *   '       .      o
     '    +    '       *       .    +      *     .      +
        """)
        