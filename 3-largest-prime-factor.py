'''The prime factors of 13195 are 5,7,13 and 29

What is the largest prime facor of the number 600851475143'''

toFactor = 13195
factorsOfToFactor = []

def isPrime(toCheck):
    for x in range(2,toCheck):
        if toCheck%x == 0:
            return False
    return True

def findFactor(toFactor):
    currentCheckValue = 1
    while True:
        currentCheckValue+=1
        
        if toFactor % currentCheckValue == 0:
            factorsOfToFactor.append(currentCheckValue)
            toFactor = toFactor / currentCheckValue
            currentCheckValue = 1
        
        if toFactor == 1:
            return

def checkFactors(factors):
    largestFactor = 0

    for x in range(len(factors)):
        if isPrime(factors[x]):
            if factors[x] > largestFactor:
                largestFactor = factors[x]
    
    print(largestFactor)

findFactor(toFactor)
checkFactors(factorsOfToFactor)

# This is dogshit slow like ngl
'''
def firstAlgo():
    for x in range(1,toFactor//2):
        if toFactor%x == 0:
            factorsOfToFactor.append(x)

    for x in range(len(factorsOfToFactor)):
        toCheck = factorsOfToFactor[len(factorsOfToFactor) - x - 1]
        found = isPrime(toCheck)
        if found:
            largestFactor = toCheck
            break

    print(largestFactor)
'''