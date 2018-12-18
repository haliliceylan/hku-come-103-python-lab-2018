import random

file_variable = open('random_numbers.txt', 'w')
for x in range(random.randint(1, 10)):
    file_variable.write(str(random.randint(1, 100)) + "\n")
file_variable.close()
