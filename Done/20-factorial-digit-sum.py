'''
n! means n * (n - 1) * ... * 3 * 2 * 1.
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of the digits
in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
'''

factorial_value = 1
digit_sum = 0
limit = 100

for i in range(1,limit + 1):
    factorial_value *= i

for j in range(len(str(factorial_value))):
    digit_sum += int(str(factorial_value)[j])

print(digit_sum)