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
    print(a + "Python Statements: " + Title) ## ENTER the overall section title here
    print("-------------------") ## Creates an underline for the title of each section
    


####### STATEMENTS IN PYTHON #######



############ EXAMPLE 1 ############

Lesson("Basics") ## Change this for each subsection. i.e. Python SectionHere: Lesson 1 Name

BankAccount = 100000


if BankAccount > 100**3: ##If statements check to see if something is tur or not | Refer back to Operators to find what you can use.
    print("You are a millionaire! Congratulations!")
    

    
if BankAccount < 100**3: ##You can require something to be false to pass through the statement
    print("You are not a millionaire and should work harder at life!")

    
    
    

############ EXAMPLE 2 ############

Lesson("If | elif | else")

BrokerageAccount = 300000 ## $300,000


if BrokerageAccount <= 100000: #Check to see if this is true
    print("You have between $0 and $100,000 invested")
elif BrokerageAccount <= 500000: #If we have more than 100,000 and less or equal to 500,000 do this
    print("You have between $100,001 and $500,000 invested")
else: ##if we anything above 500,000 it will result in this. | Defaults to this if: 1.) the if statement is false 2.) all elif statements are false.
    print("You have between $500,001 and infinity invested")

    
    


############ PRACTICE #############


########### NETFLIX ############

Lesson("Netflix (challenge)") 

##https://www.amctheatres.com/ratings-information
##Continue to this website and look at the movie requirements
##Add an if,elif,and else statement to check to see what age they are:
##In each category have a list with 2 movies of that type like: Toy Story, Finding Dory
##Lastly Create an Age variable, and have it so when you run the script it prints all the movies that person can see.






########### COMISSIONS ############

Lesson("Comission Charges (challenge)")

##You will want to import your interest calculator from S3-Lesson1-Numbers
##Create an if,elif,and else statement to check whether the person's money.
##Create it so:
##if there's less than $100,000 the comission is 2%. 
##if there's less than or equal to $250,000 the comission is 1.5%.
##if there's less than $500,000 the comission is 1%.
##if there's greater than $500,000 the comission is .75%
##You're new calculator formula will be: The formular is A = P(1+(r-c)/n)**(n*t) where c is comission


print("\n\n")