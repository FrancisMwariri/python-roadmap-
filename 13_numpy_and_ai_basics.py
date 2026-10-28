"""
Python Lesson 13: NumPy and AI Basics

This lesson introduces NumPy and the basic idea behind neural networks.

We will learn:
- arrays
- vector math
- simple activation ideas
- how AI uses numbers to make decisions
"""

import numpy as np

# ------------------------------------------------------
# 1) NumPy arrays
# ------------------------------------------------------
print("NumPy arrays:")
array1 = np.array([1, 2, 3, 4])
print(array1)
print(array1.shape)

array2 = np.array([[1, 2], [3, 4]])
print(array2)
print(array2.shape)

# Arrays are just grids of numbers.
# Neural networks are built from arrays and matrix math.

# ------------------------------------------------------
# 2) Simple math with arrays
# ------------------------------------------------------
print("\nArray math:")
print(array1 + 2)
print(array1 * 3)
print(array1 + array1)

# ------------------------------------------------------
# 3) Dot product example
# ------------------------------------------------------
print("\nDot product:")
weights = np.array([0.5, 0.2, 0.3])
inputs = np.array([1.0, 2.0, 3.0])
print(np.dot(inputs, weights))

# Neural networks use lots of dot products.

# ------------------------------------------------------
# 4) One simple neuron
# ------------------------------------------------------
print("\nSimple neuron:")
weights = np.array([0.7, -0.4, 0.6])
inputs = np.array([1.0, 0.5, 2.0])
raw_value = np.dot(inputs, weights)
print("Raw value:", raw_value)

# Activation function example
# ReLU: max(0, value)
activation = max(0.0, raw_value)
print("Activated value:", activation)

# ------------------------------------------------------
# 5) A tiny neural network concept
# ------------------------------------------------------
# Input layer -> hidden layer -> output layer
# Each connection has a weight.
# The network computes output based on input and weights.

W1 = np.array([[0.5, -0.2], [0.3, 0.8]])
X = np.array([1.0, 2.0])

hidden = X @ W1
print("Hidden layer output:", hidden)

# ------------------------------------------------------
# 6) AI decision example
# ------------------------------------------------------
print("\nAI decision example:")
features = np.array([0.9, 0.1, 0.8])
weights = np.array([0.4, 0.3, 0.5])
score = np.dot(features, weights)
print("Decision score:", score)

if score > 0.6:
    print("AI chooses to move forward.")
else:
    print("AI chooses to wait.")

# ------------------------------------------------------
# 7) Why this matters for the repo
# ------------------------------------------------------
# The AI in this repo uses a small feed-forward neural network
# implemented in NumPy.
# It reads game features and decides how to steer the enemy car.

# ------------------------------------------------------
# Exercise
# Create a simple array of game features and a weight vector.
# Compute the final score using dot product.
# ------------------------------------------------------

game_features = np.array([10.0, 5.0, 3.0, 2.0])
weight_vector = np.array([0.2, 0.5, 0.8, 0.4])
final_score = np.dot(game_features, weight_vector)
print("Final score:", final_score)

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - NumPy arrays
# - dot products
# - basic decision-making math
# - how AI uses numbers to compute outputs
# ------------------------------------------------------

print("\nLesson complete: AI starts with math and arrays.")
