# Suppose that three random numbers are generated.
# a) Determine the probability that the numbers are in decreasing order using a Monte Carlo simulation

import random

n = 1000
random_numers = [0, 0 , 0]
count = 0

for _ in range(0, n):
    for i in range(0, 3):
        random_numers[i] = random.randint(1,100)

    if random_numers[0] > random_numers[1] > random_numers[2]:
        count += 1

print("Value of counter: " + str(count))
print("Probability that number are decreasing: " + str(round(count / n, 2)))
print("Percentage that number are decreasing: " + str(round(n / count, 2)))