with open ('Day5/day_5') as f:
    data = [line.split(" -> ") for line in f.read().splitlines()]

#Part 1
field = [[0 for i in range(1000)] for j in range(1000)]
for d in data:
    x1, y1 = d[0].split(',')
    x2, y2 = d[1].split(',')
    x1, y1 = int(x1), int(y1)
    x2, y2 = int(x2), int(y2)

    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            field[y1][i] += 1

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            field[i][x1] += 1

print(len([col for row in field for col in row if col > 1]))

#Part 2
field = [[0 for i in range(1000)] for j in range(1000)]
for d in data:
    x1, y1 = d[0].split(',')
    x2, y2 = d[1].split(',')
    x1, y1 = int(x1), int(y1)
    x2, y2 = int(x2), int(y2)

    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            field[y1][i] += 1
    elif x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            field[i][x1] += 1
    else:
        x = x1
        y = y1
        x2 = x2+1 if x1 < x2 else x2-1
        y2 = y2+1 if y1 < y2 else y2-1
        while True:
            field[y][x] += 1
            x = x+1 if x1 < x2 else x-1
            y = y+1 if y1 < y2 else y-1
            if x == x2 and y == y2:
                break

print(len([col for row in field for col in row if col > 1]))