with open ('Day2/day_2') as f:
    data = f.read().splitlines()

# Part 1

h_pos = 0
depth = 0

for command in data:
    action, value = command.split()
    if action == 'forward':
        h_pos += int(value)
    elif action == 'down':
        depth += int(value)
    elif action == 'up':
        depth -= int(value)

print(h_pos, depth, (h_pos * depth))

# Part 2

h_pos = 0
depth = 0
aim = 0

for command in data:
    action, value = command.split()
    if action == 'forward':
        h_pos += int(value)
        depth += aim * int(value)
    elif action == 'down':
        aim += int(value)
    elif action == 'up':
        aim -= int(value)

print(h_pos, depth, (h_pos * depth))