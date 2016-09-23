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
    print(a + "Python Sets and Booleans: " + Title)
    print("-------------------")
    


####### PRINTING IN PYTHON #######



############ BASICS ############

Lesson("Set Basics")

MySet = set() ##Sets are used to organize data and are unique
MySet.add(1) ## This will add 1 to the set
MySet.add(2)


print(MySet)





############ Occurances ############

Lesson("Set Occurances")

MyList = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6] #We want to know how many DIFFERENT items there are
MySet = set(MyList)


print(MySet) ## Notice only 1,2,3,4,5,6 are printed. Sets don't count reoccurances





############ BOOLEANS ############

Lesson("Booleans")

a = True ## Booleans are used for things like program switches. If switch == true (it is on) then do this other line of code.
b = False
c = 1>5 ## This creates a boolean. Booleans are also used for debugging and validating information. 1 is not greater than 5 so it will return false.


print(a) ## Returns True
print(b) ## Returns False
print(c) 



############ PRACTICE #############




Lesson("Exercise Name Here (challenge)") ## it's recommended you leave the (challenge) so students know it's an exercise

########### EXERCISE 1 ############
## Create a two sets and add your own variables
## using the length operation create a variable that compares the two sets using a < or > 
## print that variable to if it returns true or false and know which set is larger.




print("\n\n")