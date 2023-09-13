'''
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order.

The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

'''
Notes

There are 10! possible options as for 0,1,2 there are 3! options

There are (n-1)! number of options that start with 0,1,2,3,...
as shown by 0,1,2 with there being 2! options that start with 0,1,2.
This can also be if there are 6 options then 1/6 (5!) will start with 0,1,2,...

9! = 362,880
2 x 9! = 725,760
3 x 9! = 1,088,640

So the answer is between numbers starting with 1 and 2. 
This limits my search to only 9! options.

Of the 9! options there will be 8! options that start with 01, 02, ...

8! = 40,320

So all the values that start with 01 is within the band of 362,880 - 403,200 
Therefore all the values that start with 10 are between 725,760 - 766,080 
'''