"""
Short description:
The elves need paper for wrapping gifts in a box

All numbers in the elves' list are in feet.
How many total square feet of wrapping paper should they order?
"""


def total_area(input_file: str) -> int:
    """This function calculates the total square feet of paper that elves need to wrap the gifts in

    ----

    Examples:
    ----
        - A present with dimensions `2x3x4` requires `2*6 + 2*12 + 2*8 = 52` square feet of wrapping paper plus
          `6` square feet of slack, for a total of `58` square feet.
        - A present with dimensions `1x1x10` requires `2*1 + 2*10 + 2*10 = 42` square feet of wrapping paper plus
          `1` square foot of slack, for a total of `43` square feet.

    ----

    :param input_file: the path to the input file
    :return: total area of papers
    """

    # reading the box sizes from the file
    # each line of the input contains one box's dimension like "29x13x26"
    with open(input_file) as file:
        lines = file.readlines()

    result = 0  # adding each box's size to this variable

    # calculating each box's size in a loop
    for line in lines:
        # extracting the sizes from the line
        sizes = [int(_) for _ in line.rstrip().split('x')]

        areas = []  # storing each side's area in this list
        for x in range(2):
            for y in range(x + 1, 3):
                areas.append(sizes[x] * sizes[y])

        # calculating the area of each box plus the slack
        result += sum(areas) * 2 + min(areas)

    # and return the total square feet of papers
    return result


if __name__ == "__main__":
    print(total_area('input.txt'))
