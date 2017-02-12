#import string
#check all methods of string ===> dir(string)
#string.ascii_letters gives all letters but we want only lowercase
#string.ascii_lowercase
import string, random

def generator():
    letter1= random.choice(string.ascii_lowercase)
    letter2= random.choice(string.ascii_lowercase)
    letter3= random.choice(string.ascii_lowercase)
    name = letter1 + letter2 + letter3
    return(name)

print(generator()) 
