file_variable = open('random_numbers.txt', 'r')
x = file_variable.readline()
even = 0
odd = 0
total = 0
while x != '':
    if(int(x) % 2 == 0):
        even += 1
    else:
        odd += 1
    total += int(x)
    x = file_variable.readline()
print('Even count:', even)
print('Odd count:', odd)
print('Total:', total)
