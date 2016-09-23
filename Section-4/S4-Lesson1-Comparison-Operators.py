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
    print(a + "Python Comparison Operators: " + Title)
    print("-------------------") 
    


####### OPERATORS IN PYTHON #######



############ BASICS ############

Lesson("Basic Comparisons")

## Comparison Operators: == | != | <> | > | < | >= | <= 
## Comparison Operators: Equals | Is not equal too | Is not equal to | Greater Than | Less Than | Greater than or equal to | Less than or equal to


print(1==1) ## Returns true because 1 does = 1
print(2==1) ## Returns false because 2 does not = 1
print("\n")

print(1!=1) ## Returns false because 1 does = 1
print(2!=1) ## Returns true because 2 does not = 1
print("\n")

print(1<>1) ## Returns false because 1 does = 1
print(2<>1) ## Returns true because 2 does not = 1
print("\n")

print(1>1)  ## Returns false because 1 is not greater than 1
print(2>1)  ## Returns true because 2 is greater than 1
print("\n")

print(1<1)  ## Returns false because 1 is not less than 1
print(2<1)  ## Returns false because 2 is not less than 1
print("\n")

print(1>=1) ## Returns true because 1 does = 1
print(2>=1) ## Returns true because 2 is greater than 1
print("\n")

print(1<=1) ## Returns true because 1 does = 1
print(2<=1) ## Returns false because 2 is not less than 1 or equal to 1
print("\n")



############ CHAINED ############

Lesson("Lesson 2 Name")

print(1 < 3)
print(3 > 1)
print(1 < 3 > 1) ## Used to check if both options are true
print(1 < 3 and 2 > 1) ## When the middle number isn't the same: True

print(1 > 10 or 5 > 3) ## 1 > 10 is false but since 5 > 3 it will print true because it's an or statement.


############ PRACTICE #############




Lesson("Age Restriction (challenge)")

########### EXERCISE 1 ############

##Create 3 variables; Name (String), Age (Integer), OldEnough (Boolean)
##Set the Name and Age to whatever you like
##Set the Boolean to check if Age is greater than or equal to 18
##Create a list adding the Name, Age, and OldEnough
##Finally add a print function that states:
##print('You can enter this site: ' + str(TableName[2]))



print("\n\n")