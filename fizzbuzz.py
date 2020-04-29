import sys
import time

""" Despite the fact fizzbuzz has its origins as a group word game for children to teach them about division,
it is also one of the easiest and most used algorithm when it comes to job interviews.

The task is to output 100 numbers (n >= 100) and check n if its divisible by 3, 5 or both 3 and 5.
3 equals fizz, 5 equals buzz, while n divisible through 3 and 5 simultaneously.
n will actually be replaced will fizz, buzz or fizzbuzz, but I waive that in my example."""

"""The following code should be self-explanatory. Iterating through a list of numbers from 1 - 15 and checking each number
if its divisible by 3,5 or both."""

StartTime = time.time()

for number in range(1, 15):
    if number % 3 == 0 & number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
print(f'The script took this time {time.time() - StartTime} seconds!')

########################################################################################################################

"""But wait. Imagine we'd use some kind of complex array or list in this example while increasing the numbers from 1-15 to 1-1000.
The code would not only double check n each time if its divisible by 3 and 5, but also lose performance and fill up your RAM.
If n is divisible simultaneously by 3 and 5, it is also divisible by 15 - since 15 is a prime factorization of 3 multiplied by 5.

So, instead of double checking the number for 3 and 5, we just check it for the factor of 15.
If n is divisible by 15, it is also divisible by 3 and 5 - thus fizzbuzz."""

StartTime = time.time()

for number in range(1, 1000):
    if number % 15 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
print(f'The script took {time.time() - StartTime} seconds!')

###############################################################

"""It it also possible to use list comprehension for this example."""

StartTime = time.time()
print('\n '.join([(x % 3 < 1) * 'fizz' + (x % 5 < 1) * 'buzz' or str(x) for x in range(1, 1000)]))
print(f'The script took {time.time() - StartTime} seconds!')
