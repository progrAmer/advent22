import fileinput

def get_duplicte_char(a, b):
    for c in a:
        if c in b:
            return c

def get_item_priority(item):
    if item == item.upper():
        return ord(item) - 38
    else:
        return ord(item) - 96

def get_common_item(backpacks):
    common_items = []
    for i in backpacks[0]:
        if i in backpacks[1]:
            common_items.append(i)
    for i in common_items:
        if i in backpacks[2]:
            return i


def get_priority_score(fileName, fileExtension = 'txt'):
    priority_score = 0
    backpacks = []

    for line in fileinput.input(f'{fileName}.{fileExtension}'):
        # backpack = line.strip()
        # midpoint = len(backpack)//2
        # item = get_duplicte_char(backpack[:midpoint], backpack[midpoint:])
        # priority_score += get_item_priority(item)
        if len(backpacks) == 3:
            common_item = get_common_item(backpacks)
            priority_score += get_item_priority(common_item)
            backpacks.clear()

        backpacks.append(line.strip())

    common_item = get_common_item(backpacks)
    priority_score += get_item_priority(common_item)
    
    return priority_score

print(get_priority_score('input'))