"""
Python Lesson 6: Modules and Project Structure

This lesson teaches how code is organized in larger projects.

Main ideas:
- modules
- imports
- packages/folders
- separating logic into files
- keeping code clean and reusable
"""

# ------------------------------------------------------
# 1) What is a module?
# ------------------------------------------------------
# A module is a Python file. Example: my_program.py
# That file can contain variables, functions, and classes.

# We can import Python code from another file.

# Example:
# import math
# print(math.sqrt(16))

# ------------------------------------------------------
# 2) Creating a simple helper module example
# ------------------------------------------------------
# Instead of writing all logic in one file, we separate it.
# Let's imagine we have two files:
# - helpers.py
# - main.py
#
# helpers.py:
# def add(a, b):
#     return a + b
#
# main.py:
# from helpers import add
# print(add(2, 3))

# ------------------------------------------------------
# 3) Example of using imports from Python builtins
# ------------------------------------------------------
import math

print(math.sqrt(25))
print(math.pi)

# ------------------------------------------------------
# 4) Using the random module
# ------------------------------------------------------
import random

print(random.randint(1, 10))
print(random.choice(["car", "truck", "bike"]))

# Games use modules like these for randomness.

# ------------------------------------------------------
# 5) Project structure idea
# ------------------------------------------------------
# A real project often looks like this:
#
# game/
#   car.py
#   road.py
#   ui.py
# ai/
#   neural_network.py
# config/
#   settings.py
# main.py
#
# This is exactly how the repo is organized.

# ------------------------------------------------------
# 6) Example: separate logic into small files
# ------------------------------------------------------
# Instead of writing everything in one file, we can do:
#
# file: math_tools.py
# def add(a, b):
#     return a + b
#
# file: main.py
# from math_tools import add
# print(add(5, 6))

# This keeps code easier to read and maintain.

# ------------------------------------------------------
# 7) Example: configuration file
# ------------------------------------------------------
# In game projects, config/settings.py holds constants:
# WIDTH = 960
# HEIGHT = 720
# PLAYER_SPEED = 5

# ------------------------------------------------------
# 8) Using a simple custom module
# ------------------------------------------------------
# We can create functions in one file and import them.
# To demonstrate the idea, let's define functions here directly.


def calculate_distance(speed, time):
    return speed * time


def format_score(player_name, score):
    return f"{player_name}: {score} points"


print(calculate_distance(60, 2))
print(format_score("Francis", 500))

# ------------------------------------------------------
# 9) Why this matters for the repo
# ------------------------------------------------------
# The repo uses multiple folders and files:
# - main.py
# - config/settings.py
# - game/arena.py
# - game/car.py
# - ai/neural_network.py
# - training/trainer.py
# - persistence/checkpoint.py
#
# Each file has a clear role.
# This is a professional pattern called modular programming.

# ------------------------------------------------------
# 10) Exercise 1
# Create a module-like structure in your own mind:
# - game/car.py
# - game/road.py
# - main.py
# Then explain what each file would do.
# ------------------------------------------------------

# Example idea:
# - car.py: player and enemy cars
# - road.py: drawing the road and lane markings
# - main.py: runs the game loop and connects everything

# ------------------------------------------------------
# 11) Exercise 2
# Write a simple custom module in your head for a score system.
# ------------------------------------------------------

def add_points(score, points):
    return score + points


def subtract_life(lives):
    return lives - 1


print(add_points(100, 25))
print(subtract_life(3))

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - modules are Python files
# - imports bring in code from another file
# - project structure helps keep programs manageable
# - large projects are split into smaller files
# ------------------------------------------------------

print("\nLesson complete: modular code is the foundation of real software projects.")
