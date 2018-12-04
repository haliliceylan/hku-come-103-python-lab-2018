A_SEAT_COST = 20
B_SEAT_COST = 15
C_SEAT_COST = 10


def showIncome(a_amount, b_amount, c_amount):
    a_total = a_amount * A_SEAT_COST
    b_total = b_amount * B_SEAT_COST
    c_total = c_amount * C_SEAT_COST
    print("Income from class A seats: $", a_total, sep='')
    print("Income from class B seats: $", b_total, sep='')
    print("Income from class C seats: $", c_total, sep='')
    print("Total Income: $", a_total+b_total+c_total, sep='')


def main():
    a_amount = int(input("Enter count of A seats: "))
    b_amount = int(input("Enter count of B seats: "))
    c_amount = int(input("Enter count of C seats: "))
    showIncome(a_amount, b_amount, c_amount)


main()
