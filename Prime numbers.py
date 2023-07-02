number = input("Podaj liczbę całkowitą: ")
i = 2
x = 0
try:
    number = int(number)
except ValueError:
    print("To nie jest liczba całkowita")
    exit()


if number < 2:
    print(f"{number} nie jest liczbą pierwszą")
    exit()

is_prime = True

while i < number:
    if number % i == 0:
        is_prime = False
    i += 1
if is_prime:
    print(f"{number} jest pierwsza.")
else:
    print(f"{number} nie jest pierwsza.")