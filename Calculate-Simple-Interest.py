def simple_interest():
    p = int(input("Enter Principal: "))
    r = int(input("Enter Rate: "))
    t = int(input("Enter Time"))

    SI = (p*r*t)/10
    print(SI)
simple_interest()