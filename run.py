"""
This section import the following classes:
OpeningMessage and EndingMessage
The random module is also imported
"""
from OpeningMessage import OpeningMessage
"""
As soon as the program runs a message is displayed.
This message comes from the OpeningMessage class
as shown below.
"""
m = OpeningMessage()
m.__init__(filename='fortuneTelleingIntroduction.txt')
print(m.open_file())
m.open_file()