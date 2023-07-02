def sum_maker(numbers):
    numbers = numbers.split(",")
    total = 0
    for number in numbers:
        try:
            number = float(number)
            total += number

        except ValueError:
            print(f"{number} to nie liczba")
    return total

user_input = input(f"Podaj liczby oddzielone przecinkiem: ")
total = sum_maker(user_input)
print(f"Suma tych liczb to {total}")