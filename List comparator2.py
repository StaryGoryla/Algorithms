def unique_elements(list1, list2):
    finals = []
    uniques = []
    wrongs = []
    list1 = list1.split(",")
    list2 = list2.split(",")
    uniques = [x for x in list1 if x not in list2]
    for x in list2:
        if x not in list1:
            uniques.append(x)
    for x in uniques:
        try:
            x = float(x)
            finals.append(x)
        except ValueError:
            wrongs.append(x)
    return finals, wrongs


user_input1 = input("Podaj listę liczb oddzielonych przecinkiem: ")
user_input2 = input("Podaj drugą listę liczb oddzielonych przecinkiem: ")
finals, wrongs = unique_elements(user_input1, user_input2)
finals = ', '.join(str(x) for x in finals)
wrongs = ", ".join(str(x) for x in wrongs)
print(f"Unikalne liczby to {finals}; elementy {wrongs} nie są liczbami i nie zostały wzięte pod uwagę.")