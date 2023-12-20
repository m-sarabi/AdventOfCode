"""
Short description:
Santa needs to find out which texts are naughty or nice.
A nice text is one with all the following properties:
- It contains a pair of any two letters that appears at least twice in the string without overlapping
- It contains at least one letter which repeats with exactly one letter between them

How many nice texts are there?
"""

import re


def count_nice_texts(filename):
    """
    Count the number of nice texts in the given file.

    ----

    Examples
    ----
        - `qjhvhtzxzqqjkmpb` is nice because it has a pair that appears twice (`qj`) and a letter that repeats
          with exactly one letter between them (`zxz`).
        - `xxyxx` is nice because it has a pair that appears twice and a letter that repeats with one between,
          even though the letters used by each rule overlap.
        - `uurcxstgmygtbstg` is naughty because it has a pair (`tg`) but no repeat with a single letter between them.
        - `ieodomkazucvgmuy` is naughty because it has a repeating letter with one between (`odo`),
          but no pair that appears twice.

    ----
    """
    nice_texts = 0
    with open(filename, 'r') as f:
        for line in f:
            if is_nice_text(line.strip()):
                nice_texts += 1
    return nice_texts


def is_nice_text(text):
    """
    Check if the given text is nice.
    """
    # check if the text has two letters repeat at least twice without overlapping
    if not re.search(r'([a-z][a-z]).*\1', text):
        return False

    # check for a letter that repeats with exactly one letter in between them
    if not re.search(r'([a-z]).\1', text):
        return False

    return True


if __name__ == "__main__":
    print(count_nice_texts('input.txt'))
