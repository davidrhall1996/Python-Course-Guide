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
from __future__ import print_function
import math, os
NeededDirectory = os.path.dirname(os.path.realpath(__file__))
os.chdir(NeededDirectory)
def Lesson(Title):
    a = "\n" * 3 ## Distance controller adjust for more or less spacing; 
    print(a + "Python Lambda and Nests: " + Title) ## ENTER the overall section title here
    print("-------------------") ## Creates an underline for the title of each section
    


####### FUNCTIONS IN PYTHON #######



############ EXAMPLE 1 ############

Lesson("Basics") 

##Lambda is a single expression that is basically a crushed function
def MyFunction(num1,num2): 
    result = num1 + num2
    return result

def MyFunction(num1,num2):##Equals above code
    return num1 + num2

def MyFunction(num1,num2): return num1 + num2##Equals above code

MyLambdaName = lambda num1,num2: num1+num2 ##Equals above code

x = MyLambdaName(3,5)

print(x) ##x = 8





############ EXAMPLE 2 ############

Lesson("Operations")

##Lambda can perform operations as well

StringCutter = lambda AString: AString[:-1]

x = StringCutter("Hello")
print(x) ## Where bad people go

PrintMyDictionary = lambda ADictionary: ADictionary.keys()

Names = {'a' : 'Alpha', 'b' : 'Beta', 'c' : 'Charlie'}

x = PrintMyDictionary(Names)

print(x)




############ EXAMPLE 3 ############

Lesson("Local and Global Variables")

AVariable = 200 ##This variable is global and can be used anywhere

def LocalTesting():
    AGlobalVariable = -20 ##AVariable equaling -20 is local and will only equal that for the duration of the function.
    print(AGlobalVariable) ## prints -20

LocalTesting() ##will print -20 because it's printing the local AVariable inside the function

print(AVariable)##Will print 200 because it's printing the Global Variable


############ PRACTICE #############

Lesson("Lambda Math (Challenge)")

########### InterestCalculator ############
##You will need to search on your own; Variable Arguments
##Create a lambda that will find the sum of numbers given
##Research *args to make this work
##We want to be able to do SolveMath(1,2,3) or SolveMath(40,37,52,11, 26)





##This is how the sum function was created.



print("\n\n")