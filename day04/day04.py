import fileinput

def get_duplicate_work(fileName, fileExtension='txt'):
    contained_pair_num = 0
    overlap_pair_num = 0

    for line in fileinput.input(f'{fileName}.{fileExtension}'):
        pairs = [ [int(y) for y in x.split('-')] for x in line.strip().split(',')]

        is_contained = (pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]) or (pairs[1][0] >= pairs[0][0] and pairs[1][1] <= pairs[0][1])
        is_overlap = (pairs[0][0] <= pairs[1][0] and  pairs[0][1] >= pairs[1][0]) or (pairs[0][0] >= pairs[1][0] and pairs[0][0] <= pairs[1][1])

        if is_contained:
            contained_pair_num += 1

        if is_overlap:
            print(pairs)
            overlap_pair_num += 1

    return [contained_pair_num, overlap_pair_num]


print(get_duplicate_work('input'))
# print(get_duplicate_work('testInput'))