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
        if i > len(right) - 1:  # right ran out of items
            return -1
        result = compare(left[i], right[i])
        if result != 0:
            return result
    if len(left) < len(right):  # left ran out of items
        return 1
    else:
        return 0


def bubblesort(list):
    offset = 1
    swapped = True
    while swapped:                       
        swapped = False
        for i in range(len(list)-offset):
            if compare(list[i], list[i+1]) == -1:
                list[i], list[i+1] = list[i+1], list[i] 
                swapped = True
        offset += 1
    return list


# parse input
with open("13/input.txt") as file:
    lines = [parse_line(line.strip()) for line in file if line.strip()]
    div1 = [[2]]
    div2 = [[6]]
    lines.append(div1)
    lines.append(div2)

    # result
    lines = bubblesort(lines)
    print((lines.index(div1)+1) * (lines.index(div2)+1))
