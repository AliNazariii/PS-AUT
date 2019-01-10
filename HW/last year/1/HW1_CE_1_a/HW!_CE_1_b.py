import random

number_of_experiment = 10
exp2_n = 0
exp2_f = 0
a = b = a_prime = b_prime = x = None
while number_of_experiment != 0:
   a = random.randrange(2)
   b = random.randrange(2)
   x = random.randrange(2)
   if x == 0:
       a_prime = a
       b_prime = b
   else:
       a_prime = b
       b_prime = a
   if a_prime == 1:
       number_of_experiment = number_of_experiment - 1
       exp2_n = exp2_n + 1
       if b_prime == 1:
           exp2_f = exp2_f + 1
print(exp2_f/exp2_n)