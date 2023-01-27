"""
This section import the following classes:
OpeningMessage, PandasToList and EndingMessage
The random module is also imported
"""
import random
from OpeningMessage import OpeningMessage
from EndingMessage import EndingMessage
from PandasToList import PandasToList
"""
As soon as the program runs a message is displayed.
The message comes from the OpeningMessage class.
"""
m = OpeningMessage()
m.__init__(filename='fortuneTelleingIntroduction.txt')
print(m.open_file())
m.open_file()

"""
The PandaToList is call to retrive a list for 
upright cards and another list for reverse cards.
"""
p = PandasToList()
list_reverse_taro = p.upright_deck("tarotCardsUpright.csv")
list_upright_taro = p.reverse_deck("tarotCardsReversed.csv")

while True:
    """
    User can enter an option to choose while True
    """
    try:
        """
        try block is added for exception handling
        """

        # promot user to enter an option
        user_input = int(input(
            "\033[1;46;48m" +
            "~~~~~ What type of Fortune reading would you like? ~~~~~" +
            "\033[0m\n"
            "Please, enter a number that correspondens "
            "to an available option.\n"
            "1: Monthly Horoscope\n"
            "2: Standart Major Arcana Spread\n"
            "3: Exit\n"
            "Enter a choice: "
        ))

        if user_input == 1:
            """
            If user input is 1, the date of birth is asked
            and after that the Horoscope will display
            """
            day = int(input("Enter your birth day, example: 16.\n"))
            month = input("Enter your month of birth, example: September.\n")
            month = month.capitalize()
            if month == 'December':
                if day < 22:
                    print("\033[0;35;47m" + "\n\n SAGITTARIUS\n" + "\033[0m")
                    print("Creativity is in the cards for you this month." +
                          "Ruling planet Jupiter lights up your" +
                          "Fun and Romance" +
                          "zone, which deals with procreation, recreation," +
                          "and artistic creation." +
                          "This Jupiter transit betokens a prolific," +
                          "pregnant mind." +
                          "But you also have the innovative" +
                          "Aquarius Sun in your Communication sector." +
                          "Double bonus." +
                          "These two transits complement" +
                          "each other well." +
                          "New ideas for expression" +
                          "(Aquarius in the 3rd House);" +
                          "expansiveness in creative output," +
                          "too (Jupiter in the 5th). Let us not forget," +
                          "too, that Aquarius is ruled by Saturn," +
                          "which can be a harsh editor. Let’s not forget," +
                          "either though, that we need this side of Saturn" +
                          "in our creative pursuits." +
                          "All great art is a wild animal tamed. Saturn’s" +
                          "presence with Aquarius should help structure" +
                          "and craft your Jupiterian excesses," +
                          "whether they take the form of poetry," +
                          "prose, grad school application," +
                          "article, online content," +
                          "or screenplay about" +
                          "bridesmaids behaving badly.")
                else:
                    print("\033[0;35;47m" + "\n\n CAPRICORN\n" + "\033[0m")
                    print("Your ruling planet is gearing up to change signs" +
                          "in early March, after a three year stint in your" +
                          "Money zone. This is the last month you will have" +
                          "Planet Taskmaster in this part of your chart for" +
                          "another three decades. Heavy. On a side note," +
                          "but also relatedly: it’s interesting that," +
                          "in general, mortgages are the length of" +
                          "a Saturn return (30 years). With that in mind," +
                          "Saturn in your Money sector is about long term" +
                          "financial planning–where do you want to be when" +
                          "Saturn comes back here again? Other signs" +
                          "(like Cancer) might blanch at such a prospect" +
                          "of thinking ahead this far, but with such clear" +
                          "astrology around finances this month," +
                          "rise to the occasion, Goat, and make the Cosmos" +
                          "smile. Ask yourself if you’ve reached" +
                          "a financial goalsince 2020" +
                          "(when Saturn ingresses)?" +
                          "And then look ahead 30 years." +
                          "How does maxing out" +
                          "on a yacht, playing backgammon" +
                          "with friends sound?" +
                          "Or what about being a homeowner with" +
                          "a trim hearth" +
                          "and an extravagant garden?" +
                          "Have fun with these thoughts, but set them down" +
                          "to paper nonetheless. Saturn loves documentation.")
            elif month == 'January':
                if day < 20:
                    print("\033[0;35;47m" + "\n\n CAPRICORN\n" + "\033[0m")
                    print("Your ruling planet is gearing up to change signs" +
                          "in early March, after a three year stint in your" +
                          "Money zone. This is the last month you will have" +
                          "Planet Taskmaster in this part of your chart for" +
                          "another three decades. Heavy. On a side note," +
                          "but also relatedly: it’s interesting that," +
                          "in general, mortgages are the length of" +
                          "a Saturn return (30 years). With that in mind," +
                          "Saturn in your Money sector is about long term" +
                          "financial planning–where do you want to be when" +
                          "Saturn comes back here again? Other signs" +
                          "(like Cancer) might blanch at such a prospect" +
                          "of thinking ahead this far, but with such clear" +
                          "astrology around finances this month," +
                          "rise to the occasion, Goat, and make the Cosmos" +
                          "smile. Ask yourself if you’ve reached" +
                          "a financial goalsince 2020" +
                          "(when Saturn ingresses)?" +
                          "And then look ahead 30 years." +
                          "How does maxing out" +
                          "on a yacht, playing backgammon" +
                          "with friends sound?" +
                          "Or what about being a homeowner with" +
                          "a trim hearth" +
                          "and an extravagant garden?" +
                          "Have fun with these thoughts, but set them down" +
                          "to paper nonetheless. Saturn loves documentation.")
                else:
                    print("\033[0;35;47m" + "\n\n AQUARIUS\n" + "\033[0m")
                    print("It’s your season until the 18th," +
                          "as the Sun lights up your Selfhood sector." +
                          "But let’s slow our roll a bit. The Sun-God" +
                          "will be sharing this part of the chart with" +
                          "your ruler, grim Saturn, which has been camped" +
                          "out there since March 2020. This is finally the" +
                          "last month of a gruelling three year Saturn" +
                          "transit which won’t be making this" +
                          "aspect for 30 years (that’s" +
                          " cause for celebration)." +
                          "But before your graduation party, please take" +
                          "notethat Saturn is the Schoolmaster" +
                          "and it’s time to review the past"
                          "few years for this transit’s final" +
                          "exam. How have you progressed" +
                          "in your self-study since" +
                          "that seemingly forever Saturnal" +
                          "ingress to your sign?" +
                          "That’s the kind of essay question" +
                          "you should prepare" +
                          "to answer. In the end, honour Saturn" +
                          "(despite its hard-nosed tactics)" +
                          "by making sure" +
                          "you keep the commitments you’ve" +
                          "made to yourself," +
                          "so you continue to grow even after your ruler has" +
                          "left the Waterbarer on March 7th. A Full Moon" +
                          "in your Relationship sector on February 5th/6th" +
                          "portends a perfect night to take a break from" +
                          "Saturn studies and be out with a friend," +
                          "helpmate, or business partner.")
            elif month == 'February':
                if day < 19:
                    print("\033[0;35;47m" + "\n\n AQUARIUS\n" + "\033[0m")
                    print("It’s your season until the 18th,\
                        as the Sun lights up your Selfhood sector.\
                        But let’s slow our roll a bit. The Sun-God\
                        will be sharing this part of the chart with\
                        your ruler, grim Saturn, which has been camped\
                        out there since March 2020. This is finally the\
                        last month of a gruelling three year Saturn transit\
                        which won’t be making this aspect for 30 years\
                        (that’s cause for celebration).\
                        But before your graduation party, please take note\
                        that Saturn is the Schoolmaster and it’s time to\
                        review the past few years for this transit’s final\
                        exam. How have you progressed in your self-study since\
                        that seemingly forever Saturnal ingress to your sign?\
                        That’s the kind of essay question you should prepare\
                        to answer. In the end, honour Saturn\
                        (despite its hard-nosed tactics) by making sure\
                        you keep the commitments you’ve made to yourself,\
                        so you continue to grow even after your ruler has left\
                        the Waterbarer on March 7th. A Full Moon\
                        in your Relationship sector on February 5th/6th\
                        portends a perfect night to take a break from\
                        Saturn studies and be out with a friend,\
                        helpmate, or business partner.")
                else:
                    print("\033[0;35;47m" + "\n\n PISCES\n" + "\033[0m")
                    print("Ritzy Venus sparkles hard in your\
                        sign until Feb 20th. It’s “exalted” here,\
                        so love and romance are in the air for you,\
                        especially on the 15th, when Planet Love\
                        goes conjunct your co-ruler, dreamy Neptune.\
                        As always with Neptune in the picture,\
                        however, one must be aware of falling\
                        too hard or too fast for a frog who plays\
                        the prince. Indeed, Neptune stands for\
                        glamour and magical artistry, but also\
                        misplaced fantasy and delusion.\
                        Those caveats aside, this conjunction\
                        is a peak day for romantic interludes.\
                        Your other ruling planet, exuberant Jupiter,\
                        transits your Money zone all month,\
                        which bodes well for finances and making\
                        extra cash. At the moment,\
                        Planet Luck is all fired up in cardinal Aries,\
                        so take advantage of this go-getter energy.\
                        It’s not a time to sit on the fence.\
                        Instead, consider a savvy investment or purchase.\
                        Jupiter is a planet known for granting\
                        unexpected windfalls, but with initiatory Aries\
                        involved, you might need to take a few steps\
                        toward Jupiter before it takes many toward you.")
            elif month == 'March':
                if day < 21:
                    print("\033[0;35;47m" + "\n\n PISCES\n" + "\033[0m")
                    print("Ritzy Venus sparkles hard in your\
                        sign until Feb 20th. It’s “exalted” here,\
                        so love and romance are in the air for you,\
                        especially on the 15th, when Planet Love\
                        goes conjunct your co-ruler, dreamy Neptune.\
                        As always with Neptune in the picture,\
                        however, one must be aware of falling\
                        too hard or too fast for a frog who plays\
                        the prince. Indeed, Neptune stands for\
                        glamour and magical artistry, but also\
                        misplaced fantasy and delusion.\
                        Those caveats aside, this conjunction\
                        is a peak day for romantic interludes.\
                        Your other ruling planet, exuberant Jupiter,\
                        transits your Money zone all month,\
                        which bodes well for finances and making\
                        extra cash. At the moment,\
                        Planet Luck is all fired up in cardinal Aries,\
                        so take advantage of this go-getter energy.\
                        It’s not a time to sit on the fence.\
                        Instead, consider a savvy investment or purchase.\
                        Jupiter is a planet known for granting\
                        unexpected windfalls, but with initiatory Aries\
                        involved, you might need to take a few steps\
                        toward Jupiter before it takes many toward you.")
                else:
                    print("\033[0;35;47m" + "\n\n ARIES\n" + "\033[0m")
                    print("Full steam ahead, Ram. After a long retrograde,\
                        your ruling planet, steroidal Mars,\
                        is direct and gaining speed in your\
                        Communication zone. Additionally, expansive Jupiter\
                        transits your sign all month.\
                        With all this forward motion, it’s time\
                        to express yourself. Jupiter will help give\
                        volume and Mars energy to your words, so turn\
                        attention to a looming project and get to work.\
                        The shadow side to Mars+Jupiter, especially in\
                        relation to the Communication zone of one’s chart,\
                        could be broadcasting aggression through speech,\
                        but the fact that these two planets form a\
                        harmonious “sextile” with each other ultimately\
                        betokens words from you being heard without\
                        the taint of disputation. On the 20th,\
                        Venus moves into your sign. With Jupiter\
                        transiting there, too, you have both Benefics\
                        pumping up your Ego zone. You already flex that\
                        bicep without these planets, so by month’s end you\
                        should be brimming with confidence, appeal, and luck.\
                        Schedule a meeting with a supervisor to talk about\
                        shouldering more responsibility at work, with an eye\
                        toward promotion and recognition.")
            elif month == 'April':
                if day < 20:
                    print("\033[0;35;47m" + "\n\n ARIES\n" + "\033[0m")
                    print("Full steam ahead, Ram. After a long retrograde,\
                        your ruling planet, steroidal Mars,\
                        is direct and gaining speed in your\
                        Communication zone. Additionally, expansive Jupiter\
                        transits your sign all month.\
                        With all this forward motion, it’s time\
                        to express yourself. Jupiter will help give\
                        volume and Mars energy to your words, so turn\
                        attention to a looming project and get to work.\
                        The shadow side to Mars+Jupiter, especially in\
                        relation to the Communication zone of one’s chart,\
                        could be broadcasting aggression through speech,\
                        but the fact that these two planets form a\
                        harmonious “sextile” with each other ultimately\
                        betokens words from you being heard without\
                        the taint of disputation. On the 20th,\
                        Venus moves into your sign. With Jupiter\
                        transiting there, too, you have both Benefics\
                        pumping up your Ego zone. You already flex that\
                        bicep without these planets, so by month’s end you\
                        should be brimming with confidence, appeal, and luck.\
                        Schedule a meeting with a supervisor to talk about\
                        shouldering more responsibility at work, with an eye\
                        toward promotion and recognition.")
                else:
                    print("\033[0;35;47m" + "\n\n TAURUS\n" + "\033[0m")
                    print("Venus, your ruling planet, jets through two\
                        signs this month, namely watery Pisces\
                        (very strong position) and aggro Aries\
                        (not so strong). How might this inform\
                        your month? Venus-in-Pisces highlights\
                        your Friendship zone until February 20th,\
                        indicating a fantastic transit for\
                        socialising and connecting in a heartfelt way\
                        with those who sustain your sense of belonging\
                        in this rough-hewn world or ours.\
                        But let’s not stop there, for it’s also a\
                        wonderful placement to meet new people through\
                        your friends–a suitor, a potential employer,\
                        or an amazing employee.\
                        Venus then moves into Aries, where Planet Love\
                        gets a bit more uncouth due to the Mars-ruled\
                        nature of the Ram. Here love can become more war\
                        torn–fighting, acting out, provoking.\
                        Given all this, it might make some sense,\
                        toward the end of the month, to get a bit\
                        introspective. Indeed, when the Sun joins\
                        Venus in your zone of the Unconscious zone\
                        around the 20th, the advice points to spending\
                        evenings at home reading and healing.\
                        Transits through one’s Unconscious zone indicate\
                        a time for convalescence to heal\
                        existential wounds.")
            elif month == 'May':
                if day < 21:
                    print("\033[0;35;47m" + "\n\n TAURUS\n" + "\033[0m")
                    print("Venus, your ruling planet, jets through two\
                        signs this month, namely watery Pisces\
                        (very strong position) and aggro Aries\
                        (not so strong). How might this inform\
                        your month? Venus-in-Pisces highlights\
                        your Friendship zone until February 20th,\
                        indicating a fantastic transit for\
                        socialising and connecting in a heartfelt way\
                        with those who sustain your sense of belonging\
                        in this rough-hewn world or ours.\
                        But let’s not stop there, for it’s also a\
                        wonderful placement to meet new people through\
                        your friends–a suitor, a potential employer,\
                        or an amazing employee.\
                        Venus then moves into Aries, where Planet Love\
                        gets a bit more uncouth due to the Mars-ruled\
                        nature of the Ram. Here love can become more war\
                        torn–fighting, acting out, provoking.\
                        Given all this, it might make some sense,\
                        toward the end of the month, to get a bit\
                        introspective. Indeed, when the Sun joins\
                        Venus in your zone of the Unconscious zone\
                        around the 20th, the advice points to spending\
                        evenings at home reading and healing.\
                        Transits through one’s Unconscious zone indicate\
                        a time for convalescence to heal\
                        existential wounds.")
                else:
                    print("\033[0;35;47m" + "\n\n GEMINI\n" + "\033[0m")
                    print("Ooof. Last month you had your ruling planet,\
                        Mercury, going retrograde in Capricorn,\
                        while aggressive Mars was also reversing\
                        in your sign (double trouble). The world\
                        could very well have felt sluggish for you:\
                        waiting, anticipating, pacing.\
                        But now Mars and Mercury are moving direct.\
                        Take your cue from these two planets and start\
                        being more direct, as well. Say what you want;\
                        mean what you say. Mars in your sign can cause\
                        you to come across as gruff in the eyes of others,\
                        but after the retrogrades of yester-month,\
                        it’s better to be productive, if a bit pushy,\
                        instead of performing a kind of pro forma politesse\
                        in professional and personal contexts.\
                        For all its faults, Mars lends us courage,\
                        so step forward with confidence online or at work\
                        to get what you need and want. Work, in particular,\
                        is looking strong for you over the next few weeks,\
                        as Venus-in-Pisces transits your Career zone\
                         until the 20th.\
                        Combine Mars bravado with Venusian charm\
                        to shine at the 9 to 5.")
            elif month == 'June':
                if day < 21:
                    print("\033[0;35;47m" + "\n\n GEMINI\n" + "\033[0m")
                    print("Ooof. Last month you had your ruling planet,\
                        Mercury, going retrograde in Capricorn,\
                        while aggressive Mars was also reversing\
                        in your sign (double trouble). The world\
                        could very well have felt sluggish for you:\
                        waiting, anticipating, pacing.\
                        But now Mars and Mercury are moving direct.\
                        Take your cue from these two planets and start\
                        being more direct, as well. Say what you want;\
                        mean what you say. Mars in your sign can cause\
                        you to come across as gruff in the eyes of others,\
                        but after the retrogrades of yester-month,\
                        it’s better to be productive, if a bit pushy,\
                        instead of performing a kind of pro forma politesse\
                        in professional and personal contexts.\
                        For all its faults, Mars lends us courage,\
                        so step forward with confidence online or at work\
                        to get what you need and want. Work, in particular,\
                        is looking strong for you over the next few weeks,\
                        as Venus-in-Pisces transits your Career zone\
                        until the 20th.\
                        Combine Mars bravado with Venusian charm\
                        to shine at the 9 to 5.")
                else:
                    print("\033[0;35;47m" + "\n\n CANCER\n" + "\033[0m")
                    print("Until the 18th, your Intimacy zone is\
                        highlighted by the independent Aquarius Sun,\
                        which needs its space, and, which, therefore,\
                        seems at loggerheads with the proximity and\
                        closeness implied by the section of the chart\
                        it’s transiting. But sometimes distance from\
                        intimate relations can help us see more clearly.\
                        It could be that the somewhat cold Aquarius Sun\
                        is shining its interrogation light on a part of\
                        your chart to ask questions about whether you\
                        need to relax that grasping Cancer claw, so that\
                        you and a beloved can relax a bit. But another\
                        way to look at this transit: the Aquarius Sun\
                        has an intellectual glint to it, meaning you\
                        might be drawn to a sapiosexual kink over the\
                        next few weeks–-reading Sade by candlelight\
                        in the tub, perhaps. On February 5th, your\
                        ruling planet, the Moon, lights up your Money\
                        zone. You might want to spend on flashy objects,\
                        as this lunation occurs in showy Leo. On February\
                        20th, the New Moon in Pisces activates your house\
                        of Spirituality and Learning. Sign-up for a class\
                        at Yogananda’s Self-Realisation Fellowship to get\
                        deeper into the architecture of enlightenment.")
            elif month == 'July':
                if day < 23:
                    print("\033[0;35;47m" + "\n\n CANCER\n" + "\033[0m")
                    print("Until the 18th, your Intimacy zone is\
                        highlighted by the independent Aquarius Sun,\
                        which needs its space, and, which, therefore,\
                        seems at loggerheads with the proximity and\
                        closeness implied by the section of the chart\
                        it’s transiting. But sometimes distance from\
                        intimate relations can help us see more clearly.\
                        It could be that the somewhat cold Aquarius Sun\
                        is shining its interrogation light on a part of\
                        your chart to ask questions about whether you\
                        need to relax that grasping Cancer claw, so that\
                        you and a beloved can relax a bit. But another\
                        way to look at this transit: the Aquarius Sun\
                        has an intellectual glint to it, meaning you\
                        might be drawn to a sapiosexual kink over the\
                        next few weeks–-reading Sade by candlelight\
                        in the tub, perhaps. On February 5th, your\
                        ruling planet, the Moon, lights up your Money\
                        zone. You might want to spend on flashy objects,\
                        as this lunation occurs in showy Leo. On February\
                        20th, the New Moon in Pisces activates your house\
                        of Spirituality and Learning. Sign-up for a class\
                        at Yogananda’s Self-Realisation Fellowship to get\
                        deeper into the architecture of enlightenment.")
                else:
                    print("\033[0;35;47m" + "\n\n LEO\n" + "\033[0m")
                    print("Your ruling planet, the Sun, is currently\
                        in Aquarius, the aloof Waterbearer. Let’s be\
                        honest: this isn’t your favourite solar placement.\
                        Some like it hot–like you–but Aquarius is saturnal\
                        and cold. You like attention, but Aquarius has a\
                        kind of impersonal energy. And finally, where you\
                        can be ego-centic (it happens), this Aquarius Sun\
                        highlights your Relationship zone, that is, the\
                        House of the Other. This is not a month of\
                        self-indulgence or showy protestation.\
                        Think instead about being present for a beloved\
                        or business partner. Why? Saturn, the Schoolmaster,\
                        will be leaving Aquarius next month.\
                        That means, you’re ending a very intense three-year\
                        transit where Saturn has been opposing your\
                        Selfhood zone. Other than the Waterbearer,\
                        no sign has been under more duress due to Saturn’s\
                        placement than you. Naturally,\
                        Planet Schoolmaster teaches lessons.\
                        Its presence in your Relationship zone has been\
                        trying to instruct you on the importance of being\
                        serious about love with another rather than\
                        merely sweet on yourself. You have one month\
                        more to show that you’ve studied for Saturn’s\
                        examination. Look back to 2020 and relationships\
                        in your life. Take stock. Like Ebenezer Scrooge\
                        in “Christmas Carol,” it’s not\
                        too late to change.")
            elif month == 'August':
                if day < 23:
                    print("\033[0;35;47m" + "\n\n LEO\n" + "\033[0m")
                    print("Your ruling planet, the Sun, is currently\
                        in Aquarius, the aloof Waterbearer. Let’s be\
                        honest: this isn’t your favourite solar placement.\
                        Some like it hot–like you–but Aquarius is saturnal\
                        and cold. You like attention, but Aquarius has a\
                        kind of impersonal energy. And finally, where you\
                        can be ego-centic (it happens), this Aquarius Sun\
                        highlights your Relationship zone, that is, the\
                        House of the Other. This is not a month of\
                        self-indulgence or showy protestation.\
                        Think instead about being present for a beloved\
                        or business partner. Why? Saturn, the Schoolmaster,\
                        will be leaving Aquarius next month.\
                        That means, you’re ending a very intense three-year\
                        transit where Saturn has been opposing your\
                        Selfhood zone. Other than the Waterbearer,\
                        no sign has been under more duress due to Saturn’s\
                        placement than you. Naturally,\
                        Planet Schoolmaster teaches lessons.\
                        Its presence in your Relationship zone has been\
                        trying to instruct you on the importance of being\
                        serious about love with another rather than\
                        merely sweet on yourself. You have one month\
                        more to show that you’ve studied for Saturn’s\
                        examination. Look back to 2020 and relationships\
                        in your life. Take stock. Like Ebenezer Scrooge\
                        in “Christmas Carol,” it’s not\
                        too late to change.")
                else:
                    print("\033[0;35;47m" + "\n\n VIRGO\n" + "\033[0m")
                    print("Speedster Mercury, your ruler, was embattled\
                        last month in a retrograde, but now it’s moving\
                        with intention through your Fun and Romance\
                        zone until the middle of February. In addition\
                        to hijinks, this part of the chart teals with\
                        creativity, artistry, and fertility. In other\
                        words, the birthing of ideas. You’re a\
                        straightforward problem-solver by nature,\
                        but sometimes answers and ideas to questions\
                        can come from a sense of play, fun, ambiguity,\
                        or the counterintuitive domains of the mind where\
                        illogical elements hold sway. Pay due respect to\
                        the Fun zone of your chart, and Mercury’s place in it,\
                        by being a bit more loose in the way you approach\
                        your day, your routine, where you find inspiration.\
                        By the middle of February, things get more buttoned\
                        up, with Mercury heading into your zone of Routine,\
                        Diet, and Health.\
                        Most signs view this part of the chart\
                        as a slog, but Virgo rules over the 6th\
                        House of Routine.\
                        With Mercury transiting there, expect a bonanza\
                        of appointments made and efficiently met.\
                        In other words, music to your Virgo ears.")
            elif month == 'September':
                if day < 23:
                    print("\033[0;35;47m" + "\n\n VIRGO\n" + "\033[0m")
                    print("Speedster Mercury, your ruler, was embattled\
                        last month in a retrograde, but now it’s moving\
                        with intention through your Fun and Romance\
                        zone until the middle of February. In addition\
                        to hijinks, this part of the chart teals with\
                        creativity, artistry, and fertility. In other\
                        words, the birthing of ideas. You’re a\
                        straightforward problem-solver by nature,\
                        but sometimes answers and ideas to questions\
                        can come from a sense of play, fun, ambiguity,\
                        or the counterintuitive domains of the mind where\
                        illogical elements hold sway. Pay due respect to\
                        the Fun zone of your chart, and Mercury’s place in it,\
                        by being a bit more loose in the way you approach\
                        your day, your routine, where you find inspiration.\
                        By the middle of February, things get more buttoned\
                        up, with Mercury heading into your zone of Routine,\
                        Diet, and Health.\
                        Most signs view this part of the chart\
                        as a slog, but Virgo rules over the 6th\
                        House of Routine.\
                        With Mercury transiting there, expect a bonanza\
                        of appointments made and efficiently met.\
                        In other words, music to your Virgo ears.")
                else:
                    print("\033[0;35;47m" + "\n\n LIBRA\n" + "\033[0m")
                    print("While others get a mere Valentine’s Day,\
                        you should think of February more as\
                        Valentine’s Month. So many romantic\
                        transits for Libra. To wit: your ruling planet,\
                        Venus, flits through Pisces, where it’s exalted,\
                        until the 20th. Pisces+Venus is about merging\
                        souls, energies, bodies, and minds. This mystical\
                        fusion energy suggests a time to be compassionate,\
                        heart-felt, caring, and loving toward family,\
                        friends, crushes, or helpmates. No holding back.\
                        No balancing and measuring words and emotions,\
                        as can sometimes be your wont. No, tip the scales\
                        toward love and excess. Such romantic feelings\
                        should come extra easily, given that you also\
                        have expansive Jupiter in your Relationship\
                        zone all month–a placement that will enlarge\
                        the heart and Venus-in-Pisces themes.\
                        Finally, Venus joins Jupiter in your\
                        Relationship sector on the 20th.\
                        Both Benefics there augur love overload\
                        (in a good way; there are no dark valances\
                        to any of these transits). Remember that\
                        Jupiter brings luck. Feeling happier with\
                        a help-mate or meeting someone new\
                        (if you’re uncoupled) are both indications\
                        of this very strong transit.")
            elif month == 'October':
                if day < 23:
                    print("\033[0;35;47m" + "\n\n LIBRA\n" + "\033[0m")
                    print("While others get a mere Valentine’s Day,\
                        you should think of February more as\
                        Valentine’s Month. So many romantic\
                        transits for Libra. To wit: your ruling planet,\
                        Venus, flits through Pisces, where it’s exalted,\
                        until the 20th. Pisces+Venus is about merging\
                        souls, energies, bodies, and minds. This mystical\
                        fusion energy suggests a time to be compassionate,\
                        heart-felt, caring, and loving toward family,\
                        friends, crushes, or helpmates. No holding back.\
                        No balancing and measuring words and emotions,\
                        as can sometimes be your wont. No, tip the scales\
                        toward love and excess. Such romantic feelings\
                        should come extra easily, given that you also\
                        have expansive Jupiter in your Relationship\
                        zone all month–a placement that will enlarge\
                        the heart and Venus-in-Pisces themes.\
                        Finally, Venus joins Jupiter in your\
                        Relationship sector on the 20th.\
                        Both Benefics there augur love overload\
                        (in a good way; there are no dark valances\
                        to any of these transits). Remember that\
                        Jupiter brings luck. Feeling happier with\
                        a help-mate or meeting someone new\
                        (if you’re uncoupled) are both indications\
                        of this very strong transit.")
                else:
                    print("\033[0;35;47m" + "\n\n SCORPIO\n" + "\033[0m")
                    print("Your ruling planet, libidinous Mars,\
                        has been all frustrated with a prolonged\
                        retrograde, but that changes this February,\
                        as it moves direct in your witchy and erotic\
                        Intimacy zone. Chart-wise, this is one of the\
                        best placements for Mars in relation to your\
                        own smouldering nature. Expect heightened libido,\
                        sexual curiosity, and desire. Lingerie days.\
                        Such enticements are intensified by the fact\
                        that you also have Venus in your Fun zone,\
                        at the same time Mars struts in the 8th House.\
                        Venus has its “joy” in this part of the chart.\
                        It wants to flirt and get creative.\
                        So, you have a doubly nice set of aspecting\
                        planets suggesting playtime. And, if we may add\
                        one more layer to all this, let’s be aware of\
                        the Pisces Sun moving into your Fun zone on\
                        the 18th for the remainder of the month.\
                        Pisces is about dreamy excess. In your\
                        Fun zone, which also deals with romance,\
                        this solar placement augurs getting swept\
                        up in big feelings for someone.\
                        It’s time to get out and about amid\
                        the night life, if only to return to the\
                        boudoir later on in the evening\
                        with mischievous notions.")
            elif month == 'November':
                if day < 22:
                    print("\033[0;35;47m" + "\n\n SCORPIO\n" + "\033[0m")
                    print("Your ruling planet, libidinous Mars,\
                        has been all frustrated with a prolonged\
                        retrograde, but that changes this February,\
                        as it moves direct in your witchy and erotic\
                        Intimacy zone. Chart-wise, this is one of the\
                        best placements for Mars in relation to your\
                        own smouldering nature. Expect heightened libido,\
                        sexual curiosity, and desire. Lingerie days.\
                        Such enticements are intensified by the fact\
                        that you also have Venus in your Fun zone,\
                        at the same time Mars struts in the 8th House.\
                        Venus has its “joy” in this part of the chart.\
                        It wants to flirt and get creative.\
                        So, you have a doubly nice set of aspecting\
                        planets suggesting playtime. And, if we may add\
                        one more layer to all this, let’s be aware of\
                        the Pisces Sun moving into your Fun zone on\
                        the 18th for the remainder of the month.\
                        Pisces is about dreamy excess. In your\
                        Fun zone, which also deals with romance,\
                        this solar placement augurs getting swept\
                        up in big feelings for someone.\
                        It’s time to get out and about amid\
                        the night life, if only to return to the\
                        boudoir later on in the evening\
                        with mischievous notions.")
                else:
                    print("\033[0;35;47m" + "\n\n SAGITTARIUS\n" + "\033[0m")
                    print("Creativity is in the cards for you this month." +
                          "Ruling planet Jupiter lights up your" +
                          "Fun and Romance" +
                          "zone, which deals with procreation, recreation," +
                          "and artistic creation." +
                          "This Jupiter transit betokens a prolific," +
                          "pregnant mind." +
                          "But you also have the innovative" +
                          "Aquarius Sun in your Communication sector." +
                          "Double bonus." +
                          "These two transits complement" +
                          "each other well." +
                          "New ideas for expression" +
                          "(Aquarius in the 3rd House);" +
                          "expansiveness in creative output," +
                          "too (Jupiter in the 5th). Let us not forget," +
                          "too, that Aquarius is ruled by Saturn," +
                          "which can be a harsh editor. Let’s not forget," +
                          "either though, that we need this side of Saturn" +
                          "in our creative pursuits." +
                          "All great art is a wild animal tamed. Saturn’s" +
                          "presence with Aquarius should help structure" +
                          "and craft your Jupiterian excesses," +
                          "whether they take the form of poetry," +
                          "prose, grad school application," +
                          "article, online content," +
                          "or screenplay about" +
                          "bridesmaids behaving badly.") 
            else:
                # If user enter a different input then string
                # The following message is displayed
                print(month, "is not a valid option, please try again.\n\n")
                
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
            # make it a set to remove duplication
            set_taro_header_standard = {
                "~~ Draw 2 : The Present ~~",
                "~~ Draw 1 : The Past ~~",
                "~~ Draw 1 : The Past ~~",
                "~~ Draw 3 : The Future ~~",
            }
            # turn set header to a truple and sort
            set_taro_header_standard = sorted(tuple(set_taro_header_standard))

            # turn final card deck to dictionary and back to list
            dic_taro_deck = {k: v for k, v in list_taro_deck}
            list_taro_deck = list(dic_taro_deck.items())

            # create header to display with tarot card reading
            print(
                "\n\n\n\033[1;32;40m" 
                + "~~~~~ STANDARD TAROT READING ~~~~~"
                + "\033[0;30;48m\n"
            )

            # print out reading header, draw number, card and description
            for x, (k, v) in zip(set_taro_header_standard, list_taro_deck):
                print("\033[1;46;48m" + x + "\033[0m")
                print("\033[0;35;47m" + k + "\033[0m")
                print(v, "\n")

            # print out message to be displayed at the end of tarot
            # reading. The message comes from the EndingMessage Class
            msg = EndingMessage()
            print(msg.__str__())

        elif user_input == 3:
            """
            If user enter 3, display Bye message
            and exit the program
            """
            print("BYE! Come back again soon!")
            break
        else:
            # If user enter a different intiger then 1,2 or 3
            # The following message is displayed
            print(user_input, "is not a valid option, please try again.\n\n")

    except ValueError:
        """
        Value Error exception displays a message for all other
        non intiger inputs entered. 
        """
        # catches all other inputs enter: str, float, etc
        print(
            "ERROR: Please enter a valid option"
            "Valoid options are intigers 1, 2 or 3\n\n"
        )