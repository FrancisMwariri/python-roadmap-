"""
Python Lesson 2: Control Flow

In this lesson we learn how programs make decisions and repeat actions.

Main ideas:
- if, elif, else
- comparison operators
- boolean logic
- for loops
- while loops
- break and continue
- simple game-like examples
"""

# ------------------------------------------------------
# 1) Comparison operators
# ------------------------------------------------------
print("Comparison examples:")
print(10 > 5)
print(10 == 10)
print(7 != 3)
print(4 >= 4)
print(2 < 1)

# A comparison gives a boolean value: True or False

# ------------------------------------------------------
# 2) if / else
# ------------------------------------------------------
print("\nDecision making:")
score = 85

if score >= 90:
    print("Excellent! You passed with distinction.")
elif score >= 70:
    print("Good job! You passed.")
else:
    print("You need more practice.")

# The computer checks the conditions in order.
# Only the first matching condition runs.

# ------------------------------------------------------
# 3) boolean logic
# ------------------------------------------------------
print("\nBoolean logic:")
has_key = True
has_map = False

if has_key and has_map:
    print("You can start the journey.")
else:
    print("You are missing something important.")

if has_key or has_map:
    print("At least one item is available.")

# and = both must be True
# or = at least one must be True
# not = opposite of the value

is_game_running = False
if not is_game_running:
    print("The game is not running yet.")

# ------------------------------------------------------
# 4) for loops
# ------------------------------------------------------
print("\nFor loops:")
for i in range(5):
    print("Loop number:", i)

# range(5) gives: 0, 1, 2, 3, 4

# Loop over a list
cars = ["Sedan", "Truck", "Sport", "SUV"]
for car in cars:
    print("Car type:", car)

# ------------------------------------------------------
# 5) while loops
# ------------------------------------------------------
print("\nWhile loops:")
counter = 0
while counter < 5:
    print("Counter is:", counter)
    counter += 1

# A while loop keeps repeating until the condition becomes False.

# ------------------------------------------------------
# 6) break and continue
# ------------------------------------------------------
print("\nBreak and continue:")
for i in range(10):
    if i == 3:
        continue  # skip the rest of this iteration
    if i == 7:
        break  # stop the loop immediately
    print("Value:", i)

# continue = skip the current loop step
# break = exit the loop early

# ------------------------------------------------------
# 7) Simple game-like example
# ------------------------------------------------------
print("\nSimple game logic:")
player_lives = 3
player_score = 120

if player_score >= 100:
    print("You unlocked a bonus level!")
    player_lives += 1

print("Lives:", player_lives)

# ------------------------------------------------------
# 8) Using loops in a game context
# ------------------------------------------------------
print("\nTraffic lights example:")
traffic_light = ["red", "green", "yellow"]
for color in traffic_light:
    if color == "red":
        print("Stop")
    elif color == "green":
        print("Go")
    else:
        print("Slow down")

# ------------------------------------------------------
# 9) Practice challenge: guessing game
# ------------------------------------------------------
print("\nGuessing game example:")
secret_number = 7
guess = 0

while guess != secret_number:
    try:
        guess = int(input("Guess the number from 1 to 10: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it!")

# ------------------------------------------------------
# Exercise 1
# Ask the user for a number.
# If the number is positive print "Positive".
# If it is negative print "Negative".
# If it is 0 print "Zero".
# ------------------------------------------------------

# Example solution:
# value = int(input("Enter a number: "))
# if value > 0:
#     print("Positive")
# elif value < 0:
#     print("Negative")
# else:
#     print("Zero")

# ------------------------------------------------------
# Exercise 2
# Print the numbers 1 to 10 using a for loop.
# ------------------------------------------------------

for number in range(1, 11):
    print(number)

# ------------------------------------------------------
# Exercise 3
# Make a loop that prints only even numbers from 0 to 20.
# ------------------------------------------------------

for even_number in range(0, 21, 2):
    print("Even:", even_number)

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - how Python makes decisions with if statements
# - comparison operators
# - boolean logic
# - for loops for repeating work
# - while loops for repeated checking
# - break and continue for controlling loops
# ------------------------------------------------------

print("\nLesson complete: control flow is the logic behind programs and games.")
