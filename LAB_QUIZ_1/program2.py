def root1(a, b, c):
    return (-b + (b**2 - 4*a*c)**0.5)/2*a


def root2(a, b, c):
    return (+b + (b**2 - 4*a*c)**0.5)/2*a


def discrimant(a, b, c):
    return b**2 - 4*a*c


def main():
    a = float(input('Enter a:'))
    b = float(input('Enter b:'))
    c = float(input('Enter c:'))
    if discrimant(a, b, c) > 0:
        print("x1:", root1(a, b, c))
        print("x2:", root2(a, b, c))
    elif discrimant(a, b, c) == 0:
        print("x1-x2:", root1(a, b, c))
    else:
        print("No Real Root")


if __name__ == "__main__":
    main()
