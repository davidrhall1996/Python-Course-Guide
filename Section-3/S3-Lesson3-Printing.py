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

def Lesson(Title):
    print("\n\n\nPython Printing: " + Title) ## Used to help organize outputs
    print("-------------------") ## Used to help organize outputs 




####### PRINTING IN PYTHON #######



############# BASICS #############

Lesson("Basics") ## Used to help organize outputs

print("I love chocolate!")## Printing is done with print("What you want to print here"); The text inside is a string.
print() ## Try printing anything you want here! Don't forget to add "" or ''

print """ 
if you like
replace this with
a nice poem or quote.
""" ## Three quotations are used to create Long Texts





############ COMBINING ###########

Lesson("Combining") ## IGNORE THESE


print("I turn in my homework " + "late") ## You can combine multiple Strings together and print the combination
print("The early bird gets ") ## Try completing this phrase using 2 strings: Hint - The early bird gets the worm.





########## ORGANIZATION ##########

Lesson("Organization")


print("Roses are red,\nViolets Are Blue") ##There is a \n which sends the rest of the string after to the next line.
print("\t The Beginning of my very boring college essay") ## \t will will tab the printed information for you.





############ NUMBERS #############

Lesson("Numbers")

MyNumber = 123
## print("This is my Number: " + MyNumber) this will not work because python can't read integers only strings
print("This is my Number: " + str(MyNumber)) # when trying to identiy non-strings add str(SomeVariableHere) to make it so python can read it as a string.



####### MULTIPLE VARIABLES ######

Lesson("Multiple variables")

## Important syntax to know; %s, %1f, %r
x = 1/3
y = 2.456789
Mystring = '%r prints raw data including things like \t, \n, %s, %f, etc.'


print("Print this number: %s" %(x))  ## prints %(Whatever is in here)
print("Print this integer: %1.3f" %(y))  ## 1.1 go 1 decimal and round up 1.3 go 2 decimals and round up
print("Print raw data: %r" %(Mystring))  ## This prints the raw data and is used for debugging
print("Print Multiple Numbers: %s, %s, %s" %(10, 20, 30)) 





############ PRACTICE ############



Lesson("Create MLA (Challenge)")

## EXERCISE 1 CREATE MLA ESSAY ## 
## Use the variables rather than triple quotations so we can easily modify the input fields as desired.
##Name = "Your Name Here" 
##Professor = "Dr. Cochran"
##Course = "Intro. to Python"
##Date = "September 16th, 2016"
##Title = "My experience with python"
##Sentence1 = "Dr. Cochran once said facetiously; 'Google is evil'." 
##Sentence2 = "This is the thesis on why Google is a evil company bent on global domination."
##print()


print("\n\n\n")