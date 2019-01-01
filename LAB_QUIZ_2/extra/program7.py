import math

# Bu betik extra olarak yazılmıştır. Lab Quizine Dahil Sorulardan Birisi Değildir.


def cordinate(x0, y0, v0, alpha, t):
    v0x = math.cos(math.radians(alpha)) * v0
    v0y = math.sin(math.radians(alpha)) * v0
    x = x0 + v0x * t
    y = y0 + v0y * t - 4.9 * t**2
    return x, y


def cordinates(x0, y0, v0, alpha, step_t):
    y = 0
    t = 0
    while y >= 0:
        x, y = cordinate(x0, y0, v0, alpha, t)
        yield (x, y)
        t += step_t


def main():
    print([x for x in cordinates(-500, 0, 75, 45, 0.01)])


if __name__ == "__main__":
    main()
