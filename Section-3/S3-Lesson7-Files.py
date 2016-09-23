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
    print(a + "Python Files: " + Title)
    print("-------------------") 
    


####### PRINTING IN PYTHON #######



####### WRITING AND READING########

Lesson("Writing and Reading")

File1 = open('MyDocument.txt', 'w') ## Creates a new file whether or not it exists. THIS OVERWRITES
File1.write('Line 1')
File1.write('\nLine 2')
File1.write('\nLine 3')
File1.close()

File2 = open('MyDocument2.txt', 'a') ## If file exists, it keeps writing to it. Run the script twice to see.
File2.write('\nLine 1') ## we skip 1 line so when we write it a second time it will go to the next line
File2.write('\nLine 2')
File2.write('\nLine 3')
File2.close()

File1 = open('MyDocument.txt')
File2 = open('MyDocument2.txt')
file_contents = File1.read() ## here we can read and print the contents of a file
file2_contents = File2.read()


print('File 1:\n')
print(file_contents)
print('\n\nFile 2:\n')
print(file2_contents)





############ PRACTICE #############




Lesson("Python with Python (challenge)") ## it's recommended you leave the (challenge) so students know it's an exercise

########### EXERCISE 1 ############

##write a python script using your knowledge of file writing and reading
##I recommend a simple Algebraic opperation and then printing it in the written file.
##Lastly, run the script and check the output.



print("\n\n")