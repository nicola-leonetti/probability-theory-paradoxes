'''
Boy or girl paradox (version 2).

Mr. Smith has two children. At least one of them is a boy. 
What is the probability that both children are boys?

Suppose 'at least of them is a boy' means 'From all families with two children, 
at least one of whom is a boy, a family is chosen at random'.

Answer: 1/3
'''
import numpy as np

NUMBER_OF_SIMULATIONS = 1_000_000
number_of_favorable_outcomes = 0

np.random.seed(0)

i = 0
while i < NUMBER_OF_SIMULATIONS:

    # Pick a random family
    sorted_children = [
        'boy' if np.random.choice([0, 1]) else 'girl',
        'boy' if np.random.choice([0, 1]) else 'girl'
    ]
    # Make sure at least a boy is in the family
    if not 'boy' in sorted_children:
        continue

    print(f"Simulation {i + 1}/{NUMBER_OF_SIMULATIONS}")

    # If both children are boys, the outcome is favorable
    if not 'girl' in sorted_children:
        number_of_favorable_outcomes += 1

    i += 1

print(f"Estimated probability: {
      number_of_favorable_outcomes/NUMBER_OF_SIMULATIONS}")
