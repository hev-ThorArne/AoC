with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

seeds = lines[0].split()
print(seeds)
linestarts = {"seed-to-soil map:": 0,
              "soil-to-fertilizer map:": 0,
              "fertilizer-to-water map:": 0,
              "water-to-light map:": 0,
              "light-to-temperature map:": 0,
              "temperature-to-humidity map:": 0,
              "humidity-to-location map:": 0,
              "endoffile:": 0}
i = 0
for line in lines:
    n = 0
    for starts in list(linestarts.keys()):
        if line == starts:
            linestarts[starts] = i
        n += 1
    i += 1


def search_in_map2(lines: list, which_map: int, linestarts: dict, find_no: int) -> tuple:

    dest_ranges = []
    src_ranges = []
    this_key = list(linestarts.keys())[which_map]
    next_key = list(linestarts.keys())[which_map+1]
    this_line = linestarts[this_key]+1

    next_line = linestarts[next_key]-1
    find_no = int(find_no)
    result = find_no

    for line in lines[this_line:next_line]:

        line_numbers = [int(x) for x in line.split()]
        dest_ranges = range(line_numbers[0], line_numbers[0]+line_numbers[2]-1)
        src_ranges = range(line_numbers[1], line_numbers[1]+line_numbers[2]-1)
        if find_no in src_ranges:
            result = dest_ranges[src_ranges.index(find_no)]

    return result, this_key


min_location = 100000000000000000
i = 0
LOG_EVERY_N = 1000000
for n in range(1, 22, 2):
    for seed in range(int(seeds[n]), int(seeds[n])+int(seeds[n+1])):
        seed = int(seed)
        i += 1
        result1 = search_in_map2(lines, 0, linestarts, seed)
        result2 = search_in_map2(lines, 1, linestarts, result1[0])
        result3 = search_in_map2(lines, 2, linestarts, result2[0])
        result4 = search_in_map2(lines, 3, linestarts, result3[0])
        result5 = search_in_map2(lines, 4, linestarts, result4[0])
        result6 = search_in_map2(lines, 5, linestarts, result5[0])
        result7 = search_in_map2(lines, 6, linestarts, result6[0])
        if min_location > result7[0]:
            min_location = result7[0]
            print(min_location)
        if (i % LOG_EVERY_N) == 0:
            print(i)