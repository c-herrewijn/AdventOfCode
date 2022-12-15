options_opponent = ['A', 'B', 'C']
options_result = ['X', 'Y', 'Z']
points = 0

with open("02/input.txt") as file:
    for line in file:
        opponent, result = line.strip().split(' ')
        result_score = options_result.index(result) * 3
        response = (options_opponent.index(opponent) + options_result.index(result) - 1) % 3
        shape_score = response + 1
        points += shape_score + result_score

print(points)
