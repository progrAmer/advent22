import fileinput

shapes = ['A', 'B', 'C', 'A', 'B']

def get_round_score(player, opponent):
    score = shapes.index(player) + 1
    
    if shapes[shapes.index(opponent) + 1] == player:
        score += 6
    elif player ==  opponent:
        score += 3 

    return score

def transform_shape(player_shape):
    shapes = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }
    return shapes[player_shape]

def get_player_shape(outcome, opponent_shape):
    outcomes = ['Y', 'Z', 'X']
    return shapes[shapes.index(opponent_shape) + outcomes.index(outcome)]

def get_tournament_score(fileName, fileExtension = 'txt'):
    score = 0
    for line in fileinput.input(f'{fileName}.{fileExtension}'):
        # [opponent, player] = line.strip().split(' ')
        # score += get_round_score(transform_shape(player), opponent)

        [opponent, outcome] = line.strip().split(' ')
        score += get_round_score(get_player_shape(outcome, opponent), opponent)

    return score 

print(get_tournament_score('input'))

