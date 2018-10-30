number = int(input("Enter how much money to be withdrawn: "))

hundred = number // 100
number = number % 100
fifty = number // 50
number = number % 50
twenty = number // 20
number = number % 20
tens = number // 10
number = number % 10
ones = number

print("100s:\t",hundred)
print("50s:\t",fifty)
print("20s:\t",twenty)
print("10s:\t",tens)
print("1s:\t",ones)