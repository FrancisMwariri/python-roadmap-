"""
Python Basics Lesson 1

Goal:
Learn the building blocks of Python before we move to game coding.

What we will learn in this file:
- What Python is
- print() and comments
- variables
- data types
- arithmetic
- user input
- type conversion
- small exercises
"""

# 1) print() - showing output to the screen
print("Hello, Francis!")
print("Welcome to Python programming.")

# 2) Comments - notes that Python ignores
# This is a single-line comment.

"""
This is a multi-line comment.
It helps explain code.
"""

# 3) Variables - storing information in memory
name = "Francis"
age = 20
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# 4) Data types
# int -> whole numbers
# float -> decimal numbers
# str -> text
# bool -> True / False

number_of_cars = 5        # int
price = 19.99              # float
city = "Berlin"           # str
has_license = True         # bool

print(type(number_of_cars))
print(type(price))
print(type(city))
print(type(has_license))

# 5) Basic arithmetic
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # integer division
print(x % y)   # remainder
print(x ** y)  # power

# 6) Strings
first_name = "Francis"
last_name = "Programming"

full_name = first_name + " " + last_name
print(full_name)

print(first_name * 3)
print(len(first_name))
print(first_name.upper())
print(first_name.lower())

# 7) User input
# input() always returns a string
# name_input = input("What is your name? ")
# print("Hello, " + name_input)

# 8) Type conversion
text_number = "42"
converted = int(text_number)
print(converted + 8)

float_value = float("3.14")
print(float_value + 1)

# 9) Using variables in a small real example
car_speed = 80
speed_limit = 60

if car_speed > speed_limit:
    print("You are driving too fast.")
else:
    print("You are within the speed limit.")

# ------------------------------------------------------
# Exercise 1
# Create a program that asks for a user's name and age,
# then prints: "Hello <name>, you are <age> years old."
#
# Example output:
# Hello Francis, you are 20 years old.
# ------------------------------------------------------

# Try this code yourself:
# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# print("Hello " + user_name + ", you are " + user_age + " years old.")

# ------------------------------------------------------
# Exercise 2
# Create variables for:
# - player_name
# - score
# - level
# Then print a message showing the current game status.
# ------------------------------------------------------

# Example answer below:
player_name = "Francis"
score = 1500
level = 3
print(f"Player: {player_name} | Score: {score} | Level: {level}")

# Important idea:
# f-strings make it easy to combine strings and variables.
print(f"Hi {player_name}, your score is {score}.")

# ------------------------------------------------------
# Mini challenge
# 1. Create a variable called favorite_game.
# 2. Create a variable called favorite_language.
# 3. Print a sentence like:
# "My favorite game is ... and my favorite language is ..."
# ------------------------------------------------------

favorite_game = "car racing game"
favorite_language = "Python"
print(f"My favorite game is {favorite_game} and my favorite language is {favorite_language}.")

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - how to print output
# - variables and data types
# - arithmetic
# - strings and f-strings
# - user input
# - type conversion
# ------------------------------------------------------

print("\nLesson complete: Python basics are now in your toolbox.")
