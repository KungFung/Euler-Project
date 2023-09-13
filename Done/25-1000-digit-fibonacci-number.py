'''
The Fibonacci sequence is defined by the recurrence relation:
F_n = F_{n - 1} + F_{n - 2}, where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_{10} = 55
F_{11} = 89
F_{12} = 144

The 12th term, F_{12}, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

'''
Could try to implement Binet's formula so its more efficient for larger values
of n. Stack exchange also has an interesting point.
https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
https://codereview.stackexchange.com/questions/224518/project-euler-25-the-1000-digit-fibonacci-index
'''

x = 1
y = 1
z = 0

# Have to set to 1 as when the loop starts it skips straight to 1,2,3,5,8,... 
# and therefore misses 1,1,...

count = 1

while True:
    z = x+y
    x = y
    y = z
    count += 1

    if len(str(x)) == 1000:
        print(x)
        print(count)
        break
