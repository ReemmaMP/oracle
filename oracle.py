import collections
import string
import re
filename = "text.txt"

#whitespace delimited word count
def word_count():
    text_file = open(filename)
    total = 0
    for line in text_file:
        total += len(line.split())
    text_file.close()
    return total

#line count
def line_count():
    text_file = open(filename)
    return text_file.read().count('\n') + 1

#average number of letters per word (to one decimal place)
def average_word_length():
    text_file = open(filename)
    line_array = text_file.read().split('\n')
    count, total = 0, 0
    for line in line_array:
        line.translate(None, string.punctuation)
        for word in line.split():
            if word != "":
              	total += len(word)
                count += 1
    text_file.close()
    return total / count

#most common letter
def common_letter():
    text_file = open(filename)
    file_content = re.sub('[^0-9a-zA-Z]+', '', text_file.read())
    letter_counter = collections.Counter(file_content)
    max_occ_number = max(letter_counter.values())
    max_occ_letters = []
    for letter in letter_counter:
      	if letter_counter[letter] == max_occ_number:
          		max_occ_letters.append(letter)
    text_file.close()
    return max_occ_letters

print "The whitespace delimited word count is: ", word_count()
print "The line count is: ", line_count()
print "The average number of letters per word (to 1 d.p.) is: ", "{0:.1f}".format(average_word_length())
print "The most common letter is: ", common_letter()
