def main():
    file_variable = open('numbers.txt', 'r')
    total = 0
    line_number = 0
    x = file_variable.readline()
    while x != '':
        x = int(x)
        total += x
        line_number += 1
        x = file_variable.readline()

    print("Average is:", total/line_number)


main()
