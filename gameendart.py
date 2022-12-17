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


def art_twentyfive():
    """
    Game art for if the player hits the score of 25
    """
    first = Fore.CYAN + "_____   _______" + Fore.WHITE
    second = Fore.CYAN + r"|___   \|    ___|" + Fore.WHITE
    third = Fore.CYAN + r"\   |   |__" + Fore.WHITE
    forth = Fore.CYAN + r"__/   |___   \ " + Fore.WHITE
    fifth = Fore.CYAN + r"/   __/    \   |" + Fore.WHITE
    sixth = Fore.CYAN + "|   |___ ___/   |" + Fore.WHITE
    seventh = Fore.CYAN + "|_______|_____ /" + Fore.WHITE
    print(f"""      *     ,    o     .     .       +         .        *
     .           .     ~+ {first} +    |   '        .
        .   |       *    {second}   - o -       +
     *    - o -            . {third}   .   |      .
            |      .   '   {forth}   o             '
       +       ~+         {fifth}*       +    *
     .               *   {sixth}  .   '    .    .
            '          . {seventh}      ~~+     .   *
     *           o        '    .    *               o
     '    +    '       *     '   +     .   *     .      +
            """)


def art_fifty():
    """
    Game art for if the player hits the score of 50
    """
    first = Fore.CYAN + "_______  ______" + Fore.WHITE
    second = Fore.CYAN + r"|    ___|/  __  \ " + Fore.WHITE
    third = Fore.CYAN + r"|   |__ |  |  |  |" + Fore.WHITE
    forth = Fore.CYAN + r"|___   \|  |  |  |" + Fore.WHITE
    fifth = Fore.CYAN + r"\   |  |  |  |" + Fore.WHITE
    sixth = Fore.CYAN + "___/   |  |__|  |" + Fore.WHITE
    seventh = Fore.CYAN + r"|_____ / \______/" + Fore.WHITE
    print(f"""      *     ,    o     .     .       +         .        *
     .           .     ~+ {first} +    |   '        .
        .   |       *    {second}  - o -       +
     *    - o -          {third}.   |      .
            |      .   ' {forth}  o             '
       +       ~+          , {fifth}       +    *
     .               *    {sixth} .   '    .    .
            '          . {seventh}     ~~+     .   *
     *           o        '    .    *               o
     '    +    '       *     '   +     .   *     .      +
            """)


def art_seventyfive():
    """
    Game art for if the player hits the score of 75
    """
    first = Fore.CYAN + "_________ _______" + Fore.WHITE
    second = Fore.CYAN + r"|______   |    ___|" + Fore.WHITE
    third = Fore.CYAN + r"/  /|   |__" + Fore.WHITE
    forth = Fore.CYAN + r"/  / |___   \ " + Fore.WHITE
    fifth = Fore.CYAN + r"/  /" + Fore.WHITE
    sixth = Fore.CYAN + r"\   |" + Fore.WHITE
    seventh = Fore.CYAN + "/  /" + Fore.WHITE
    eight = Fore.CYAN + r"___/   |" + Fore.WHITE
    ninth = Fore.CYAN + r"/__/    |_____ /" + Fore.WHITE
    print(f"""      *     ,    o     .     .       +         .        *
     .           .    ~+ {first} +      |         .
        .   |       *   {second}     - o -    +
     *    - o -            o  {third}  .      |   .
            |      .   '     {forth}  o             '
       +       ~+         + {fifth}    . {sixth}       +    *
     .               *     {seventh} ,  {eight} .   '    .    .
            '          .  {ninth}     ~~+     .   *
     *           o        '    .    *               o
     '    +    '       *     '   +     .   *     .      +
            """)


def art_onehundred():
    """
    Game art for if the player hits the score of 100
    """
    first = Fore.CYAN + "____  ______" + Fore.WHITE
    second = Fore.CYAN + r"______" + Fore.WHITE
    third = Fore.CYAN + r"/    |/  __  \ /  __  \ " + Fore.WHITE
    forth = Fore.CYAN + r"/_    |  |  |  |  |  |  |" + Fore.WHITE
    fifth = Fore.CYAN + r"|   |  |  |  |  |  |  |" + Fore.WHITE
    sixth = Fore.CYAN + r"|   |  |  |  |  |  |  |" + Fore.WHITE
    seventh = Fore.CYAN + "|   |  |__|  |  |__|  |" + Fore.WHITE
    eight = Fore.CYAN + r"|___|\______/ \______/" + Fore.WHITE
    print(f"""      *     ,    o     .     .       +         .        *
     .          .   ~+ {first} . {second}+      |         .
        .   |       * {third}    - o -    +
     *    - o -      {forth}.    |   .
            |      .   {fifth}   o          '
       +       ~+      {sixth}    +    *
     .               * {seventh}  '    .    .
            '          {eight}  ~~+     .   *
     *           o   '    '    .    *               o
     '    +    '       *     '   +     .   *     .      +
            """)


def normal_art():
    """
    Game art for when the player wins a round
    """
    first = Fore.YELLOW + "____________" + Fore.WHITE
    second = Fore.YELLOW + r".-\    _     /-." + Fore.WHITE
    third = Fore.YELLOW + r"| (|   / |    |) |" + Fore.WHITE
    forth = Fore.YELLOW + r"'-|     |    |-'" + Fore.WHITE
    fifth = Fore.YELLOW + r"\    _|_   /" + Fore.WHITE
    sixth = Fore.YELLOW + "'.      .'" + Fore.WHITE
    seventh = Fore.YELLOW + r"_`)  (`_" + Fore.WHITE
    eight = Fore.YELLOW + r"_/________\_" + Fore.WHITE
    ninth = Fore.YELLOW + r"/____________\ " + Fore.WHITE
    print(f"""      *     .    o     .     .       +         .        *
     .           .      ~+ {first}   +    |   '        .
        .   |       *    {second}    - o -       +
     *    - o -         {third} .   |      .
            |      .   ' {forth}    o             '
       +       ~+         .{fifth}   *       +    *
     .               *      {sixth}  .       '    .    .
            '          .   + {seventh}      .   ~~+     .   *
     *           o        .{eight}             o
     '    +    '       *  {ninth}  *     .      +
            """)
