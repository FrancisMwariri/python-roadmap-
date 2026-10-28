"""
Python Lesson 4: Data Structures

This lesson introduces the main ways to store many values in Python.

We will learn:
- lists
- tuples
- dictionaries
- sets
- when to use each one
"""

# ------------------------------------------------------
# 1) Lists
# ------------------------------------------------------
print("Lists:")
traffic_cars = ["Sedan", "Truck", "SUV", "Sport"]
print(traffic_cars)
print(traffic_cars[0])
print(traffic_cars[-1])

traffic_cars.append("Bus")
print(traffic_cars)

traffic_cars.remove("Truck")
print(traffic_cars)

# Lists are ordered and can change.
# They are extremely useful for storing collections.

# ------------------------------------------------------
# 2) List operations
# ------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# ------------------------------------------------------
# 3) Slicing
# ------------------------------------------------------
print("Slicing:")
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# ------------------------------------------------------
# 4) Tuples
# ------------------------------------------------------
print("\nTuples:")
player_position = (100, 200)
print(player_position)
print(player_position[0])

# Tuples are like lists, but they cannot be changed after creation.
# They are good when values should stay fixed.

# ------------------------------------------------------
# 5) Dictionaries
# ------------------------------------------------------
print("\nDictionaries:")
player = {
    "name": "Francis",
    "score": 1500,
    "level": 3,
    "alive": True,
}

print(player)
print(player["name"])
print(player["score"])

player["score"] = 2000
print(player)

player["lives"] = 3
print(player)

# Dictionaries store data as key-value pairs.
# They are great for game state, player info, settings, and objects.

# ------------------------------------------------------
# 6) Nested dictionaries
# ------------------------------------------------------
print("\nNested dictionaries:")
car = {
    "brand": "Toyota",
    "speed": 90,
    "color": "blue",
    "position": {"x": 250, "y": 500},
}

print(car["brand"])
print(car["position"]["x"])

# This is very similar to how games store lots of object data.

# ------------------------------------------------------
# 7) Sets
# ------------------------------------------------------
print("\nSets:")
unique_colors = {"red", "blue", "green", "red"}
print(unique_colors)

# Sets store unique values only.
# They are useful when you need to remove duplicates.

# ------------------------------------------------------
# 8) When to use which structure
# ------------------------------------------------------
print("\nStructure guide:")
print("List -> ordered, changable collection")
print("Tuple -> fixed ordered values")
print("Dictionary -> name/value pairs")
print("Set -> unique values only")

# ------------------------------------------------------
# 9) Real game example: player inventory
# ------------------------------------------------------
print("\nGame inventory example:")
inventory = ["keys", "coins", "battery"]
inventory.append("health pack")
print(inventory)

settings = {
    "volume": 80,
    "difficulty": "hard",
    "screen_width": 960,
}
print(settings["difficulty"])

# ------------------------------------------------------
# 10) Exercise 1: create a list of 5 favorite games
# ------------------------------------------------------
favorite_games = ["Need for Speed", "Mario Kart", "Forza", "Rocket League", "Trackmania"]
print(favorite_games)

# ------------------------------------------------------
# 11) Exercise 2: create a dictionary for a player
# ------------------------------------------------------
player = {
    "name": "Francis",
    "score": 500,
    "coins": 40,
    "level": 2,
}
print(player)

# ------------------------------------------------------
# 12) Exercise 3: use a set to remove duplicates
# ------------------------------------------------------
colors = ["red", "blue", "red", "green", "blue"]
unique_colors = set(colors)
print(unique_colors)

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - lists
# - tuples
# - dictionaries
# - sets
# - using the right structure for the right job
# ------------------------------------------------------

print("\nLesson complete: data structures help organize real-world information.")
