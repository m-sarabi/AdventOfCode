"""
Short description:
Santa wants to know when he first reaches the basement.
go up one floor if '(', go down one floor if ')'

What is the position of the character that causes Santa to first enter the basement?
"""


def final_floor(input_file: str) -> int:
    """This function finds the position of first character that takes santa to the basement

    ----

    Example:
    ----
        - `)` causes him to enter the basement at character position `1`.
        - `()())` causes him to enter the basement at character position `5`.

    ----

    :param input_file: the path to the input file
    :return: position of the floor that first reaches the basement
    """

    # reading the instructions from the file
    # it's text is "()()(()()()(()()((()..."
    with open(input_file) as file:
        instructions = file.read()

    # first floor is 0
    floor = 0

    # in a loop, we check each char(character) of the instructions
    # if char is '(' we add 1 to the `floor`, otherwise we subtract one from it
    for position, char in enumerate(instructions):
        if char == '(':
            floor += 1
        else:
            floor -= 1

        if floor < 0:
            # if we reach the negative floor, we return the position of the floor (starting at 1)
            return position + 1


if __name__ == "__main__":
    print(final_floor('input.txt'))
