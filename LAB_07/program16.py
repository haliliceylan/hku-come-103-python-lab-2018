for n in range(10000, 100001, 10000):
    pi = 0
    for x in range(1, n+1):
        pi += (-1)**(x+1)/(2*x-1)
    print("for n =", n)
    print("Pi is", pi)
