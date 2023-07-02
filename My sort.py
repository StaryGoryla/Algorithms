def latest_sort(list):
    list = list.split(",")
    list2 = []
    for number in list:
        number = isinteger(number)
        list2.append(number)
        if len(list2) > 1:
            i = len(list2) - 1
            while i > 0:
                h = i - 1
                if list2[i] < list2[h]:
                    list2[i], list2[h] = list2[h], list2[i]
                i -= 1
    return list2

def isinteger(x):
    try:
        x = int(x)
    except ValueError:
        print(f"{x} nie jest liczbą całkowitą")
        exit()
    return x


user_input = input("Podaj ciąg liczb oddzielonych przecinkiem: ")
list2 = latest_sort(user_input)
print(list2)
