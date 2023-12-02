# Short description:
# go up one floor if '(', go down one floor if '('
# to what floor do the instructions take santa?

# reading the instructions from the file
# it's text is "()()(()()()(()()((()..."
with open('input.txt') as file:
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
print(floor)
