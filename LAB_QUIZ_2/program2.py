def roots(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**0.5) / 2*a
    x2 = (-b - (b**2 - 4*a*c)**0.5) / 2*a
    return (x1, x2)


def is_any_root(a, b, c):
    return (b**2 - 4*a*c) >= 0


def main():
    a = float(input('Enter a:'))
    b = float(input('Enter b:'))
    c = float(input('Enter c:'))
    if(is_any_root(a, b, c)):
        my_roots = roots(a, b, c)
        if(my_roots[0] != my_roots[1]):
            print("The roots are", my_roots[0], my_roots[1])
        else:
            print("The root is", my_roots[0])
    else:
        print("The equation has no real roots.")


if __name__ == "__main__":
    main()
