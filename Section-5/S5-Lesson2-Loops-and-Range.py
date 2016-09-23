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
import math, os
NeededDirectory = os.path.dirname(os.path.realpath(__file__))
os.chdir(NeededDirectory)
from DBC import *
def Lesson(Title):
    a = "\n" * 3 ## Distance controller adjust for more or less spacing; 
    print(a + "Python Loops: " + Title) ## ENTER the overall section title here
    print("-------------------") ## Creates an underline for the title of each section
    


####### LOOPS IN PYTHON #######



############ EXAMPLE 1 ############

Lesson("Basics") ## Change this for each subsection. i.e. Python SectionHere: Lesson 1 Name

G_Rated_Movies = ["Toy Story", "Toy Story 2", "Toy Story 3"]

for EveryMovie in G_Rated_Movies: ##You can call the variable EveryMovie anything you want. I did EveryMovie so it makes more sense what we are looping.
    print(EveryMovie) ## for EveryMovie will = Toy Story and since it's a loop will = Toy Story 2 and go through the list G-Rated_Movies until it is at the end.
    
    
    
    
    
############ EXAMPLE 2 ############

Lesson("Range")

PossibleAnswers = ["A.) A dog", "B.) A cat", "C.) A Lizard", "D.) All the above", "E.) None of the Above", "F.) Blah blah blah"]

print("What Animal is your Favorite?")
for Pos in range( len(PossibleAnswers) - 1): ## Will loop through every item in the list except the last
    print(Pos) ## When using range the variable becomes the List Position
    print(PossibleAnswers[Pos]) ## This will go through and loop printing PossibleAnswers[1], PossibleAnswers[2], etc.
    print("DEVELOPER DEBUGGER: '%s' is at table position %s in the list PossibleAnswers.\n\n" %(PossibleAnswers[Pos], Pos))
    

    
    

############ EXAMPLE 2 ############

Lesson("Information Dissection Advanced")

NetflixMovies = {'GMovies' : {'L' : 'Lelo and Sitch', 'T' : 'Toy Story'}, 'RMovies' : {'D' : 'Deadpool', 'T' : 'The Conjuring II'}}

## It might be easier to read this in console then come back and read the code. If you're having trouble reference the dictionary Lesson S3-Lesson5

for key in sorted(NetflixMovies): ##Reinforces alphabetically | Remember Dictionaries are KeyName : Value
    print("Key Name: %s" %(key))
    print("Print value of %s: %s ##It's another dictionary!" %(key, NetflixMovies[key]))
    print("## we see that it contains more Key's and values e.g. Key = Letter movie starts with, Value is Movie Name. Let's print those as well...")
    for InsideKey in NetflixMovies[key]: ##Accesses the inner Dictionaries
        print("\t Key Name: %s" %(InsideKey)) ##Prints the key of the inner Dictionaries
        print("\t Print Value of %s: %s" %(InsideKey, NetflixMovies[key][InsideKey])) ## Prints the Vaules of a Value an inner Dictionary
    print("\n")
    
    
print("Imagine if NetflixMovies contained 1000 movies. We would not want to type print(NetflixMovies[1]) all the way to NetflixMovies[1000] loops help us to do tasks the require a repeat of the same operation or close to the same")





############ EXAMPLE 2 ############



############ PRACTICE #############



########### Wesleyan ############

Lesson("Giving Wesleyan Students ID Numbers")
## See if you can use a for loop to print ID's for 10000 Students
## I will assist you with the print function
## print("%010d" %(EachStudent)) so it will start: "for EachStudent in.....
## Make an if statement inside the loop so that if it is your id it will print("THIS IS ME!!) then scroll up to see if it worked.



########### COMISSIONS ############

Lesson("Database Extraction (challenge)")
##Here you will be asked to manipulate a database to find leads for a sales company
##I would like you all to search through a List called DataBase
##In the list DataBase it contains 3000 lists each with a person name and phone number
##Create a for loop and if function to find every person with a phone number that starts with:  (156) Exactly
##Lastly I want you to print the names of these people
##DataBase is the list name it does not need to be created.



##If done correctly it will list these names;
##John Baily
##Max Nash
##Lauren Ball
##Benjamin Poole
##Joshua Mills
##Stephanie Sanderson

##If you are interested in learning more about how I did this open the DBC.py file for extra commentary on database creation.





print("\n\n")