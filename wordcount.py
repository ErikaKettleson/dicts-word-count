# put your code here.

text_file = open("test.txt")

word_count = {}

for line in text_file:
    stripped_line = line.rstrip()
    words = stripped_line.split(" ")
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

for word in word_count:
    print word, word_count[word]

text_file.close()
