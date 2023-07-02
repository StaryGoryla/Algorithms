def isinteger(x):
    try:
        x = int(x)
    except ValueError:
        print(f"{x} nie jest liczbą całkowitą")
        exit()
    return x


def fibonacci(n):
    if n <= 0:
        print("N musi być liczbą dodatnią.")
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


user_input = input("Podaj całkowitą liczbę dodatnią: ")
user_input = isinteger(user_input)
result = fibonacci(user_input)
print(result)