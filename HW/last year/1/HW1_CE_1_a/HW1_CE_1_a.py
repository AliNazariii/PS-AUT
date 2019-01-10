import random

number_of_experiment = 10
exp1_n = 0
exp1_f = 0
a = b = None
while number_of_experiment != 0:
   a = random.randrange(2)
   b = random.randrange(2)
   if a == 1:
       number_of_experiment = number_of_experiment - 1
       exp1_n = exp1_n + 1
       if b == 1:
           exp1_f = exp1_f + 1
print(exp1_f/exp1_n)