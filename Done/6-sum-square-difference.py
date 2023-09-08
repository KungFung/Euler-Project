'''The sum of the squares of the first ten natural numbers is,
    1^2 + 2^" + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is,
    (1+2+3+...+10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.'''

# The second one can be done in O(1) due to sum of arithmetic sequence

limit = 100

def squareOfSum(limit):
    #n/2 [ 2 a + ( n − 1 ) d ]
    sum = (limit/2) * (2 + (limit - 1))
    
    answer = sum ** 2
    return answer

def sumOfSquares(limit):
    total = 0
    for x in range(limit + 1):
        total += x**2
    return total

print("The difference between the sum of the squares of the first one hundred",
      "natural numbers and the square of the sum is")
print(squareOfSum(limit) - sumOfSquares(limit))

