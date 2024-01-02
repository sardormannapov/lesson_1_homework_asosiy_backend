inp = int(input("Enter number: "))
lst = [10, 7, 3, 5]
lst_two = []

def percent(input, massiv, massiv2):
    result = 1
    while input / 100 * result:
        input / 100 * result
        lst_two.append(result)
        print(massiv2)


percent(input=inp, massiv=lst, massiv2=lst_two)