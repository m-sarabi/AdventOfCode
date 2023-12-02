"""
Short description:
go up one floor if '(', go down one floor if '('
to what floor do the instructions take santa?
"""


# reading the instructions from the file
# it's text is "()()(()()()(()()((()..."
def final_floor(input_file: str) -> int:
    """This function finds the final floor based on the instructions

    :param input_file: the path to the input file
    :return: final floor
    """
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

    # and we print the final floor
    return floor


if __name__ == "__main__":
    print(final_floor('input.txt'))
