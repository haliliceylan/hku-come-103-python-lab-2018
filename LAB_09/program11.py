import random


def printQuestion(no):
    print("Question " + str(no))
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    print(str(x1) + " + " + str(x2) + " = _____")


def main():
    for x in range(5):
        printQuestion(x+1)


if __name__ == "__main__":
    main()
    pass
