"""
Python Lesson 7: Debugging and Testing

Programs do not always work perfectly the first time.
This lesson teaches how to find and fix mistakes.

We will learn:
- print debugging
- exceptions
- try / except
- assertions
- basic testing with pytest
"""

# ------------------------------------------------------
# 1) Print debugging
# ------------------------------------------------------
print("Debugging example:")
number = 10
print("Before calculation, number is:", number)
number = number + 5
print("After calculation, number is:", number)

# Printing values helps us understand what the program is doing.

# ------------------------------------------------------
# 2) Exceptions
# ------------------------------------------------------
print("\nExceptions:")

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Exceptions happen when Python cannot do something valid.
# We catch them with try/except.

# ------------------------------------------------------
# 3) Using input safely
# ------------------------------------------------------
# This is useful for preventing crashes.
try:
    user_input = int(input("Enter a number: "))
    print("You entered:", user_input)
except ValueError:
    print("That is not a valid integer.")

# ------------------------------------------------------
# 4) Assertions
# ------------------------------------------------------
print("\nAssertions:")
assert 5 + 5 == 10
print("The math assertion passed.")

# assert checks a condition.
# If it is false, the program stops with an error.

# ------------------------------------------------------
# 5) Function with validation
# ------------------------------------------------------
def divide(a, b):
    if b == 0:
        raise ValueError("The second value cannot be zero.")
    return a / b


try:
    print(divide(10, 2))
    print(divide(10, 0))
except ValueError as error:
    print("Error:", error)

# ------------------------------------------------------
# 6) Bug example: wrong logic
# ------------------------------------------------------
print("\nBug example:")
def calculate_total(price, tax_rate):
    # This version is wrong on purpose.
    total = price + tax_rate
    return total

print(calculate_total(100, 0.2))

# A common bug is that we forgot to multiply by the price.
# Real debugging means checking logic, not just syntax.

# ------------------------------------------------------
# 7) Correct version
# ------------------------------------------------------
def correct_total(price, tax_rate):
    return price * (1 + tax_rate)

print(correct_total(100, 0.2))

# ------------------------------------------------------
# 8) Testing with pytest (basic)
# ------------------------------------------------------
# We can write tests like this:
#
# def test_addition():
#     assert 2 + 2 == 4
#
# def test_division():
#     assert 10 / 2 == 5
#
# Then run: pytest
#
# Pytest checks whether our code behaves as expected.

# ------------------------------------------------------
# Exercise 1
# Write a function called is_positive(number) that returns True if the number is > 0.
# ------------------------------------------------------

def is_positive(number):
    return number > 0


print(is_positive(5))
print(is_positive(-2))

# ------------------------------------------------------
# Exercise 2
# Write a function that safely converts a string to an integer.
# ------------------------------------------------------

def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None


print(safe_int("42"))
print(safe_int("abc"))

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - how to debug code using print
# - how to catch errors with try/except
# - how assertions help check logic
# - how pytest helps test functions
# ------------------------------------------------------

print("\nLesson complete: debugging and testing are essential for real software.")
