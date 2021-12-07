with open ('Day7/day_7') as f:
    data = [int(n) for n in f.readline().split(",")]

# Part 1
solutions = []
for i in range(min(data), max(data)+1):
    solutions.append(sum([abs(n-i) for n in data]))

print(min(solutions))

# Part 2
solutions = []
for i in range(min(data), max(data)+1):
    solutions.append(sum([((abs(n-i) * (abs(n-i)+1)) // 2) for n in data]))

print(min(solutions))
