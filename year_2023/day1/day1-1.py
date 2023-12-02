with open("input.txt", 'r') as file:
    lines = file.readlines()
    calibration_code = 0
    for line in lines:
        numbers = [_ for _ in line if _.isnumeric()]
        code = numbers[0] + numbers[-1]
        calibration_code += int(code)

print(calibration_code)

# 53194
