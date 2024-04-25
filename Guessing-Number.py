lst = [12, 26, 24, 18, 15]

while True:
    n = int(input("Enter your number: "))
    if n in lst:
        print("You guess the right number")
        break
    else:
        print("try again!!")
        continue
