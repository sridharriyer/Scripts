import random
import os

#data = open(r"C:\Users\python\names.txt").readlines()
#print(random.choice(data))
#print(random.randint(20,50))


# phone number generator
phonenumber = ''
for i in range(0,10):
    if i == 0:
        phonenumber = str(random.randint(0,9))
    elif i == 3 or i == 6:
        phonenumber = phonenumber + '-' + str(random.randint(0,9))
    else:
        phonenumber = phonenumber + str(random.randint(0,9))

print(phonenumber)