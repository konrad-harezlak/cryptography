import random

def column_transposition(text, num_columns):
    padded_text = text + '_' * (num_columns - len(text) % num_columns)
    matrix = [padded_text[i:i + num_columns] for i in range(0, len(padded_text), num_columns)]
    transposed_matrix = [''.join(row[i] for row in matrix) for i in range(num_columns)]
    return ''.join(transposed_matrix)

def row_transposition(text, num_rows):
    num_columns = len(text) // num_rows
    matrix = [text[i:i + num_columns] for i in range(0, len(text), num_columns)]
    transposed_matrix = random.sample(matrix, len(matrix))
    return ''.join(transposed_matrix)
