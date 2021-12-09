with open ('Day8/day_8') as f:
    data = [[n.split(" | ")[0].strip().split(), n.split(" | ")[1].strip().split()] for n in f.readlines()]

# Part 1
segments = {}
for combinations in data:
    for combination in combinations[1]:
        segments[len(combination)] = segments.get(len(combination), 0) + 1

#print(segments[2] + segments[4] + segments[3] + segments[7])

values = []
# Part 2
for combinations in data:
    digits = {}
    mapping = {}
    for combination in combinations[0]:
        digits.setdefault(len(combination),[]).append(combination)
    mapping[1] = digits[2]
    mapping[4] = digits[4]
    mapping[7] = digits[3]
    mapping[8] = digits[7]

    for six in digits[6]:
        for d in [d for d in mapping[4] for d in d]:
            if d not in six:
                break
        else:
            mapping.setdefault(9,[]).append(six)
            continue
        for d in [d for d in mapping[1] for d in d]:
            if d not in six:
                break
        else:
            mapping.setdefault(0,[]).append(six)
            continue

        mapping.setdefault(6,[]).append(six)

    for five in digits[5]:
        for d in [d for d in mapping[1] for d in d]:
            if d not in five:
                break
        else:
            mapping.setdefault(3,[]).append(five)
            continue
        for d in [d for d in five for d in d]:
            if d not in mapping[6][0]:
                break
        else:
            mapping.setdefault(5,[]).append(five)
            continue
        mapping.setdefault(2,[]).append(five)

    #print(mapping)

    result = []
    for combination in [c for c in combinations[1]]:
        #print(combination)
        for value, signal in mapping.items():
            if len(combination) == len(signal[0]):
                if(sorted(signal[0]) == sorted(combination)):
                    result.append(str(value))
                    break
    if result:
        values.append((int("".join(result))))
print(sum(values))
#print(values)
