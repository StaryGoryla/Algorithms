def list_sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + list_sum(list[1:])


list2 = []
wrongs = []
user_input = input("Podaj liczbę liczb oddzielonych przecinkiem: ").split(",")
for x in user_input:
    try:
        list2.append(float(x))
    except ValueError:
        wrongs.append(x)
result = list_sum(list2)
wrongs = ", ".join(str(x) for x in wrongs)
print(f"Suma liczb z listy to {result}")
if len(wrongs) > 0:
    print(f"{wrongs} nie są liczbami i nie zostały wzięte pod uwagę.")