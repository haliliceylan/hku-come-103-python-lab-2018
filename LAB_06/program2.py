speed = int(input("What is the speed of he vehicle in mph? "))
time = int(input("How many hours has it traveled? "))

print("Hour", "\t", "Distance-Traveled")

for x in range(time):
    print(x+1, "\t", format(speed*x, "10.2f"))
