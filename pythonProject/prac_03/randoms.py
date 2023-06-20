
import random
print(random.randint(5, 20))  # line 1

#There are several iterations and all return a single digit at atime
#smallest number was 5
#largest number was 20


print(random.randrange(3, 10, 2))  # line 2
#There are several iterations and all return a single digit at atime
#smallest number was 3
#largest number was 9
#Yes, Line 2 produced a 4


print(random.uniform(2.5, 5.5))  # line 3
#smallest number was 2.7
#largest number was 5.3876



random_number = random.randint(1, 100)
print(random_number)