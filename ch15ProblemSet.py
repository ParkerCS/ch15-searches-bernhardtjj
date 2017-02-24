"""
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
"""
import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(lin):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', lin)


# 1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

def find_longest(file):
    high_score = 0
    saved_words = []
    for line in file:
        line = line.strip()
        for word in split_line(line):
            if len(word) >= high_score:
                high_score = len(word)
                saved_words.append(word)
    file.close()
    print([i for i in saved_words if len(i) == high_score])


find_longest(open("AliceInWonderLand.txt"))
find_longest(open("dictionary.txt"))


# 2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"
def find_average_and_word_count(file):
    saved_words = []
    for line in file:
        line = line.strip()
        for word in split_line(line):
            saved_words.append(len(word))
    file.close()
    print("The word count is", len(saved_words), "and the avg word length is", sum(saved_words) / len(saved_words))


find_average_and_word_count(open("AliceInWonderLand.txt"))


# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

# 3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

def find_num_cat(file):
    high_score = "cheshire"
    low_score = "cat"
    chess_score = 0
    cat_score = 0
    both_score = 0
    last_word = ""
    for line in file:
        line = line.strip()
        for word in split_line(line):
            if word.lower() == high_score:
                chess_score += 1
            elif word.lower() == low_score:
                cat_score += 1
                if last_word == high_score:
                    both_score += 1
            last_word = word.lower()
    file.close()
    print("Cheshire is", chess_score, "times and Cat is", cat_score, "times and Cheshire Cat is", both_score, "times.")


# OR

# 3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

def find_frq(file):
    high_score = 7
    saved_words = []
    for line in file:
        line = line.strip()
        for word in split_line(line):
            if len(word) == high_score:
                saved_words.append(word)
    file.close()

    while len(saved_words) - 1:
        saved_words = [word for pos, word in enumerate(saved_words) if word in saved_words[:pos]]

    print("The most frequently occuring seven letter word is ``" + saved_words[0] + "''")


find_num_cat(open("AliceInWonderLand.txt"))
find_frq(open("AliceInWonderLand.txt"))

# Challenge problem (for fun).
# What words appear in the text of "Alice in Wonderland"
# that DO NOT occur in "Alice Through the Looking Glass".  Make a list.
# You can substitute this for any of the above problems.
# Read in a file from disk and put it in an array.
