import collections
import string
text_file = open("text.txt")

#most common letter
def common_letter(text_file):
    # print collections.Counter(text_file.read())
    return max(collections.Counter(text_file.read()))

#line count
def line_count(text_file):
    count = 0
    with open("text.txt")as f:
        for line in f:
            count+=1
    return count

#whitespace delimited word count
def word_count(text_file):
    total = 0
    for line in open("text.txt"):
        total += len(line.split())
    return total

#average number of letters per word (to one decimal place)
def average_word_length(text_file):
    with open('text.txt') as f:
        number = sum(collections.Counter(letter for line in f
                  for letter in line.lower()
                  if letter in string.ascii_lowercase).values())/word_count(text_file)
        return round(number, 1)

print common_letter(text_file)
print line_count(text_file)
print word_count(text_file)
print average_word_length(text_file)

text_file.close()
