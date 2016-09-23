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
    print(a + "Python Strings: " + Title) ## Used to help organize outputs
    print("-------------------") ## Used to help organize outputs 
    





####### STRINGS IN PYTHON ########



############# BASICS #############

Lesson("Basics") ## Used to help organize outputs

Hello = 'Hello, my name is name_here!' ## strings are text that would be read and are more logical like this here
Reply = "Hi, it's great to meet you!"  ## strings can be create with a variable using '' or ""


print("%s\n%s" %(Hello, Reply))  ## Ignore for now, will be taught in S3-Lesson3-Printing





########## DOUBLE QUOTES ##########

Lesson("Double Quotes")

Quotes = ' David Hall says; "I love python" ' ## You can add quotations into strings by starting with ''
Apostrophe = " It's hot in here." ## The reverse of the previous string ' can be added by using " instead
QA = ' David Hall says; "It\'s hot in here" ' ## We need to put the \ before the ' in It's so it knows it's part of the string otherwise it will end the string early and not work. Try it without the \ if you like it will break. This is a third alternative when you have a lot of '' or "" in your string.
MyQuote = " YourQuoteHere "## Try Replacing with something else containing apostrophe and quotes


print("%s\n%s\n%s\n%s" %(Quotes, Apostrophe, QA, MyQuote)) 





############ LENGTH ############

Lesson("Length")

WordLength = len('Hi') ## This will print 2
MyWord = 'Hello'
VariableLength = len(MyWord) ## This will print 5


print("%s\n%s" %(WordLength, VariableLength)) 





############# STRING IDENTIFICATION #############

Lesson("String Identification")

s = 'Hello' ## Length is measured starting from 1. e.g. 1-5
Identify = s[0] ##Position is measured starting from 0. e.g. Hello goes 0-4. This will print H
Shorten = s[1:] ##This will start at position 1 and get everything after. ello
ShortenBack = s[:3] ##This will start at 0 and get everything before position 3. Hel

print("%s\n%s\n%s" %(Identify, Shorten, ShortenBack)) 





############ STRING IDENTIFICATION 2 ############

Lesson("String Identification 2")

s = 'Hello'
Identify = s[-1] ## Negatives will go from Right to left. This will print o
Shorten = s[:-1] ## This will start at 0 and go until the end - 1. This will print Hell


print("%s\n%s" %(Identify, Shorten)) 





############ STRING IDENTIFICATION 3 ############

Lesson("String Identification 3")

s = 'Hello'
EveryLetter = s[::1] ## This will give you every character. This will print Hello
EveryOther = s[::2] ## This will give you every other character. This will print Hlo
Inverse = s[::-1] ## This will print the word backwords. olleH


print("%s\n%s\n%s" %(EveryLetter, EveryOther, Inverse)) 





############## STRING OPERATIONS ##############

Lesson("String Operations")

s = 'Hello'
Multiply = s*3 ##Strings can be multiplied! HelloHelloHello
Capitalize = s.upper() ## This will Capitalize everything. HELLO
lowercase = s.lower() ## This will force lowercase. hello
Table = s.split('e') ## This will split a string into two parts. ['H', 'llo']


Note = "##It's important to note these are in a table, and can access 1 of 2 strings either 'H' by Table[0] or 'llo' by Table[1]"
print("%s\n%s\%s\n'%s' '%s' %s" %(Multiply, Capitalize, lowercase, Table[0], Table[1], Note))  





############## PRACTICE #######################

Lesson("Fix something broken (challenge)")

## EXERCISE 1 FIX SOMETHING BROKEN ##
## Get rid of the FIRST ## and fix the print function so it can print the string inside.

##print('Andrea's mom asked; "What would you like to eat?". Andrea replied "Ice cream!") 



Lesson("Broken website link (challenge)")

## EXERCISE 2 BROKEN WEBSITE LINK ##
## Use String Operations and Identification to fix this website link

Website = "whttps://www.okwu.edu.vanilla"



print("\n\n")