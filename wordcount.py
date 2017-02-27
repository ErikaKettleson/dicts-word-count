# put your code here.

text_file = open("test.txt")

word_count = {}

for line in text_file:
    stripped_line = line.rstrip()
    words = stripped_line.split(" ")


    print words

text_file.close()
