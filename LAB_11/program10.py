import random
counts = [0] * 10
for x in range(1000):
    counts[random.randint(0, 9)] += 1


for x in range(len(counts)):
    print(x, "count:", counts[x])
