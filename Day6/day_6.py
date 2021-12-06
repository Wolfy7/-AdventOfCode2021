from collections import defaultdict


with open ('Day6/day_6') as f:
    data = [int(fish) for fish in f.readline().split(",")]

# Part 1
# for _ in range(80):
#     new_fish = 0
#     for i, fish in enumerate(data):
#         if fish != 0:
#             data[i] -= 1
#         else:
#             data[i] = 6
#             new_fish += 1
#     for n in range(new_fish):
#         data.append(8)

# #print(data)
# print(len(data))

def solver(lantern_fish, iterations):
    for d in range(iterations):
        reset = 0
        lantern_fish_tmp = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for k, v in lantern_fish.items():
            if k == 0:
                reset = v
            else:
                lantern_fish_tmp[k - 1] = v

        lantern_fish_tmp[6] += reset
        lantern_fish_tmp[8] = reset

        lantern_fish = dict(lantern_fish_tmp)

    return sum(lantern_fish.values())

lantern_fish = {i: data.count(i) for i in set(data)}
print(solver(lantern_fish, 80))
print(solver(lantern_fish, 256))