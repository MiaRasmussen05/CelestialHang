"""
File to store the functions for the player to give the game stars
and a review if they want to.
"""
import time
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore
colorama.init()

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
    global classification
    first = Fore.WHITE + "  A" + Fore.YELLOW
    second = Fore.WHITE + r"/ \ " + Fore.YELLOW
    third = Fore.WHITE + r"_______/   \_______" + Fore.YELLOW
    forth = Fore.WHITE + r"'.                 .'" + Fore.YELLOW
    fifth = Fore.WHITE + r"'.             .'" + Fore.YELLOW
    sixth = Fore.WHITE + "'.         .'" + Fore.YELLOW
    seventh = Fore.WHITE + r"/    .^.    \ " + Fore.YELLOW
    eight = Fore.WHITE + r"/ . '     ' . \ " + Fore.YELLOW
    ninth = Fore.WHITE + r"/'             '\ " + Fore.YELLOW
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    classification = input("Give stars here:\n").strip(' ').replace(",", ".")
    validation = validate_data(classification)
    time.sleep(0.4)
    while validation is None or validation is False:
        print("\nInvalid input. Please enter a number between 0 and 3.")
        print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
        classification_input = input("Give stars here:\n").strip(' ')
        classification = classification_input.replace(",", ".")
        validation = validate_data(classification)
    classification = float(classification)
    if classification >= 3:
        print(Fore.YELLOW + r"""
          A                      A                      A
         /*\                    /*\                    /*\
 _______/***\_______    _______/***\_______    _______/***\_______
'.*****************.'  '.*****************.'  '.*****************.'
  '.*************.'      '.*************.'      '.*************.'
    '.*********.'          '.*********.'          '.*********.'
    /****.^.****\          /****.^.****\          /****.^.****\
   /*. '     ' .*\        /*. '     ' .*\        /*. '     ' .*\
  /'             '\      /'             '\      /'             '\
        """ + Fore.WHITE)
    elif classification >= 2.8:
        print(Fore.YELLOW + fr"""
          A                      A                    {first}
         /*\                    /*\                    {second}
 _______/***\_______    _______/***\_______    {third}
'.*****************.'  '.*****************.'  '.*****************.'
  '.*************.'      '.*************.'      '.*************.'
    '.*********.'          '.*********.'          '.*********.'
    /****.^.****\          /****.^.****\          /****.^.****\
   /*. '     ' .*\        /*. '     ' .*\        /*. '     ' .*\
  /'             '\      /'             '\      /'             '\
    """ + Fore.WHITE)
    elif classification >= 2.5:
        print(Fore.YELLOW + fr"""
          A                      A                    {first}
         /*\                    /*\                    {second}
 _______/***\_______    _______/***\_______    {third}
'.*****************.'  '.*****************.'  {forth}
  '.*************.'      '.*************.'      {fifth}
    '.*********.'          '.*********.'          '.*********.'
    /****.^.****\          /****.^.****\          /****.^.****\
   /*. '     ' .*\        /*. '     ' .*\        /*. '     ' .*\
  /'             '\      /'             '\      /'             '\
    """ + Fore.WHITE)
    elif classification >= 2.3:
        print(Fore.YELLOW + fr"""
          A                      A                    {first}
         /*\                    /*\                    {second}
 _______/***\_______    _______/***\_______    {third}
'.*****************.'  '.*****************.'  {forth}
  '.*************.'      '.*************.'      {fifth}
    '.*********.'          '.*********.'          {sixth}
    /****.^.****\          /****.^.****\          {seventh}
   /*. '     ' .*\        /*. '     ' .*\        /*. '     ' .*\
  /'             '\      /'             '\      /'             '\
    """ + Fore.WHITE)
    elif classification >= 2:
        print(Fore.YELLOW + fr"""
          A                      A                    {first}
         /*\                    /*\                    {second}
 _______/***\_______    _______/***\_______    {third}
'.*****************.'  '.*****************.'  {forth}
  '.*************.'      '.*************.'      {fifth}
    '.*********.'          '.*********.'          {sixth}
    /****.^.****\          /****.^.****\          {seventh}
   /*. '     ' .*\        /*. '     ' .*\        {eight}
  /'             '\      /'             '\      {ninth}
    """ + Fore.WHITE)
    elif classification >= 1.8:
        print(Fore.YELLOW + fr"""
          A                    {first}                    {first}
         /*\                    {second}                   {second}
 _______/***\_______    {third}    {third}
'.*****************.'  '.*****************.'  {forth}
  '.*************.'      '.*************.'      {fifth}
    '.*********.'          '.*********.'          {sixth}
    /****.^.****\          /****.^.****\          {seventh}
   /*. '     ' .*\        /*. '     ' .*\        {eight}
  /'             '\      /'             '\      {ninth}
    """ + Fore.WHITE)
    elif classification >= 1.5:
        print(Fore.YELLOW + fr"""
          A                    {first}                    {first}
         /*\                    {second}                   {second}
 _______/***\_______    {third}    {third}
'.*****************.'  {forth}  {forth}
  '.*************.'      {fifth}      {fifth}
    '.*********.'          '.*********.'          {sixth}
    /****.^.****\          /****.^.****\          {seventh}
   /*. '     ' .*\        /*. '     ' .*\        {eight}
  /'             '\      /'             '\      {ninth}
    """ + Fore.WHITE)
    elif classification >= 1.3:
        print(Fore.YELLOW + fr"""
          A                    {first}                    {first}
         /*\                    {second}                   {second}
 _______/***\_______    {third}    {third}
'.*****************.'  {forth}  {forth}
  '.*************.'      {fifth}      {fifth}
    '.*********.'          {sixth}          {sixth}
    /****.^.****\          {seventh}         {seventh}
   /*. '     ' .*\        /*. '     ' .*\        {eight}
  /'             '\      /'             '\      {ninth}
    """ + Fore.WHITE)
    elif classification >= 1:
        print(Fore.YELLOW + fr"""
          A                    {first}                    {first}
         /*\                    {second}                   {second}
 _______/***\_______    {third}    {third}
'.*****************.'  {forth}  {forth}
  '.*************.'      {fifth}      {fifth}
    '.*********.'          {sixth}          {sixth}
    /****.^.****\          {seventh}         {seventh}
   /*. '     ' .*\        {eight}       {eight}
  /'             '\      {ninth}     {ninth}
    """ + Fore.WHITE)
    elif classification >= 0.8:
        print(Fore.YELLOW + fr"""
        {first}                    {first}                    {first}
         {second}                   {second}                   {second}
 {third}    {third}    {third}
'.*****************.'  {forth}  {forth}
  '.*************.'      {fifth}      {fifth}
    '.*********.'          {sixth}          {sixth}
    /****.^.****\          {seventh}         {seventh}
   /*. '     ' .*\        {eight}       {eight}
  /'             '\      {ninth}     {ninth}
    """ + Fore.WHITE)
    elif classification >= 0.5:
        print(Fore.YELLOW + fr"""
        {first}                    {first}                    {first}
         {second}                   {second}                   {second}
 {third}    {third}    {third}
{forth}  {forth}  {forth}
  {fifth}      {fifth}      {fifth}
    '.*********.'          {sixth}          {sixth}
    /****.^.****\          {seventh}         {seventh}
   /*. '     ' .*\        {eight}       {eight}
  /'             '\      {ninth}     {ninth}
    """ + Fore.WHITE)
    elif classification >= 0.3:
        print(Fore.YELLOW + fr"""
        {first}                    {first}                    {first}
         {second}                   {second}                   {second}
 {third}    {third}    {third}
{forth}  {forth}  {forth}
  {fifth}      {fifth}      {fifth}
    {sixth}          {sixth}          {sixth}
    {seventh}         {seventh}         {seventh}
   /*. '     ' .*\        {eight}       {eight}
  /'             '\      {ninth}     {ninth}
    """ + Fore.WHITE)
    elif classification >= 0:
        print(Fore.YELLOW + fr"""
        {first}                     {first}                    {first}
         {second}                    {second}                   {second}
 {third}     {third}    {third}
{forth}   {forth}  {forth}
  {fifth}       {fifth}      {fifth}
    {sixth}           {sixth}          {sixth}
    {seventh}          {seventh}         {seventh}
   {eight}        {eight}       {eight}
  {ninth}      {ninth}     {ninth}
    """ + Fore.WHITE)
    else:
        print("\nInvalid input. Please enter a number between 0 and 3.")
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)


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
