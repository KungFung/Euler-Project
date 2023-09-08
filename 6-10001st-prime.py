# What is the 10001st prime

# maybe sive of eristostines

#This sucks in terms of efficiency

def inefficient():
    numbers = [x for x in range(2,int(2e6))]

    for x in range(len(numbers)):
        for y in range(x + 1,len(numbers)):
            if numbers[y] == 0 or numbers[x] == 0:
                pass
            elif numbers[y] % numbers[x] == 0:
                numbers[y] = 0

    print(numbers)

inefficient()