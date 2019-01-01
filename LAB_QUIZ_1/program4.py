file_name = input('Enter a filename: ')
my_ints = list()
file_object = open(file_name, 'r')

for line in file_object:
    line = int(line)
    my_ints += [line]

print("There are", len(my_ints), "scores preocessed from", file_name)
print("The total is", sum(my_ints))
print("The average is", (sum(my_ints)/len(my_ints)))
