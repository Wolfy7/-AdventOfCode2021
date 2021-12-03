with open ('Day3/day_3') as f:
    data = f.read().splitlines()

# Part 1

common_values = [0,0,0,0,0,0,0,0,0,0,0,0]
for number in data:
    for i, bit in enumerate(number):
        common_values[i] += int(bit)

gamma_rate = ["1" if (c > len(data)//2) else "0" for c in common_values ]
epsilon_rate = []
for b in gamma_rate:
    epsilon_rate.append( "1" if b == "0" else "0" )

gamma_rate = int("".join(gamma_rate), 2)
epsilon_rate = int("".join(epsilon_rate), 2)
print(gamma_rate ,epsilon_rate, gamma_rate * epsilon_rate)

# Part 2

def find_rating(data, pos = 0, bit_criteria = "1"):
    if len(data) == 1:
        return data[0]

    common_values = [0,0,0,0,0,0,0,0,0,0,0,0]
    for number in data:
        for i, bit in enumerate(number):
            common_values[i] += int(bit)

    if bit_criteria == "1":
        most_common = [1 if (c >= len(data)/2) else 0 for c in common_values]
    if bit_criteria == "0":
        most_common = [0 if (c >= len(data)/2) else 1 for c in common_values]

    new_list = []
    for v in data:
         if int(v[pos]) == most_common[pos]:
                new_list.append(v)

    return find_rating(new_list, pos + 1, bit_criteria)

oxygen_generator_rating = int(find_rating(data, 0, "1"), 2)
CO2_scrubber_rating = int(find_rating(data, 0, "0"), 2)

print(oxygen_generator_rating, CO2_scrubber_rating, oxygen_generator_rating * CO2_scrubber_rating)