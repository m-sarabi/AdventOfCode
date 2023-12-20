"""
Short description:
Santa needs to find out which texts are naughty or nice.
A nice text is one with all the following properties:
- It contains at least three vowels
- It contains at least one letter that appears twice in a row
- It does not contain the strings ab, cd, pq, or xy

How many nice texts are there?
"""

import re


def count_nice_texts(input_file: str) -> int:
    """Count the number of nice texts in the given file.

    ----

    Example:
    ----
        - `ugknbfddgicrmopn` is nice because it has at least three vowels (`u...i...o...`),
          a double letter (`...dd...`), and none of the disallowed substrings.
        - `aaa` is nice because it has at least three vowels and a double letter,
          even though the letters used by different rules overlap.
        - `jchzalrnumimnmhp` is naughty because it has no double letter.
        - `haegwjzuvuyypxyu` is naughty because it contains the string `xy`.
        - `dvszwmarrgswjxmb` is naughty because it contains only one vowel.
        
    ----

    :param input_file: The input file's path
    :return: Number of nice texts
    """
    nice_texts = 0
    with open(input_file, 'r') as f:
        for line in f:
            if is_nice_text(line.strip()):
                nice_texts += 1
    return nice_texts


def is_nice_text(text):
    """
    Check if the given text is nice.
    """
    # check if the text contains at least three vowels with regex
    if not re.search(r'.*[aeiou].*[aeiou].*[aeiou].*', text):
        return False

    # check if the text contains at least one letter that appears twice in a row
    if not re.search(r'(.)\1', text):
        return False

    # check if the text contains any of the disallowed substrings
    if re.search(r'ab|cd|pq|xy', text):
        return False

    return True


if __name__ == "__main__":
    print(count_nice_texts('input.txt'))
