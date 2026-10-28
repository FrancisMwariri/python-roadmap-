"""
Python Lesson 3: Functions

Functions let us group code into reusable blocks.

Why they matter:
- avoid repeating code
- break big problems into smaller parts
- easier debugging
- build game systems cleanly
"""

# ------------------------------------------------------
# 1) A simple function
# ------------------------------------------------------
def greet():
    print("Hello, Francis!")


greet()
greet()

# A function is a reusable block of code.
# It only runs when we call it.

# ------------------------------------------------------
# 2) Function with parameters
# ------------------------------------------------------
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming.")


greet_user("Francis")
greet_user("Alice")
greet_user("Sam")

# Parameters are inputs to the function.

# ------------------------------------------------------
# 3) Function with multiple parameters
# ------------------------------------------------------
def add_numbers(a, b):
    total = a + b
    print(f"{a} + {b} = {total}")


add_numbers(5, 7)
add_numbers(12, 8)

# ------------------------------------------------------
# 4) Return values
# ------------------------------------------------------
def multiply(x, y):
    return x * y


result = multiply(4, 6)
print("Result:", result)

# A function can return data so we can use it later.

# ------------------------------------------------------
# 5) Function that returns a message
# ------------------------------------------------------
def get_player_status(name, score):
    return f"Player {name} has {score} points."


status = get_player_status("Francis", 1500)
print(status)

# ------------------------------------------------------
# 6) Default parameter values
# ------------------------------------------------------
def describe_car(name, speed=0):
    return f"Car: {name}, Speed: {speed} km/h"


print(describe_car("Sedan"))
print(describe_car("Sport", 120))

# Default values allow us to skip some arguments.

# ------------------------------------------------------
# 7) Scope
# ------------------------------------------------------
player_name = "Francis"  # global variable


def show_player_name():
    print(player_name)


show_player_name()

# A function can use variables outside it if they are global.
# But it is usually better to pass values as parameters.

# ------------------------------------------------------
# 8) A game-like function example
# ------------------------------------------------------
def update_score(score, points):
    score = score + points
    return score


score = 100
score = update_score(score, 50)
print("Updated score:", score)

# This is how score systems work in a game.

# ------------------------------------------------------
# 9) Another example: speed check
# ------------------------------------------------------
def check_speed(speed_limit, current_speed):
    if current_speed > speed_limit:
        return "You are speeding."
    return "You are within the speed limit."


print(check_speed(60, 75))
print(check_speed(60, 50))

# ------------------------------------------------------
# 10) Functions for game logic
# ------------------------------------------------------
def player_hit_wall(position, wall_limit):
    if position > wall_limit:
        return True
    return False


print(player_hit_wall(120, 100))
print(player_hit_wall(80, 100))

# ------------------------------------------------------
# Exercise 1
# Create a function called square that takes a number and returns its square.
# ------------------------------------------------------

def square(number):
    return number * number


print("Square of 5:", square(5))

# ------------------------------------------------------
# Exercise 2
# Create a function called is_even that returns True if a number is even.
# ------------------------------------------------------

def is_even(number):
    return number % 2 == 0


print(is_even(8))
print(is_even(7))

# ------------------------------------------------------
# Exercise 3
# Create a function called calculate_distance(speed, time) that returns speed * time.
# ------------------------------------------------------

def calculate_distance(speed, time):
    return speed * time


print("Distance:", calculate_distance(60, 2))

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - how to create functions
# - parameters and arguments
# - return values
# - default parameters
# - why functions make code cleaner
# ------------------------------------------------------

print("\nLesson complete: functions help you organize your code like a real programmer.")
