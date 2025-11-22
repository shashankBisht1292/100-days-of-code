#Random module
import random

random_int = random.randint(1,10)
print(random_int)

random_float = random.random() * 10
print(random_float)
random_float_two = random.uniform(1, 10)
print(random_float_two)

#PAUSE 1 - Heads or Tails
if random.randint(1,2) == 2:
    print("Heads")
else:
    print("Tails")

states_of_america = ['delaware', 'Pennsylvania']
states_of_america[1] = "pencilvania"

states_of_america.append('chicago')

states_of_america.extend(['Angel land', 'New York', 'Kentucky'])
print(states_of_america)

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random
random_index = random.randint(0, len(friends)-1)

print(friends[random_index])

print(random.choice(friends))

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
