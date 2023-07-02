def isnotstring(x):
    try:
        x = float(x)
    except ValueError:
        print(f"{x} nie jest liczbą")
        exit()
    return x


def insertion_sort(list):

     for i in range(1, len(list)):
        key = list[i]
        h = i - 1
        while h >= 0 and key < list[h]:
            list[h + 1] = list[h]
            list[h] = key
            h -= 1
        list[h + 1] = key
     return list


user_input = input("Podaj ciąg liczb oddzielonych przecinkiem: ").split(",")
for i in user_input:
    isnotstring(i)
list = insertion_sort(user_input)
print(list)