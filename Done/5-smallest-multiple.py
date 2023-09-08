''' 
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
'''

# This solution fucking sucks but is done 
'''I previously had a solution where you would take the top half of the list of
numbers and do some funky maths shit with it'''

n = 20
count = 1

checkValues = [x for x in range(n//2,n+1)]

while True:
    if all(count % x == 0 for x in checkValues):
        print("Answer is {}".format(count))
        break
    count +=1
