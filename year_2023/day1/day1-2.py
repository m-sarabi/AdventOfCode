def extract_number(pos):
    rng = range(len(line)) if pos == 'first' else range(len(line), 0, -1)
    for i in rng:
        for letter in letters:
            if line[i:].startswith(letter) if pos == 'first' else line[:i].endswith(letter):
                return letters[letter]


letters = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
           "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, }

with open("input.txt", 'r') as file:
    lines = file.readlines()
    calibration_code = 0
    lines = [_.strip() for _ in lines]
    for line in lines:
        code = extract_number('first') * 10 + extract_number('second')
        calibration_code += code
print(calibration_code)

# 54249
