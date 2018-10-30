principal_amount = int(input("Enter the starting principal: "))
annual_interest_rate = int(input("Enter the annual interest rate: "))
annual_interest_rate = annual_interest_rate / 100
number_of_years = int(input("How many times per year is the interest compounded? "))
specified_numbers = int(input("For how many years will the account earn interest? "))
total = principal_amount * (1 + annual_interest_rate / number_of_years)**(number_of_years * specified_numbers)
print("At the end of",specified_numbers,"years you will have",format(total,".2f"),"$")