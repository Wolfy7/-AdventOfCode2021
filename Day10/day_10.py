with open ('Day10/day_10') as f:
    data = f.read().splitlines()

pairs = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}

# Part 1
closing_tags = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
result = 0
incomplete = []
for line in data:
    chars = []
    for char in line:
        #print(char)
        if char in pairs.keys():
            chars.append(char)
        else:
            if  char == pairs[chars[-1]]:
                chars.pop()
            else:
                result += closing_tags[char]
                break
    else:
        incomplete.append(line)

print(result)

# Part 2
closing_tags = {")" : 1, "]" : 2, "}" : 3, ">" : 4}
scores = []
for line in incomplete:
    chars = []
    for char in line:
        if char in pairs.keys():
            chars.append(pairs[char])
            #print(chars)
        else:
            if char in chars:
                chars.reverse()
                chars.remove(char)
                chars.reverse()
    result = 0
    for c in chars[::-1]:
        result = (result * 5) + closing_tags[c]
    scores.append(result)
print(sorted(scores)[len(scores) // 2])