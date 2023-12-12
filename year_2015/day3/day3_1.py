"""
Short description:

Santa moves up, down, left or right to deliver presents to the houses.
How many houses receive at least one present?
"""


def count_houses(input_file: str) -> int:
    """ Count the number of houses that receive at least one present.

    ----

    Examples
    ----
        - `>` delivers presents to `2` houses: one at the starting location, and one to the east.
        - `^>v<` delivers presents to `4` houses in a square,
          including twice to the house at his starting/ending location.
        - `^v^v^v^v^v` delivers a bunch of presents to some very lucky children at only `2` houses.

    ----


    :param input_file: The input file with the directions.
    :return: The number of houses that receive at least one present.
    """
    # reading the directions from the file
    with open(input_file) as file:
        directions = file.read()

    # initializing the list of houses and the starting house (0, 0)
    houses = [(0, 0)]

    # setting the current house to the starting house (0, 0)
    current_house = (0, 0)

    # following the directions in a loop
    for direction in directions:
        # following the direction
        match direction:
            case '^':
                current_house = (current_house[0], current_house[1] + 1)
            case 'v':
                current_house = (current_house[0], current_house[1] - 1)
            case '<':
                current_house = (current_house[0] - 1, current_house[1])
            case '>':
                current_house = (current_house[0] + 1, current_house[1])

        # checking if the current house is already in the list of houses
        if current_house not in houses:
            # if not, add it to the list of houses
            houses.append(current_house)

    # returning the number of houses
    return len(houses)


if __name__ == "__main__":
    print(count_houses('input.txt'))
