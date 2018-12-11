def getPentagonalNumber(n):
    return n*(3*n - 1)//2


def main():
    for x in range(1, 21):
        print(getPentagonalNumber(x), end=" ")
        if x % 5 == 0:
            print("")
    print("")


if __name__ == "__main__":
    main()
    pass
