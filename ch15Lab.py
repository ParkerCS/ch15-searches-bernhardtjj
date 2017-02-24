"""
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
"""

import re


# This function takes in a file of text and returns
# a list of words in the file.
def split_file(file):
    return [x for line in file for x in re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line.strip())]


dict_words = split_file(open("dictionary.txt"))


def split_file(file):  # this returns it in lines
    return [re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line.strip()) for line in file]


alice = split_file(open("AliceInWonderLand200.txt"))

print("--- Linear Search ---")

for n in range(len(alice)):
    for word in alice[n]:
        i = 0
        while i < len(dict_words) and dict_words[i] != word.upper():
            i += 1

        if i >= len(dict_words):
            print("Line", n + 1, "possible misspelled word:", word)

print("--- Binary Search ---")

for i in range(len(alice)):
    for word in alice[i]:
        lower_bound = 0
        upper_bound = len(dict_words) - 1
        found = False
        while lower_bound <= upper_bound and not found:
            target = (lower_bound + upper_bound) // 2
            if dict_words[target] < word.upper():
                lower_bound = target + 1
            elif dict_words[target] > word.upper():
                upper_bound = target - 1
            else:
                found = True

        if not found:
            print("Line", i + 1, "possible misspelled word:", word)
