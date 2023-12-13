"""
Short description:
Santa and robo-santa take turns delivering presents to the houses.

How many houses receive at least one present?
"""


def count_houses(input_file: str) -> int:
    """ Count the number of houses that receive at least one present.

    ----

    Examples
    ----
        - `^v` delivers presents to `3` houses, because Santa goes north, and then Robo-Santa goes south.
        - `^>v<` now delivers presents to `3` houses, and Santa and Robo-Santa end up back where they started.
        - `^v^v^v^v^v` now delivers presents to `11` houses,
          with Santa going one direction and Robo-Santa going the other.

    ----


    :param input_file: The input file with the directions.
    :return: The number of houses that receive at least one present.
    """
    #  reading the directions from the file
    with open(input_file) as file:
        directions = file.read()

    # initializing the list of houses and the starting house (0, 0)
    houses = [(0, 0)]

    # setting the current house to the starting house (0, 0)
    current_house = [(0, 0), (0, 0)]

    # following the directions in a loop for Santa and Robo-Santa
    for i, direction in enumerate(directions):
        # following the direction
        match direction:
            case '^':
                current_house[i % 2] = (current_house[i % 2][0], current_house[i % 2][1] + 1)
            case 'v':
                current_house[i % 2] = (current_house[i % 2][0], current_house[i % 2][1] - 1)
            case '<':
                current_house[i % 2] = (current_house[i % 2][0] - 1, current_house[i % 2][1])
            case '>':
                current_house[i % 2] = (current_house[i % 2][0] + 1, current_house[i % 2][1])

        # checking if the current house is already in the list of houses
        if current_house[i % 2] not in houses:
            # if not, add it to the list of houses
            houses.append(current_house[i % 2])

    # returning the number of houses
    return len(houses)


if __name__ == "__main__":
    print(count_houses('input.txt'))
