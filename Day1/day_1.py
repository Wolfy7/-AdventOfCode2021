with open ('day_1') as f:
    data = f.read().splitlines()

# Part 1
counter = 0
previous = 0

for value in data:
    value = int(value)
    if previous != 0 and value > previous:
        counter += 1

    previous = value

print(counter)


# Part 2
counter = 0
previous = 0

for i, value in enumerate(data[:-2]):
    value = int(value) + int(data[i+1]) + int(data[i+2])
    if previous != 0 and value > previous:
        counter += 1

    previous = value

print(counter)