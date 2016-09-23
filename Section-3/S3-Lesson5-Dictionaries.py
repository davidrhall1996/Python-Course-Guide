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
    print(a + "Python Dictionary: " + Title) 
    print("-------------------")
    


####### PRINTING IN PYTHON #######



############ BASICS ############

Lesson("Basics") 

FirstDictionary = {'Key' : 'Value'} ## Dictionaries are used to find Information and have a 'key' (like a position) and then a value
Realistic = {"Ethic's" : "moral principles that govern a person's or group's behavior."}


print(FirstDictionary['Key']) ##notice like in a table we use [] however instead of position value: 0,1,2 we print it by it's name
print(Realistic["Ethic's"]) ## This will print the vaalue of Ethics which is a string





########## IDENTIFICATION ##########

Lesson("Identification and Modification")

MyDictionary = {'Happy' : 'feeling or showing pleasure or contentment.'}
MyAge = {'Age' : 30}


print(MyDictionary['Happy'][0]) ## prints f
print(MyDictionary['Happy'][1:]) ## Everything but f
print(MyAge['Age'] - 10) ## Just turned 30? You can modify Dictionaries to make yourself younger :-)





######### ADV. MODIFICATION #########

Lesson("Advanced Modification")

MyAge = {'Age' : 20 }
MyName = {'Name' : 'David'}

MyAge['Age'] = MyAge['Age'] + 10 ## This will make make MyAge['Age'] = 20 + 10 but that's a lot of writing :(
MyAge['Age'] += 10 ## += means whatever is left e.g. MyAge['Age'] = itself + 10: My['Age'] = 30 + 10

MyName['Name'] = MyName['Name'].upper() ## Can modify strings in dictionaries. Output: DAVID

          
print(MyAge['Age']) ## You age is now 40 because you added 10 twice
print(MyName['Name']) ## prints your name in all caps





######### DIRECT AND NESTS #########

Lesson("Direct and Nests")

DirectDictionary = {}
DirectDictionary['Dog'] = 'Animal' ## This will directly add it in like: DirectDictionary = { 'Dog' : 'Animal' }

Dictionaries = { 'Dictionary1' : {'Attack' : 'an aggressive and violent action against a person or place.'}} ## Like lists dictionaries can be have multiple Dictionaries in them


print(DirectDictionary['Dog'])
print(Dictionaries['Dictionary1']['Attack']) ## Similar to lists, dictionaries find values by name


############# Listing ##############

Lesson("Listing")

MyDictionary = {'Dog' : 'Man\'s best friend', 'Human' : 'Superior Species', 'Cat' : 'A curious animal'}


print(MyDictionary.keys()) ## You can find all the keys in a dictionary with .keys()
print(MyDictionary.values()) ## You can see an overview of all the values with .values()





############ PRACTICE #############


Lesson("Create a Dictionary (challenge)") ## it's recommended you leave the (challenge) so students know it's an exercise

########### EXERCISE 1 ############

##Create a dictionary containing two dictionaries inside it. Name the first inside one A-B and second C-D.
##Next add a Word and Definition into each Dictionary.  A-B should have a A word and B word. C-D should have a C word and D word.
##Lastly print the keys and values inside your main dictionary, A-B and C-D IN SORTED ORDER!!



print("\n\n")