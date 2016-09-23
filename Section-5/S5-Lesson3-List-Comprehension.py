##################################
##     Pyton Sections 5 & 6     ##
##           Examples           ##
##         By David Hall        ##
##                              ##
##           Statements         ##
##                              ##
##             Loops            ##
##                              ##
##             Range            ##            
##                              ##                             
##       List Comprehension     ##
##                              ##
##             Methods          ##
##                              ##
##            Functions         ##
##                              ##
##             Lambda           ##
##                              ##
##              Nests           ##
##                              ##    
##       Comparison Operators   ##
##################################
import math, os, string
NeededDirectory = os.path.dirname(os.path.realpath(__file__))
os.chdir(NeededDirectory)
from DBC import *
def Lesson(Title):
    a = "\n" * 3 ## Distance controller adjust for more or less spacing; 
    print(a + "Python Comprehensions: " + Title) ## ENTER the overall section title here
    print("-------------------") ## Creates an underline for the title of each section
    


####### COMPREHENSION IN PYTHON #######



############ EXAMPLE 1 ############

Lesson("Lists") ## Change this for each subsection. i.e. Python SectionHere: Lesson 1 Name

WordInParts = []

for EachLetter in 'ThisWord': ## Will loop through the string 'ThisWord' and EachLetter will = T, then h,i,s,W,o,r,D
    WordInParts.append(EachLetter) ##Add it to the end of WordInParts List
    
print(WordInParts)


WordInParts = [EachLetter for EachLetter in 'SeparateThis'] ##We can make the previous loop shorter
##We want EachLetter to go into the list so that is the first variable
##We then want to set EachLetter equal to something
##We use SeparateThis as the string we want EachLetter to equal
print(WordInParts)


print("\n")

MyNumbers = [EachNumber for EachNumber in range(1,5)] ##We can use range to find stuff. Won't include 5
print(MyNumbers)

print("\n")

MyNumbers = [EachNumber for EachNumber in range(1,11) if EachNumber % 2==0] ##We add if statements. if the remainder = 0 then add EachNumber to the table.
##This means if it is a whole number: 2, 4, 6, 8, 10 it will go into MyNumbers List
print(MyNumbers)



############ EXAMPLE 2 ############

Lesson("Dictionaries")

SquareDictionary = {}
for x in range(1,10):
    Key = "%s squared" %(x)
    Value = x**2 
    SquareDictionary[Key] = Value
    
print(sorted(SquareDictionary))
print(sorted(SquareDictionary.values()))
    
print("\n")

    
SquareDictionary = {"%s squared" %(x): x**2 for x in range(1,10)} ##same as writing SquareDictionary = { '1 squared : 1', '2 squared', etc. }

print(sorted(SquareDictionary)) ## As we can see the same output is created with 1 line rather than 4
print(sorted(SquareDictionary.values()))


############ PRACTICE #############



########### DBC ############

Lesson("More Database Management (challenge)")
## We will use the DataBase again to find specific people
## Create a list that will search the DataBase for names 
## if it comes across a name "Joshua" then it will be added to the list
## Lastly print the names of everyone who has Joshua in their name
## 2 lines of code maximum;





########### COMISSIONS ############

Lesson("Database Extraction (challenge)")
##create a dictionary that has all lowercase letters a-z as the key and all upercase as the value
##string.ascii will help. Google searching will most likely be required.
import string
##Start under here



print("\n\n")