# put your code here.

def word_counter(text):
    """ function to print a list of words and their frequency in a file
    """

    text_file = open(text)

    word_count = {}

    for line in text_file:
        stripped_line = line.rstrip()
        words = stripped_line.split(" ")

        all_letter_words = []

        for word in words:
            word = word.lower()
            if not word[-1].isalpha():
                all_letter_words.append(word[:-1])
            else:
                all_letter_words.append(word)

        for word in all_letter_words:
            word_count[word] = word_count.get(word, 0) + 1

    # for word in word_count:
    #     print word, word_count[word]

    sorted_word_count = sorted(word_count)
    for word in sorted_word_count:
        print word, word_count[word]

    text_file.close()

word_counter("test.txt")
