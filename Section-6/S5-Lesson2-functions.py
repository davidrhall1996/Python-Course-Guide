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
import math
def Lesson(Title):
    a = "\n" * 3 ## Distance controller adjust for more or less spacing; 
    print(a + "Python Functions: " + Title) ## ENTER the overall section title here
    print("-------------------") ## Creates an underline for the title of each section
    


####### FUNCTIONS IN PYTHON #######



############ EXAMPLE 1 ############

Lesson("Basics") 

##If you look above I've been using functions since the beginning of these tutorials
##functions are used to make life easier and running a block of code several times with different variables
def MyFunctionNameHere():
    x = 10 + 10
    print(x)
    
#unlike loops functions don't run automatically they have to be called
##Called is being written in the program:
MyFunctionNameHere() ##This does everything in lines 43-44






############ EXAMPLE 2 ############

Lesson("Variables") 


def MyFunctionNameHere(AVariable): ##This states that something is required in the () when calling MyFunctionNameHere()
    x = 10 + AVariable ##We want to be able to change the value of x to 10 + An unknown number at the moment
    print(x)
    

MyFunctionNameHere(3) ##Remember MyFunctionNameHere requires an arguement to work, so we gave it 3
##This will run lines 57-58 as: x = 10+3 \n print(x) \n output is 13

MyFunctionNameHere(5) ##We can run everything again but this time with 5 and will output 15

def MySecondFunction(FirstVariable, SecondVariable):
    x = FirstVariable * SecondVariable
    print(x)
    
MySecondFunction(3,2) ## FirstVariable = 3, SecondVariable = 2 therefore x = 3 * 2 --> x = 6






############ EXAMPLE 3 ############

Lesson("Returning") 

def Pythagorean_Theorem(A,B):
    ASquared = A**2 ##In future tense this equals 9
    BSquared = B**2 ##In future tense this equals 4; Look below.
    return ASquared+BSquared ##Sets what called this function = to this value

CSquared = Pythagorean_Theorem(3,2) ##we can use this to return the value of a function so a variable can equal it
##In this case CSquared = 13
print(CSquared)





############ PRACTICE #############

Lesson("Interest Calculator")

########### InterestCalculator ############
##Create our interest calculator as a function so that we can change the values of P,n,r and t
##Refer back to S3-Lesson1-Numbers









print("\n\n")