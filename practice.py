try:
    with open("1.txt") as a:
        print(a.read())

except FileNotFoundError:
    print("File does not exist")

try:
    with open("1.txt") as b:
        print(b.read())

except FileNotFoundError:
    print("File does not exist")

try:
    with open("1.txt") as c:
        print(c.read())

except FileNotFoundError:
    print("File does not exist")