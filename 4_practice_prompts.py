

# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it
keyboard= "keyboard"
mouse= True
computer= "Mr Evins"

print(f"while I was in computer science class I used my {keyboard} to send the word {mouse} to my teacher {computer}")

# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.
print("manuel")
print("Today is November 3rd")
print("Minecraft movie")
# Print your name and age on separate lines using a single print() function.
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
Yourname= "Manuel"
age= 16 + 10
print(f"in 10 years {Yourname} will be {age} years old")
##############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value


#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen

# print the length of the summary
# upper case the entire summary
# print the summary
# print the summary in lowercase
# replace the word blue with red
# print the summary
# string index the word beetle and print it out
# print the last word of the summary
# print the summary in reverse
summary= "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Red Beetle."

print(len(summary))
print(summary.upper())
print(summary)
print(summary.lower())
print(summary[-7:-1])
print(summary[-7:-1])

reversedsummary= summary[::-1]
print(reversedsummary)

##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.
print(input("What is your name"))
# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
print(input("What are you learning today?"))
# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
print(input("Where are you from?"))
# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?s
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.
name= input("What is your name?")
surname= input("What is your surname?")
print(f"Hello, your full name is {name} {surname}")

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.

fname= input("What is your full name?")
fcolor= input("what is your favorite colro?")
print(f"{fname} you like the color {fcolor}")
