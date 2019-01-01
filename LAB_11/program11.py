# I'm not sure to this answer
def gcd(numbers):
    for x in range(min(numbers), max(numbers)+1):
        for number in numbers:
            if number % x != 0:
                return x-1


a = gcd([36, 72, 18])
print(a)
