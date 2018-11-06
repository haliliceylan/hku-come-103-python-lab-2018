pennies = int(input("Number of pennies: "))
nickels = int(input("Number of nickels: "))
dimes = int(input("Number of dimes: "))
quarters = int(input("Number of quarters: "))


total = pennies * 1 + nickels * 5 + dimes * 10 + quarters * 25

if(total == 100):
	print("Congrulations, the amount you entered is one dollar !")
elif(total < 100):
	print("Sorry, the amount you entered was less than one dollar")
else:
	print("Sorry, the amount you entered was greater than one dollar")