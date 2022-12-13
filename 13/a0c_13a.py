'''
depth : list with indices
lst :   list with nested sublists, with a depth corresponding with the depth above
'''
def get_element(lst, depth):
    if depth == []:
        return lst
    if len(depth) == 1:
        return (lst[depth[0]])
    else:
        return get_element(lst[depth[0]], depth[1:])


'''
parses a string into a nested list
'''
def parse_line(line):
    lst = []
    depth = [0]
    i = 0
    while i < len(line):
        c = line[i]
        if not (i == 0 or i == len(line) -1):  # skip first and last char of line
            el = get_element(lst, depth[:-1])
            if c == "[":
                el.append([])
                depth.append(0)
            if c.isnumeric():
                num = int(c)
                while line[i+1].isnumeric():
                    num = num * 10 + int(line[i+1])
                    i += 1
                el.append(int(num))
                depth[-1] += 1
            if c == "]":
                depth.pop(-1)
                depth[-1] += 1
        i += 1
    return lst


'''
left and right can be integer, list or mixed
'''
def compare(left, right):
    if (type(left) is not list) and (type(right) is not list):
        if left < right:
            return 1  # correct order
        elif left > right:
            return -1  # wrong order
        else:
            return 0  # undecided
    if type(left) is not list:
        left = [left]
    if type(right) is not list:
        right = [right]
    for i, _ in enumerate(left):
        if i > len(right) - 1:
            return -1
        result = compare(left[i], right[i])
        if result != 0:
            return result
    return 1


sum_indices = 0
index = 1
with open("13/input_test.txt") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        left = parse_line(lines[i].strip())
        right = parse_line(lines[i+1].strip())
        if compare(left, right) == 1:
            sum_indices += index
        index += 1

print(sum_indices)

# 6251 -> too high!
