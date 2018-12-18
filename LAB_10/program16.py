def main():
    file_name = input("Enter the file name:")

    file_variable = open(file_name, "r")

    line_number = 1
    x = file_variable.readline()
    while x != '':
        print(line_number, ":", x.rstrip("\n"))
        line_number += 1
        x = file_variable.readline()


main()
