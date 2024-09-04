'''
Boy or girl paradox (question 1).

Mr. Jones has two children. The older child is a girl. 
What is the probability that both children are girls?

Answer: 1/2
'''
import numpy as np

NUMBER_OF_SIMULATIONS = 1_000_000
number_of_favorable_outcomes = 0

np.random.seed(0)

i = 0
while i < NUMBER_OF_SIMULATIONS:
    print(f"Simulation {i + 1}/{NUMBER_OF_SIMULATIONS}")

    # Array with Mr. Jones' children, sorted by ascending age
    sorted_children = [None, None]
    # The older child is always a girl
    sorted_children[1] = 'girl'
    # The younger child can either be a boy or a girl, with a 50-50 chance
    sorted_children[0] = 'boy' if np.random.choice([0, 1]) else 'girl'

    # If also the younger children is a girl, the outcome is favorable
    if sorted_children[0] == 'girl':
        number_of_favorable_outcomes += 1

    i += 1

print(f"Estimated probability: {
      number_of_favorable_outcomes/NUMBER_OF_SIMULATIONS}")
