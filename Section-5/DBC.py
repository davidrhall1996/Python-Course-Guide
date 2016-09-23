from itertools import izip

file1 = open("DataBaseCreation.py", 'w') ##I want to create a new file that will serve as my database to hold a bunch of names and phone numbers.

file1.write("DataBase = [\n") ## I want to create the start of the list as the output should be;
##We keep the Database outside the for loop because we only want 1 MAIN List that holds the others. via the example below.
##Stage 1 we have:
"""
Database = [ 
    
"""

## we open a txt file with a list of names and the other as a list of phonenumbers
with open("names.txt", 'r') as names, open("phonenumbers.txt", 'r') as phones: ## MUST BE OPENED AT THE SAME TIME
    for NameLine, PhoneLine in izip(names, phones): ##There is a tool called izip which helps us read line by line of a txt document
        Namefix = NameLine[:-1]##If we read the line it will read "FirstName LastName\n" We need to take out the "\n" so we can have: " ['Name', 'Phone'],\n"
        Phonefix = PhoneLine[:-1] ##without the [:-1] it will write ['Name\n'] creating lots of syntax errors :-( we don't like those.
        file1.write("\t['%s', " %(Namefix)) ##We write the name to the database: \t['Name1', 
        file1.write("'%s'],\n" %(Phonefix)) ##finish the loop off with the phone number and next line:  'Phone1'],\n 

##Stage 2 we have:
"""
Database = [ 
    ['Name1', 'Phone1'],
    ['Name2', 'Phone2'],
    ['Name3', 'Phone3'],
    ['Name4', 'Phone4'],
    etc...to 3000,
"""

        
file1.write("]") ## We can't forget to close the MAIN LIST
file1.close() ## Close the file because we're done writing

##Stage 3 we have:
"""
Database = [ 
    ['Name1', 'Phone1'],
    ['Name2', 'Phone2'],
    ['Name3', 'Phone3'],
    ['Name4', 'Phone4'],
    etc...for all 3000,
]
"""

from DataBaseCreation import * ## This is very important this allows us to get the 3002 lines of code we created without having 3002 lines of our script because that would be very annoying to scroll through. :/

##You can import custom files by doing: from FileName import *
##import * import's everything, however you could just give a specific variable name.





##Final Code without comments clean cut
"""
from itertools import izip

file1 = open("DataBaseCreation.py", 'w')

file1.write("DataBase = [\n")


with open("names.txt", 'r') as names, open("phonenumbers.txt", 'r') as phones: 
    for NameLine, PhoneLine in izip(names, phones):
        Namefix = NameLine[:-1]
        Phonefix = PhoneLine[:-1] 
        file1.write("\t['%s', " %(Namefix))
        file1.write("'%s'],\n" %(Phonefix))

        
file1.write("]") 
file1.close()

from DataBaseCreation import *

"""