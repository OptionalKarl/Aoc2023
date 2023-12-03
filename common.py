from itertools import permutations

grid_size = (5, 3)
center = (2, 1)
target_character = '*'
repeating_characters = '10'
other_character = '.'

def is_valid_permutation(grid):
    count = 0
    for row in grid:
        count += row.count(repeating_characters)
        if count > 2:
            return False
    return count == 2

def generate_permutations(grid_size, center, target_character, repeating_characters, other_character):
    all_characters = other_character * (grid_size[0] * grid_size[1] - 3)
    permutations_list = []

    for perm in permutations(all_characters):
        perm_list = list(perm)
        perm_list.insert(center[0] * grid_size[1] + center[1], target_character)
        grid = [perm_list[i:i + grid_size[1]] for i in range(0, len(perm_list), grid_size[1])]
        if is_valid_permutation(grid):
            permutations_list.append(grid)

    return permutations_list

permutations_list = generate_permutations(grid_size, center, target_character, repeating_characters, other_character)

# Printing the generated valid permutations
for grid in permutations_list:
    for row in grid:
        print(''.join(row))
    print()