# Напишите программу, которая анализирует текст, введенный пользователем,
# и выполняет следующие действия:
#
# Подсчитывает количество слов в тексте.
# Определяет самое длинное слово в тексте.
# Подсчитывает количество гласных букв (а, е, ё, и, о, у, ы, э, ю, я) в тексте.
# Выводит количество раз, которое каждое слово встречается в тексте.
#
# Требования к программе:
# Используйте цикл for для итерации по словам в тексте.
# Программа должна игнорировать регистр букв (т.е. "А" и "а" считаются одинаковыми).
# Учтите возможность наличия знаков препинания в тексте (они не должны учитываться как часть слов).
# Найдите самое длинное слово. Если их несколько, выберите первое из них.
import string


def get_list_words_not_punctuation_and_lower(input_text):
    list_words = []
    for word in input_text.lower().split():
        list_words.append(word.translate(str.maketrans('', '',
                                                       string.punctuation)))
    return list_words


def get_word_count(list_clean_words):
    word_count = 0
    for _ in list_clean_words:
        word_count += 1
    return word_count


def get_counting_vowel_letters(list_clean_words):
    letters_count = 0
    vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    for word in list_clean_words:
        for letter in word:
            if letter in vowels:
                letters_count += 1
    return letters_count


def get_list_words_and_count(list_clean_words):
    list_words_and_count = []
    for uniq_word in set(list_clean_words):
        list_words_and_count.append([uniq_word, list_clean_words.count(uniq_word)])
    return list_words_and_count


input_text = input("Введите текст для анализа:\n")

list_clean_words = get_list_words_not_punctuation_and_lower(input_text)

print(f"\nКоличество слов в тексте - {get_word_count(list_clean_words)}")

longest_word = max(list_clean_words, key=len)
print(f"Самое первое длинное слово - \"{longest_word}\".")

print(f"Гласных букв - {get_counting_vowel_letters(list_clean_words)}.\n")

list_words_and_count = get_list_words_and_count(list_clean_words)
for word, count in list_words_and_count:
    print(f"Слово \"{word}\" встречается в тексте {count} раз(а).")
