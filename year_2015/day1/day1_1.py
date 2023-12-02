"""
Short description:
go up one floor if '(', go down one floor if '('

To what floor do the instructions take Santa?
"""


def final_floor(input_file: str) -> int:
    """This function finds the final floor based on the instructions

    ----

    Example:
    ----
        - `(())` and `()()` both result in floor `0`.
        - `(((` and `(()(()(` both result in floor `3`.
        - `))(((((` also results in floor `3`.
        - `())` and `))(` both result in floor `-1` (the first basement level).
        - `)))` and `)())())` both result in floor `-3`.

    ----

    :param input_file: the path to the input file
    :return: final floor
    """

    # reading the instructions from the file
    # it's text is "()()(()()()(()()((()..."
    with open(input_file) as file:
        instructions = file.read()

    # first floor is 0
    floor = 0

    # in a loop, we check each char(character) of the instructions
    # if char is '(' we add 1 to the `floor`, otherwise we subtract one from it
    for char in instructions:
        if char == '(':
            floor += 1
        else:
            floor -= 1

    # and when finished, return the final destination
    return floor


if __name__ == "__main__":
    print(final_floor('input.txt'))
