
def repeat(word, repeat_number):
    for x in range(repeat_number):
        print(word, end="")


def main():
    word = input("Enter a string:")
    times = int(input("How many times?"))
    repeat(word, times)


main()
