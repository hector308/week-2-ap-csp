# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Hector"
age = 15
favorite_color = "Blue"
favorite_number = 7

#  Step 2: Practice String Operations
# 1. Print your name in uppercase
print(first_name.upper)

# 2. Print how many letters are in your name
print(len(first_name))

# 3. Combine your name and favorite color into one message

print (f"{first_name} and {favorite_color}")
#  Step 3: Math Practice
# Use arithmetic operators with your favorite number
num1=13
print(favorite_number+num1)

#  Step 4: User Input Practice
# Ask the user two questions and combine answers
#num3= int(input("What is your favorite number?"))
#num4= int(input("What is your second favorite number?"))
#print (num3+num4)
# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together
username= (input("What is your name?"))
favnum1= int(input("What is your favorite number"))
favnum2= int(input("What is your second favorite number"))
print(f"Hello {username}, how are you, I know you like the color{favnum1}+{favnum2}")