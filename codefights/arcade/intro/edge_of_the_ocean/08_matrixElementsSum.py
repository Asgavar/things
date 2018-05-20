def matrixElementsSum(matrix):
    rooms_to_be_afraid_of = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if is_indirectly_haunted(row, column, matrix):
                rooms_to_be_afraid_of.append((row, column))
    for haunted_row, haunted_column in rooms_to_be_afraid_of:
        matrix[haunted_row][haunted_column] = 0
    return sum(map(sum, matrix))

def is_indirectly_haunted(room_row, room_column, matrix):
    column_above = [row[room_column] for row in matrix[:room_row]]
    return 0 in column_above
