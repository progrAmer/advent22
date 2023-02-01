import fileinput

def get_max_calories(fileName, fileExtension = 'txt'):
    max_calories = 0
    current_calories = 0

    for line in fileinput.input(f'{fileName}.{fileExtension}'):
        if line == '\n':
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
            continue

        current_calories += int(line.strip())

    if current_calories > max_calories:
        max_calories = current_calories

    return max_calories


def get_n_top_calories(n, fileName, fileExtension = 'txt'):
    top_calories = []
    current_calories = 0

    for line in fileinput.input(f'{fileName}.{fileExtension}'):
        if line == '\n':
            top_calories.append(current_calories)
            top_calories.sort()
            if len(top_calories) > n:
                top_calories.pop(0)

            current_calories = 0
            continue

        current_calories += int(line.strip())

    return top_calories 

print(get_max_calories('input'))
print(sum(get_n_top_calories(3, 'input')))