"""
Short description:
Santa needs to find the MD5 hash of a secret key to mine AdventCoins for present.
For that he needs to find add a number to the end of the secret key so that
the MD5 hash of the secret key plus the number starts with five/six zeroes.

What is the lowest positive number that can be added to the secret key to make the MD5 hash?
"""

import hashlib


def find_secret_number(secret_key, zeros):
    """
    Find the secret number to add to the secret key to make the MD5 hash start with five/six zeroes.

    ----

    Examples
    ----
        - If your secret key is `abcdef`, the answer is `609043`, because the MD5 hash of `abcdef609043`
          starts with five zeroes (`000001dbbfa...`), and it is the lowest such number to do so.
        - If your secret key is `pqrstuv`, the lowest number it combines with to make an MD5 hash
          starting with five zeroes is `1048970`; that is, the MD5 hash of `pqrstuv1048970` looks like `000006136ef...`.

    ----

    :param secret_key: The secret key.
    :return: The secret number.
    """
    number = 0
    while True:
        md5_hash = hashlib.md5(f'{secret_key}{number}'.encode()).hexdigest()
        if md5_hash.startswith('0' * zeros):
            return number
        number += 1


puzzle_input = 'yzbqklnj'
if __name__ == "__main__":
    # part 1
    print(find_secret_number(puzzle_input, 5))

    # part 2
    print(find_secret_number(puzzle_input, 6))
