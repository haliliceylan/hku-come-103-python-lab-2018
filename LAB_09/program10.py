
def pass_it(x, y):
    z = x*y
    result = get_result(z)
    return(result)


def get_result(number):
    z = number + 2
    return(z)


num1 = 3
num2 = 4
answer = pass_it(num1, num2)
print(answer)
