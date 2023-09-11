# What is the 10001st prime

# maybe sive of eristostines

#This sucks in terms of efficiency
'''
def inefficient():
    numbers = [x for x in range(2,100)]

    for x in range(len(numbers)):
        for y in range(x + 1,len(numbers)):
            if numbers[y] == 0 or numbers[x] == 0:
                pass
            elif numbers[y] % numbers[x] == 0:
                numbers[y] = 0

    print(numbers)

inefficient()
'''

max_value = 10_000_000
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

print(primes[10001])