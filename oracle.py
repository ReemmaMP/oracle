import collections
import string
import re
filename = "text.txt"

#most common letter
def common_letter():
    # print collections.Counter(text_file.read())
    # non ascii is replaced
    text_file = open(filename)
    file_content = re.sub('[^0-9a-zA-Z]+', '', text_file.read())
    letter_counter = collections.Counter(file_content)
    max_occurence_number = max(letter_counter.values())

    max_occ_letters = []
    for letter in letter_counter:
      	if letter_counter[letter] == max_occurence_number:
          		max_occ_letters.append(letter)
    text_file.close()
    return max_occ_letters

#line count
def line_count():
    text_file = open(filename)
    return text_file.read().count('\n') + 1

#whitespace delimited word count
def word_count():
    text_file = open(filename)
    total = 0
    for line in text_file:
        total += len(line.split())
    text_file.close()
    return total

#average number of letters per word (to one decimal place)
def average_word_length():
  	# gets each line in an array
    text_file = open(filename)
    line_array = text_file.read().split('\n')
    # initialise count and total
    count, total = 0, 0
    # iterate through each line
    for line in line_array:
      	# iterate through each words in the array
        # get rid of punctuations
        line.translate(None, string.punctuation)
        for word in line.split():
          	# here it could have "", since there could be two spaces together
            if word != "":
              	total += len(word)
                count += 1
    text_file.close()
    return total / count

print common_letter()
print line_count()
print word_count()
print "{0:.1f}".format(average_word_length())
