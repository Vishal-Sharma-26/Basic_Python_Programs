count = 0

str = input("Enter your string: ")
char = input("Which character you find: ")

for i in str:
    if i == char:
        count += 1
print(count)