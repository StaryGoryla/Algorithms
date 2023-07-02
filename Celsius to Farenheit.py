def c_to_f_conversion(cel):
    try:
        cel = float(cel)
        far = cel * 9 / 5 + 32
        return far
    except ValueError:
        print(f"{cel} nie jest liczbą całkowitą")
        exit()


user_input = input("Podaj temperaturę w C: ")
far = c_to_f_conversion(user_input)
print(f"{user_input} stopni C to {far} stopni F.")