'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

# Just gonna copy the code for problem 7 and edit it a bit 

# This code can be optimised as you only have to check up to the sqrt(n) due to
# everything above sqrt(n) already being checked and sqrt(n) * sqrt(n) = n

import time

start_time = time.time()

max_value = 2_000_000
numbers = [True for x in range(max_value)]
counter = 2
primes = []

for x in range(2,max_value):
    if numbers[x] == False:
        pass
    while x*counter < max_value:
        numbers[x * counter] = False
        counter += 1
    counter = 2

for x in range(max_value):
    if numbers[x] == True:
        primes.append(x)

# This makes it so that the first prime is at index 1 and so on
primes.remove(0)

# This is an edit to the code in problem 7 as the order of the primes relative 
# to index is not important
primes.remove(1)
answer = 0

for x in primes:
    answer += x

print(answer)

end_time = time.time()

# For 1 x 10^7 it takes 30 seconds to compute. Only needed to go up to 200_000 
print(f"The time it took was {end_time - start_time} seconds")