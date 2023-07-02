def isinteger(x):
    try:
        x = int(x)
    except ValueError:
        print(f"{x} nie jest liczbą całkowitą")
        exit()
    return x


def exp(x, n):
    if n == 1:
        return x
    return x * exp(x, n - 1)


user_input = input("Podaj liczbę potęgowaną: ")
user_input2 = input("Podaj stopień potęgi: ")
user_input = isinteger(user_input)
user_input2 = isinteger(user_input2)
exp = exp(user_input, user_input2)
print(exp)