x = int(input("Enter number: "))
y = int(input("Enter again number: "))

def kilometres(x, y):
    day = 1
    while y > x:
        x *= 1.1
        day += 1
    print(day)


kilometres(x=x, y=y)