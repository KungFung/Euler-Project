'''
A Pythagorean triplet is a set of three natural numbers, a < b <  c, for which,
a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

'''
Explination from Addison (this is why he is the GOAT)

Say you have a tripple thats like:

3 |\ 5  3,4,5 Traingle
  |_\ 4

Then if you were to double it then that would also be a valid pythagorian triple
so 6,8,10 works.

Therefore we need to find a pythagorean triple which sums to a number that is a
factor of 1000. An the example he found was 8,15 and 17 which sum to 40.

1000 / 40 = 25

so the value of abc would be (8 * 25) * (15 * 25) * (17 * 25) = 31875000
'''