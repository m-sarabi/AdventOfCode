"""
Short description:
The elves need ribbons to wrap the presents.
Ribbons are the same width. they only need to know the length of the ribbon.
length of the ribbons are the perimeter of the smallest face plus the volume of the present for the bow.

How many total feet of ribbon should they order?
"""


def ribbon_length(input_file: str) -> int:
    """This function calculates the total length of ribbon needed to wrap all the presents in the input file.

    ----

    Examples:
    ----
        - A present with dimensions `2x3x4` requires `2+2+3+3 = 10` feet of ribbon to wrap the present plus
          `2*3*4 = 24` feet of ribbon for the bow, for a total of `34` feet.
        - A present with dimensions `1x1x10` requires `1+1+1+1 = 4` feet of ribbon to wrap the present plus
          `1*1*10 = 10` feet of ribbon for the bow, for a total of `14` feet.

    ----

    :param input_file: the path to the input file
    :return: total length of the ribbon
    """

    # reading the box sizes from the file
    # each line of the input contains one box's dimension like "29x13x26"
    with open(input_file) as file:
        lines = file.readlines()

    result = 0  # adding each box's size to this variable

    # calculating the length of ribbon plus the bow for each box
    for line in lines:
        # extracting the sizes from the line
        sizes = [int(_) for _ in line.rstrip().split('x')]
        # sorting the sizes in ascending order
        sizes.sort()

        # shortest distance around each box
        # which is twice the sum of the two smallest sides
        result += 2 * sum(sizes[:2])

        # adding the volume of the box to the result
        result += sizes[0] * sizes[1] * sizes[2]

    # and return the total square feet of papers
    return result


if __name__ == "__main__":
    print(ribbon_length('input.txt'))
