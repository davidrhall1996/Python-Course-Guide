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
    print(a + "Python Lists: " + Title)
    print("-------------------")
    


######### LISTS IN PYTHON #########



############ EXAMPLE 1 ############

Lesson("Basics")

MyList = ['david',20,1996] ## Lists can store multiple information Rather than writing three variables we can store it in a list


print(MyList) ## prints contents of list
print(len(MyList)) ## prints length of list: 3
print(MyList[0]) ## prints whatever is in the first position: REMEMBER len is 3 but positions start at 0 e.g. 0, 1 ,2 for 'david', 20, 1996


####### LIST IDENTIFICATION #######

Lesson("List Identification")

MyList = ['david',20,1996]


print(MyList) ## Normal Print
print(MyList[1:]) ## starts at position 1 like in strings. Output: 20,1996
print(MyList[:2]) ## Gets every value up until position 2 i.g MyList[0], MyList[1]





######## LIST MODIFICATION ########

Lesson("List Modification")

MyList = ['david', 20, 1996]
MyList = MyList + ['Management Information Systems'] ## Says MyList Equals what it currently has plus the new item
MyList.append('Oklahoma Wesleyan University') ## Adds it to the end of the list. A shorter version if you like. Does the same as above.
MyList.pop() ## Will remove the last option and return it's value. Removes 'Oklahoma Wesleyan University'


print(MyList) ##prints the list
print(MyList.pop()) ## Removes the last item and prints it: 'Management Information Systems' **We popped OKWU Earlier
print(MyList) ## Prints the list again without MIS

## YOU CAN ALSO SET A POSITION INSIDE THE .pop() e.g. 0, 1, 2 MyList.pop(0) otherwise it defaults to last item in table.





############ ORGANIZING ############

Lesson("Organization")

Original = ['Mykelti', 'David', 'Trevor', 'Bethany']

MyList = ['Mykelti', 'David', 'Trevor', 'Bethany']
MyList.reverse() ## Reverses the list

MyList2 = ['Mykelti', 'David', 'Trevor', 'Bethany']
MyList2.sort() ## Sorts the list alphabetically!!!


print("%s Original" %(Original)) 
print("%s Reversed" %(MyList)) 
print("%s Sorted" %(MyList2)) 





############ MATRIX'S ############

Lesson("Matrix's")

Account1 = ['David Hall', 'david.hall@okwustudents.edu', 'MyPassword']
Account2 = ['Trevor Carter', 'trevor.carter@okwustudents.edu', 'TrevorsPassword']

AccountList = [Account1, Account2] ## We can store multiple lists in another list. This is known as a Matrix


print(AccountList) ## List of Accounts
print(AccountList[0]) ## This prints what's in the first position. Which is our Account1 List
print(AccountList[0][0]) ## This goes to the first position. Account1List, the the first position of that which is 'David Hall'





############ PRACTICE #############




Lesson("Managing Accounts (challenge)") ## it's recommended you leave the (challenge) so students know it's an exercise

########### EXERCISE 1 ############

## Add an account with your information by creating a variable named Account 6 and add it to the AccountList
## Sort the accounts in alphabetical order
## create an okwu email for each student using .append()
## Lastly, print your Full Name by finding the position. I.g. 'Trevor Carter' AccountList[1][0]
Account1 = ['David Hall', 'david.hall', 'MyPassword']
Account2 = ['Trevor Carter', 'trevor.carter', 'TrevorsPassword']
Account3 = ['Mykelti Sheldon', 'mykelti.sheldon', 'MykeltisPassword']
Account4 = ['Dadani Carreno', 'dadani.carreno', 'DadanisPassword']
Account5 = ['Ana Popov', 'ana.popov', 'AnasPassword']

AccountList = [Account1, Account2, Account3, Account4, Account5]


print("\n\n")