def factorial(integer):
    result = 1
    integer = isinteger(integer)
    if integer >= 0:
        for x in range(1, integer + 1):
            result = result * x
    else:
        print("Nie można silniować liczb ujemnych")
        exit()
    return result


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