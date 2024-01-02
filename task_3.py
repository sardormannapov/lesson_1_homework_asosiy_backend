inp = int(input("Enter number: "))
lst = [1, 3, 5, 4, 8, 10]

def app(input, msv):
    for num in msv:
        if input == num:
            lst.remove(num)
            lst.append(num)
            print(msv)
            break
    else:
        print("We don' have this number")


app(input=inp, msv=lst)