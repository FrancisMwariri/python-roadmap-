"""
Python Lesson 5: Object-Oriented Programming (OOP)

OOP is a way of organizing code around "objects".

Objects can model real things like:
- cars
- players
- enemies
- roads
- traffic lights

Key ideas:
- class
- object / instance
- attribute
- method
- __init__
- self
"""

# ------------------------------------------------------
# 1) A basic class
# ------------------------------------------------------
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} is now moving at {self.speed} km/h.")

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"{self.brand} slowed down to {self.speed} km/h.")


# Create objects from the class
car1 = Car("Toyota", "blue")
car2 = Car("Honda", "red")

print(car1.brand)
print(car2.color)

car1.accelerate(30)
car2.accelerate(50)
car1.brake(10)

# ------------------------------------------------------
# 2) A Player class
# ------------------------------------------------------
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.score = 0

    def gain_score(self, points):
        self.score += points
        print(f"{self.name} gained {points} points.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage.")


player = Player("Francis", 100)
print(player.name)
print(player.health)
player.gain_score(50)
player.take_damage(15)
print(player.health)

# ------------------------------------------------------
# 3) Why OOP matters in games
# ------------------------------------------------------
# In games, each object has its own state and actions:
# - player car has position, speed, color
# - enemy has chase behavior
# - road has boundaries and lane markers
# - traffic has movement and collision checks

# ------------------------------------------------------
# 4) Class with more methods
# ------------------------------------------------------
class Enemy:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def chase(self, amount):
        self.distance += amount
        self.speed += 2
        print(f"{self.name} is chasing. Distance: {self.distance}, Speed: {self.speed}")


enemy = Enemy("Pursuer", 40)
enemy.chase(50)
enemy.chase(30)

# ------------------------------------------------------
# 5) A class with a return value
# ------------------------------------------------------
class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, amount):
        self.value += amount
        return self.value

    def multiply(self, amount):
        self.value *= amount
        return self.value


calc = Calculator(10)
print(calc.add(5))
print(calc.multiply(2))

# ------------------------------------------------------
# 6) A class representing a road
# ------------------------------------------------------
class Road:
    def __init__(self, width, lane_count):
        self.width = width
        self.lane_count = lane_count

    def describe(self):
        print(f"Road width: {self.width}, lanes: {self.lane_count}")


road = Road(540, 3)
road.describe()

# ------------------------------------------------------
# 7) Exercise 1: create a class called Dog
# ------------------------------------------------------
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")


dog = Dog("Buddy", 4)
dog.bark()

# ------------------------------------------------------
# 8) Exercise 2: create a class called Student
# ------------------------------------------------------
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def pass_exam(self):
        if self.grade >= 50:
            print(f"{self.name} passed the exam.")
        else:
            print(f"{self.name} failed the exam.")


student = Student("Francis", 82)
student.pass_exam()

# ------------------------------------------------------
# 9) Why this matches the repo
# ------------------------------------------------------
# The repo has classes like:
# - Car
# - Road
# - GameUI
# - HandGestureController
# - Population / Genome
#
# Each of those classes contains data and methods to perform actions.

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - classes define blueprints
# - objects are created from classes
# - attributes hold data
# - methods perform actions
# - OOP helps organize larger projects
# ------------------------------------------------------

print("\nLesson complete: OOP is how we model real game objects and systems.")
