'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used? 

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out
numbers is in compliance with British usage.
'''

'''
Think Tank

Need Words for 1,2,3,...,9
Need Words for 10,11,12,...,19
Need Words for 20,30,40,...

Any number > 20 will have two words i.e. twenty seven

Need words for and, hundred and thousand
'''

#For this case alone im just gonna consider numbers up to and including 1000

'''
Dummy code to set the dictionary
for x in range(101):
    print(f"{x}:")
'''
 
numbers_to_words = {
    0:0,
    1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4,
    10:3,
    11:6,
    12:6,
    13:8,
    14:8,
    15:7,
    16:7,
    17:9,
    18:8,
    19:8,
    20:6,
    30:6,
    40:5,
    50:5,
    60:5,
    70:7,
    80:6,
    90:6,
}
hundred  = 7
len_and = 3
thousand = 8
sum = 0

for x in range(1,1001):
    thousands = x // 1000
    hundreds = (x % 1000) // 100
    tens = (x % 100) // 10
    ones = x % 10

    if thousands == 1:
        sum += numbers_to_words[1] + thousand
    
    if hundreds > 0 and (tens > 0 or ones > 0):
        if tens == 1:
            sum += numbers_to_words[hundreds] + hundred + len_and + numbers_to_words[(tens * 10) + ones]
        else:
            sum += numbers_to_words[hundreds] + hundred + len_and + numbers_to_words[(tens * 10)] + numbers_to_words[ones]
    elif hundreds > 0:
        sum += numbers_to_words[hundreds] + hundred
    else:
        if x > 9 and x < 20:
            sum += numbers_to_words[(tens * 10) + ones]
        else:
            sum += numbers_to_words[tens * 10] + numbers_to_words[ones]

print(sum)
    
