'''
Bertrand's box paradox.

There are three boxes:
    - a box containing two gold coins,
    - a box containing two silver coins,
    - a box containing one gold coin and one silver coin.
Choose a box at random. From this box, withdraw one coin at random. 
If that happens to be a gold coin, then what is the probability that the next 
coin drawn from the same box is also a gold coin? 

Answer: 2/3
'''
import numpy as np

NUMBER_OF_SIMULATIONS = 1_000_000
number_of_favorable_outcomes = 0

np.random.seed(0)

i = 0
while i < NUMBER_OF_SIMULATIONS:
    print(f"Simulation {i + 1}/{NUMBER_OF_SIMULATIONS}")

    # Generate the boxes
    boxes = np.array([
        ['gold', 'silver'] if np.random.choice([0, 1]) else ['silver', 'gold'],
        ['gold', 'gold'],
        ['silver', 'silver']
    ])
    np.random.shuffle(boxes)

    # Choose a random box, then a random coin from the box
    box = boxes[np.random.choice(len(boxes))]
    coin = np.random.choice(box)

    # If the chosen coin is silver, try again (we are only interested in the
    # cases in which the first coin is gold)
    if coin != 'gold':
        continue

    # If the box contains two gold coins, the outcome is favorable
    if not 'silver' in box:
        number_of_favorable_outcomes += 1

    i += 1

print(f"Estimated probability: {
      number_of_favorable_outcomes/NUMBER_OF_SIMULATIONS}")
