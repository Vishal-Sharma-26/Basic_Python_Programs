def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print(CI)


principal = int(input("Enter Principal: "))
rate = int(input("Enter Rate: "))
time = int(input("Enter Time: "))

compound_interest(principal, rate, time)
