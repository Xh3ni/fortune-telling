"""
This section import the following classes:
OpeningMessage and EndingMessage
The random module is also imported
"""
from OpeningMessage import OpeningMessage
from EndingMessage import EndingMessage
from PandasToList import PandasToList
import random

"""
As soon as the program runs a message is displayed.
This message comes from the OpeningMessage class
as shown below.
"""
m = OpeningMessage()
m.__init__(filename='fortuneTelleingIntroduction.txt')
print(m.open_file())
m.open_file()

"""
The PandaToList is then invoked. This is done to 
retrieve a list for upright cards and another 
list for reverse cards.
"""
p = PandasToList()
list_reverse_taro = p.upright_deck('tarotCardsUpright.csv')
list_upright_taro = p.reverse_deck('tarotCardsReversed.csv')



while True:
    """
    while True keeps the user input alive
    """
    try:
        """
        try block is added for exception handling
        """

        # prompt user to enter an option
        user_input = int(input(
            "\n What type of Fortune reading would you like?"
            "Please, enter a number that correspondens to an available option.\n"
            "1: Monthly Horoscope\n"
            "2: Standart Major Arcana Spread\n"
            "3: Exit\n"
            "Enter a choice: "))

        if user_input == 1:
            """
            If user input is 1, ask for the date of birth
            and display the horoscope
            """
            year = int(input('Enter your birth year, ex: 1994. \n'))
            month = int(input('Enter the month of birth, ex: 9.\n'))
            day = int(input('Enter your birth date, ex: 16.\n'))
            print(day, month, year)

        elif user_input == 2:

            # randomize list to show
            # 2 random upright cards and
            # 1 random reverse cards
            list_reverse_random = random.sample(list_reverse_taro, 2)
            list_upright_random = random.sample(list_upright_taro, 1)

            # combine reverse card list and upright card list
            list_taro_deck = list_reverse_random
            list_taro_deck.extend(list_upright_random)

            # randomize combined list
            list_taro_deck = random.sample(list_taro_deck, 3)

            # create headers for each card displayed
            # make it a set to remove duplicates
            set_taro_header_standard = {'~~ Draw 2 : The Present ~~',
                                        '~~ Draw 1 : The Past ~~',
                                        '~~ Draw 1 : The Past ~~',
                                        '~~ Draw 3 : The Future ~~'
                                        }
            # turn set header to a tuple and sort
            set_taro_header_standard = sorted(tuple(set_taro_header_standard))

            # turn final card deck to dictionary and back to list
            dic_taro_deck = {k: v for k, v in list_taro_deck}
            list_taro_deck = list(dic_taro_deck.items())

            # create header to display with tarot card reading
            print("\n\n\n\033[1;30;48m" +
                  "~~~~~ STANDARD TAROT READING ~~~~~"
                  + "\033[0;30;48m\n")

            # print out reading header, draw number, card and description
            for x, (k, v) in zip(set_taro_header_standard, list_taro_deck):
                print("\033[1;46;48m" + x + "\033[0;30;48m")
                print("\033[1;30;48m" + k + "\033[0;30;48m")
                print(v, "\n")

            # print out message to be displayed at the end of tarot
            # reading. This come from the EndingMessage Class
            msg = EndingMessage()
            print(msg.__str__())

        elif user_input == 3:
            """
            If user selects 3, display bye
            message and exit the program
            """
            print("BYE! Come back again soon!")
            break

        else:
            # If user enter an integer thats not 1, 2, or 3
            # The following message is displayed
            print(user_input, "is not a valid option, please try again.\n\n")

    except ValueError:
        """
        value error exception displays a message for all other
        non integer inputs entered.
        """
        # catches all other inputs enter str, float, etc
        print("ERROR: Please enter a valid option. "
              "Valid options are integers 1, 2, or 3\n\n")
