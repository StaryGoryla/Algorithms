def longest_word(sentence):
    try:
        sentence = sentence.split()
        length_list = [len(word) for word in sentence]
        max_length = max(length_list)
        longest_words = [word for word in sentence if len(word) == max_length]
        print(f"Najdłuższe słowo to {', '.join(longest_words)}")
    except ValueError:
        print("Niepoprawne zdanie.")


user_input = input("Podaj zdanie: ")
longest_word(user_input)