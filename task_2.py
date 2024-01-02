lst = [1, 2, 3, 3, 2, 1, 6, -1, 5, 6, 5]
lst_two = []

def search(massiv, massiv_two):
    result = 0
    for num in massiv:
        result ^= num
    lst_two.append(result)
    print(massiv_two)


search(massiv=lst, massiv_two=lst_two)