

print("Minutes", "\t", "Calories Burned")
print("-"*33)
for x in range(5, 61, 5):
    print(format(x, "5d"), "\t", format(x*4.2, "18.2f"))
