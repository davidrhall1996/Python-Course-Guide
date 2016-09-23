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
    print(a + "Python Numbers: " + Title) ## Used to help organize outputs
    print("-------------------") ## Used to help organize outputs 
    




####### NUMBERS IN PYTHON ########



####### FLOATS AND INTEGERS ######

Lesson("Floats and Integers") ## Used to help organize outputs

x = 3 + 3 ## X is an integer. Integers are all whole numbers; 2,1,0,-1,-2 
y = 3.0 + 3.0 ## Y is a float. Floats are either numbers containing decimals or numbers with exponentials commonly seen in calculators when you do 1 billion * 1 billion; 3.0,2.0, 4E2 (4 * 10)squared
z = 2 + 2 ## try changing the numbers and see the different outputs


print("3 + 3 = " + str(x)) ## Ignore for now will be taught in S3-Lesson3-Printing
print("3.0 + 3.0 = " + str(y))
print(str(z))





############ OPERATIONS ############

Lesson("Operations")

a = 3 + 3 ## 6
b = 3 - 3 ## 0
c = 3 * 3 ## 9
d = 3 / 3 ## 1
e = 3**3  ## 27: Exponent
f = math.sqrt(25)
g = 1 + 1 ## practice changing this and performing the different arithmatics.


print("3 + 3 = %s" %(a)) 
print("3 - 3 = %s" %(b)) 
print("3 * 3 = %s" %(c)) 
print("3 / 3 = %s" %(d)) 
print("3 ^ 3 = %s" %(e)) 
print("3 * 3 * 3 = %s" %(f)) 
print("%s" %(g)) 





####### FLOAT VS INTEGER OPERATIONS #######

Lesson("Float vs. Integer Operations")

a = 3 / 2 ## 3 / 2 = 1.5 HOWEVER, since it is an integer it must be a whole number and python rounds down. Therefore, the output is 1
b = 3.0 / 2 ## Here we get the answer probably desired. 1.5 because it is a float
c = 0## practice something like 1/3 


print("3 / 2 = %s" %(a)) 
print("3.0 / 2 = %s" %(b)) 
print("%s" %(c)) 





############# PEMDAS #############

Lesson("PEMDAS")

## Python follows PEMDAS ORDER: PARENTHESIS, EXPONENTS, MULTIPLICATION, DEVISION, ADDITION, SUBTRACTION

a = 2*(3+1)**2/4+10-11 ## Parenthesis (3+1) = (4), Exponent (4)**2 = 16, Multiplication 16*2 = 32, Division 32/4 = 8, Addition 8 + 10 = 18, Subtraction 18 - 11 = 7


print("%s" %(a)) 





############ PRACTICE ############

## INTEREST CALCULATOR ##

Lesson("Interest Calculator (Challenge)")

## The formular is A = P(1+r/n)**(n*t)
## Create each variable separate
## P = Principal, r = Rate %, n = times compounded per year, t = years
## find How much money you will have if you invest your college tuition, $100,000 into a investment account for 40 years earning 7% interest compounded yearly.

##CREATE HERE##
P = 100000
r = .07
t = 40
n = 1
A = P*(1+r/n)**(n*t)



## STOP HERE ##

##uncomment the print line when you are done and run the script. The correct answer should be $1,497,445.78
print("You invested $%s in 2016. Over %s years you earned on average %1f percent and are now retired with $%1.2f" %(P, t, r*100, A)) 


print("\n\n")