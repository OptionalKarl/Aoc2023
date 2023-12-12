def calculate_next_number(sequence):
    def find_sequence(sequence):
        differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        
        while True:
            diffs_of_diffs = [differences[i + 1] - differences[i] for i in range(len(differences) - 1)]
            if len(set(diffs_of_diffs)) == 1:
                break
            differences = diffs_of_diffs

        return differences[0]

    first_difference = find_sequence(sequence)
    second_difference = find_sequence([first_difference])
    
    if second_difference == 0:
        # If the second difference is zero, it's a linear sequence
        return sequence[-1] + first_difference
    
    a = second_difference // 2
    n = len(sequence) + 1
    sequence_2n2 = [2 * a * (i ** 2) for i in range(1, n)]
    
    linear_sequence = [sequence[i] - sequence_2n2[i] for i in range(len(sequence))]
    next_number = linear_sequence[-1] + find_sequence(linear_sequence)
    
    return next_number

# Example sequences
sequences = [
    [-3, 8, 23, 42, 65],[0, 3, 6, 9, 12, 15],[1, 3, 6, 10, 15, 21],[10, 13, 16, 21, 30, 45]
    # Add more sequences here if needed
]

# Predicting the next number for each sequence
for seq in sequences:
    prediction = calculate_next_number(seq)
    print(f"For sequence {seq}, the next number is: {prediction}")
