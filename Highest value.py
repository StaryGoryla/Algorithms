input = input("Podaj liczby oddzielone przecinkiem i spacją: ")
numbers = input.split(", ")
numbers2 = []
for value in numbers:
    try:
        value = float(value)
        numbers2.append(value)
    except ValueError:
        print(f"{value} nie jest liczbą")
try:
    print(f"Najwyższa wartość to {max(numbers2)}")
    print(f"Suma to {sum(numbers2)}")
except ValueError:
    print("Nie podano żadnych liczb")
