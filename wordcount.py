# put your code here.

text_file = open("test.txt")

word_count = {}

for line in text_file:
    stripped_line = line.rstrip()
    words = stripped_line.split(" ")

    all_letter_words = []

    for word in words:
        if not word[-1].isalpha():
            all_letter_words.append(word[:-1])
        else:
            all_letter_words.append(word)

    for word in all_letter_words:
        word_count[word] = word_count.get(word, 0) + 1

for word in word_count:
    print word, word_count[word]

text_file.close()
