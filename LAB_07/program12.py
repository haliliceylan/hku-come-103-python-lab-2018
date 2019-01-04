amount = int(input("amount: "))
print("Year", "\t", "Tuttion Amount")
for x in range(1, 6):
    print(x, "\t", format(amount, '.2f'))
    amount = amount * ((100 + 3*x)/100)
