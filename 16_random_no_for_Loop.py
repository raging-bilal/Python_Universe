# Using a for-loop to create a list of random integers

import random

random_list=[]


for i in range(0,10):

    n=random.randint(0,50)

    random_list.append(n)


print("The random element in the list: ", random_list)