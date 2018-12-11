
def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True

    for y in range(2, x):
        if(x % y == 0):
            return False
    return True


def main():
    for x in range(1, 101):
        if is_prime(x):
            print(x)


if __name__ == "__main__":
    main()
    pass
