def word_rotator(sentence):
   list = []
   back_list = []
   sum = ""
   for it in text:
      list.append(it)
   for number, element in enumerate(list):
      x = -number + len(text) - 1
      y = list[x]
      back_list.append(y)
   for it in back_list:
      sum += it
   return sum


text = input(">")
sum = word_rotator(text)
print(sum)