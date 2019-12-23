''' Sum two numbers and find the target in the remaining array '''
def sum_two(target, numbers):
    map = {}
    for n in range(numbers.__len__()):
        key = numbers[n]
        map[key] = n
        if target-numbers[n] in map:
            return [n, map.get(target-numbers[n])]
        else:
            n += 1


print(sum_two(9, [2, 7, 11, 13]))
