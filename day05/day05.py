from collections import deque
import fileinput

def transform_stacks(stacks, fileName, fileExtension = 'txt'):
    for line in fileinput.input(f'{fileName}.{fileExtension}'):
        [_, number, _, origin, _, destination] = [int(x) if x.isnumeric() else x for x in line.strip().split(' ')]

        for _ in range(number):
            crate = stacks[origin-1].pop()
            stacks[destination-1].append(crate)

    return stacks


def transform_multiple_stacks(stacks, fileName, fileExtension = 'txt'):
    for line in fileinput.input(f'{fileName}.{fileExtension}'):
        [_, number, _, origin, _, destination] = [int(x) if x.isnumeric() else x for x in line.strip().split(' ')]

        origin_stack = stacks[origin-1]
        stacks[destination-1] += origin_stack[len(origin_stack) - number:]
        stacks[origin-1] = origin_stack[:len(origin_stack) - number]

    return stacks

stacks = [
    ['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],
    ['N','Q','H','W','R','F','S','J'],
    ['F','B','H','W','P','M','Q'],
    ['V','S','T','D','F'],
    ['Q','L','D','W','V','F','Z'],
    ['Z','C','L','S'],
    ['Z','B','M','V','D','F'],
    ['T','J','B'],
    ['Q','N','B','G','L','S','P','H']
]

transformed_stacks = transform_multiple_stacks(stacks, 'input')
print('Top stacks are: ', ''.join(map(str, [x.pop() for x in transformed_stacks])))