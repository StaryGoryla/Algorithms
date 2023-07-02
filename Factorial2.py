def factorial(x):
    x = isinteger(x)
    if x >= 0:
        if x < 2:
            return 1
        else:
            return x * factorial(x - 1)
    else:
        print("Nie można silniować liczb ujemnych")
        exit()


def isinteger(x):
    try:
        x = int(x)
    except ValueError:
        print(f"{x} nie jest liczbą całkowitą")
        exit()
    return x


user_input = input("Podaj liczbę całkowitą: ")
result = factorial(user_input)
print(result)