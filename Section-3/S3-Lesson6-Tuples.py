##################################
##     Pyton Sections 3 & 4     ##
##           Examples           ##
##         By David Hall        ##
##                              ##
##            Numbers           ##
##                              ##
##            Strings           ##
##                              ##
##            Printing          ##            
##                              ##                             
##             Lists            ##
##                              ##
##          Dictionaries        ##
##                              ##
##             Tuples           ##
##                              ##
##              Sets            ##
##                              ##
##             Booleans         ##
##                              ##    
##       Comparison Operators   ##
##################################

import math
def Lesson(Title):
    a = "\n" * 3 ## Distance controller adjust for more or less spacing; 
    print(a + "Python Tuples: " + Title)
    print("-------------------")
    


####### PRINTING IN PYTHON #######



############# BASICS #############

Lesson("Basics") 

t = (1,1,2,2) ## Tuples are non-changeable and used to store data we want permenant like days of the week.


print(t[0]) # Can be accesses like lists. Output will be 1

##t[0] = 2  In lists you can change the value of something. However, if we try this operation we get an error because Tuples CAN NOT BE CHANGED!
##print(t[0]) Will return error: 'tuple' object does not support item assignment





############ Info ############

Lesson("Information")

t = (1,1,1,2,'test')


print(len(t)) ## This will give us 5 because there are 5 items in the tuple
print(t.count(1)) ## We can find how many of a certain item is in a tuple. This will return 3 because 1 is in there three times.
print(t.index('test')) ## This will return the position of the item in (). The output is 4 so we know t[4] = 'test'





############ PRACTICE #############




Lesson("Calendar (challenge)") ## it's recommended you leave the (challenge) so students know it's an exercise

########### EXERCISE 1 ############

## Find and add the missing months to the tuple
## Use the length operation to verify there are 12 months
## Index each of the missing months and print their values

t = ('January', 'Febuary', 'March', 'May', 'June', 'July', 'September', 'November', 'December')



print("\n\n")