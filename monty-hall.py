'''
Monty Hall problem.

In a game show, you are presented with three doors. Behind one of the doors is 
a car, and behind the other two doors are goats. You do not know what is behind
any of the doors, but Monty Hall, the host of the game, does. 

You start by choosing one door without opening it. Monty then opens another 
door, which has a goat behind it.

You are then given a choice: stick with your original choice, or switch to the 
remaining unopened door.

What is the probability of choosing the car if you switch door?

Answer: 2/3
'''
import numpy as np

NUMBER_OF_SIMULATIONS = 1_000_000
number_of_favorable_outcomes = 0

np.random.seed(0)
i = 0
while i < NUMBER_OF_SIMULATIONS:
    print(f"Simulation {i + 1}/{NUMBER_OF_SIMULATIONS}")

    # Generate the doors with prizes
    doors = np.array(['car', 'goat', 'goat'])
    np.random.shuffle(doors)

    # Choose an initial random door: 0, 1 or 2
    choice = np.random.choice(len(doors))

    # Select one of the remaining doors with a goat
    for door, prize in enumerate(doors):
        if door != choice and prize == 'goat':
            goat = door
            break

    # Change the choice to the remaining door
    for door, prize in enumerate(doors):
        if door != choice and door != goat:
            choice = door
            break

    # If the new choice contains the car, the outcome is favorable
    if doors[choice] == 'car':
        number_of_favorable_outcomes += 1

    i += 1

print(f"Estimated probability: {
      number_of_favorable_outcomes/NUMBER_OF_SIMULATIONS}")
