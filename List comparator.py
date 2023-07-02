def unique_elements(list1, list2):
    wrongs = []
    uniques = []
    list1 = list1.split(",")
    list2 = list2.split(",")

    floats1, wrongs1 = floats_wrongs(list1)
    floats2, wrongs2 = floats_wrongs(list2)

    wrongs.extend(wrongs1)
    wrongs.extend(wrongs2)

    for x in floats1:
        if x not in floats2:
            uniques.append(x)
    for x in floats2:
        if x not in floats1:
            uniques.append(x)
    return uniques, wrongs

def floats_wrongs(list):
    floats = []
    wrongs = []
    for x in list:
        try:
            floats.append(float(x))
        except ValueError:
            wrongs.append(x)
    return floats, wrongs


user_input1 = input("Podaj listę liczb oddzielonych przecinkiem: ")
user_input2 = input("Podaj drugą listę liczb oddzielonych przecinkiem: ")
uniques, wrongs = unique_elements(user_input1, user_input2)
uniques = ', '.join(str(x) for x in uniques)
wrongs = ", ".join(str(x) for x in wrongs)
print(f"Unikalne liczby to {uniques}; elementy {wrongs} nie są liczbami i nie zostały wzięte pod uwagę.")