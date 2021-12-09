with open ('Day9/day_9') as f:
    lines = f.read().splitlines()
    board = []
    for line in lines:
        row = []
        for number in line:
            row.append(number)
        board.append(row)

#Part 1

low_points = []
for x, row in enumerate(board):
    for y, number in enumerate(row):
        neighbors = []
        if x > 0:
            neighbors.append(board[x-1][y])
        if y > 0:
            neighbors.append(board[x][y-1])
        if x < len(board)-1:
            neighbors.append(board[x+1][y])
        if y < len(board[x])-1:
            neighbors.append(board[x][y+1])

        if number < min(neighbors):
            low_points.append((x,y))

result = 0
for point in low_points:
    result += int(board[point[0]][point[1]])
print(result + len(low_points))

#Part 2

def get_neighbor(x,y, points = []):
    if (x > len(board)-1) or (y > len(board[0])-1) or (x < 0) or (y < 0) or board[x][y] == "9":
        return False
    if (x, y) in points:
        return False

    points.append((x,y))
    field = board[x][y]
    if x > 0:
        neighbor = get_neighbor(x-1,y, points)
        if neighbor != False:
            field += neighbor
    if y > 0:
        neighbor = get_neighbor(x,y-1, points)
        if neighbor != False:
            field += neighbor
    if x < len(board)-1:
        neighbor = get_neighbor(x+1,y, points)
        if neighbor != False:
            field += neighbor
    if y < len(board[0])-1:
        neighbor = get_neighbor(x,y+1, points)
        if neighbor != False:
            field += neighbor
    return field

basins = []
for point in low_points:
    basin = len(get_neighbor(*point))
    basins.append(basin)

basins = sorted(basins, reverse=True)
print(basins[0] * basins[1] * basins[2])


