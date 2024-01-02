n = int(input("Enter number: "))

def daraja(num):
    if num > 1023 and num < 2048:
        print("10 1024")

    elif num > 511 and num < 1024:
        print("9 512")

    elif num > 255 and num < 512:
        print("8 256")

    elif num > 127 and num < 256:
        print("7 128")

    elif num > 63 and num < 127:
        print("6 64")

    elif num > 2**5 and num < 2**6:
        print("5 32")

    elif num > 15 and num < 33:
        print("4 16")

    elif num > 7 and num < 16:
        print("3 8")

    elif num < 8 and num > 3:
        print("2 4")

    else:
        print("Превышено")


daraja(num=n)