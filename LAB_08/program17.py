import random

tails_count = 0
heads_count = 0


def simulate():
    global tails_count, heads_count
    if random.randint(1, 2) == 1:
        heads_count += 1
    else:
        tails_count += 1


def output():
    global tails_count, heads_count
    print(format("TAILS COUNT", "<10s"), format("HEADS COUNT", "<10s"))
    print(format(tails_count, "<10d"), format(heads_count, "<10d"))


for x in range(10000):
    simulate()

output()
