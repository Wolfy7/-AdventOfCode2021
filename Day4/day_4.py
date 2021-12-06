with open ('Day4/day_4') as f:

    data = [line for line in f.read().splitlines() if line != ""]

numbers = data[0].split(',')

boards = []
for i in range(1, len(data), 5):
    board = []
    for i in [d.split() for d in data[i:i+5]]:
        row = []
        for j in i:
            row.append([int(j), False])
        board.append(row)
    boards.append(board)

def checkBoard(board):
    for x in range(len(board)):
        if all([t[1] for t in board[x]]):
            return True

        for y in range(len(board)):
            if all([t[1] for t in [board[y][x] for y in range(len(board[0]))]]):
                return True
    return False

# Part 1
def part_1():
    for number in numbers:
        for board in boards:
            for x in range(len(board)):
                for y in range(len(board)):
                    if board[x][y][0] == int(number):
                        board[x][y][1] = True
                        if checkBoard(board):
                            tmp = []
                            for x in range(len(board)):
                                for y in range(len(board)):
                                    if board[x][y][1] == False:
                                        tmp.append(board[x][y][0])
                            return(sum(tmp) * int(number))

print(part_1())

# Part 2
won_boards = []
def part_2():
    for number in numbers:
        for board in boards:
            for x in range(len(board)):
                for y in range(len(board)):
                    if board[x][y][0] == int(number):
                        # if int(number) == 16:
                        #     #print(board)
                        board[x][y][1] = True
                        if checkBoard(board) and board not in won_boards:
                            if len(boards) - len(won_boards) == 1:
                                #print(board)
                                tmp = []
                                for x in range(len(board)):
                                    for y in range(len(board)):
                                        if board[x][y][1] == False:
                                            tmp.append(board[x][y][0])
                                return(sum(tmp) * int(number))
                            won_boards.append(board)
print(part_2())