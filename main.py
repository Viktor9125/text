text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for symbol in punctuation:
    text = text.replace(symbol, '')

words = text.split()
# print(words)
words_dict = {}
different_word = 0
for word in words:
    if word not in words_dict:
        words_dict[word] = 0
        different_word += 1
    words_dict[word] += 1
print(f"Количество разных слов - {different_word}", )
# for word in words_dict.keys():
#     print(f'{word} - {words_dict[word]}')
print("Частота слов")
for word, frequency in words_dict.items():
    print(f"{word} - {frequency}")
