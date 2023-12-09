#As we know we can create string using 3 types
a=' Prathamesh ' #single Quoted 
#a='"prathamesh"' #here double Quote is get printed
b=" Prakash " #Double Quoted
#b="prakash's" #here single Quote is get printed
c=''' Wadkar ''' #Ttriple Quoted

#concatinationx
c= a+ b+ c
print(c)
print(type(c))

#Accessing String elements using index
print(c[8])
#we cant change the value using index e.g c[6]='t' this wont work

#slicing a String 
#Syntax name[starting_index : End_index]
#Starting Index is always "0"
print(c[1:5])
print(c[:8]) #here by defualt starting index is 0
print(c[4:]) #here by default end index is the last index of string

#Negative Indexing
#the last element is represented by '-1' followed by megativ Integers
print(c[-3])
#this is useful when you dont know the string lenght and want to get last character.

#slicing  with skiping characters
print(c[0:-1:2])
#the last Character 2 indicates that skip every 2nd charcter

#string functions
#len funtion to get the lenght of string
str = "here is the string for performing the string operations."
print(len(str)) #this returns the interger value

#to find wether the strings end with the string
print(str.endswith("string")) #it gives true or false value
print(str.endswith("tions.")) #it gives true or false value
#it also checks the substring but last index must be there 




# Find and replace funtion
letter = '''
hello <|name|>,
we are happy to say that you are selectd
for this internship
happy learning!
reguards
HR
<|date|>
'''
name = input("Enter the name : ")
date = input("Enter the date : ")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)

print(letter)