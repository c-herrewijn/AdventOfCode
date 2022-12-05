options_opponent = ['A', 'B', 'C']
options_player = ['X', 'Y', 'Z']
points = 0

with open("day02/input.txt") as file1:
    lines = file1.readlines()
    for line in lines:
        opponent, player = line.strip().split(' ')
        shape_score = options_player.index(player) + 1

        # draw
        if (options_player.index(player) - options_opponent.index(opponent)) % 3 == 0:
            points += shape_score + 3
        
        # win
        if (options_player.index(player) - options_opponent.index(opponent)) % 3 == 1:
            points += shape_score + 6
        
        # loss
        if (options_player.index(player) - options_opponent.index(opponent)) % 3 == 2:
            points += shape_score + 0

print(points)
