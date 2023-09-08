'''A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 91 x 99 = 9009.

Find the largest palindrome made from the product of two 3-digit numbers.'''

largest = 0

def checkPalindrome(value):
    value = str(value)
    for x in range(3):

        if value[x] != value[-(x+1)]:
            return False
    
    return True

for x in range(999,99,-1):
    for y in range(999,99,-1):
        product = x*y
        if checkPalindrome(product):
            if product > largest:
                largest = product

print(largest)

