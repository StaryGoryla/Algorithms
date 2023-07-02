def palindrom_check(word):
        try:
            word = str(word)
            if word.isalpha():
                word_list = [char for char in word]
                word_list2 = []
                for char in range(len(word) -1, -1, -1):
                    word_list2.append(word_list[char])
                if word_list == word_list2:
                    print(f"{word} jest palindromem.")
                else:
                    print(f"{word} nie jest palindromem.")
            else:
                print("To nie jest słowo")
        except ValueError:
            print("To nie jest słowo")

user_input = input("Podaj słowo: ")
palindrom_check(user_input)