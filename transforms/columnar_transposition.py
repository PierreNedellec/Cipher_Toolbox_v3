from transforms import caesar
from registry import register
import math

def keyword_to_permutation(word):
    indexes = []
    permutation = ['None' for a in range(len(word))]
    for i in word:
        indexes.append(caesar.ord(i))
    for j in range(len(word)):
        smallest = min(indexes)
        position_of_smallest = indexes.index(smallest)
        permutation[j] = position_of_smallest
        indexes[position_of_smallest] = 1000
    return permutation

def transpose(matrix):
    x_dim = len(matrix[0])
    y_dim = len(matrix)
    transposed_matrix = [['' for a in range(y_dim)] for b in range(x_dim)]
    for column in range(x_dim):
        for row in range(y_dim):
            transposed_matrix[column][row] = matrix[row][column]
    return transposed_matrix

def read_rows(matrix):
    for i in range(len(matrix)):
        matrix[i] = ''.join(matrix[i])
    return ''.join(matrix)


def column_encrypt(text, keyword):
    columns = []
    x_dimension = len(keyword)
    y_dimension = math.ceil(len(text) / x_dimension)

    for column_index in range(x_dimension):
        col = ""
        for i in range(y_dimension):
            pos = x_dimension * i + column_index
            if pos < len(text):
                col += text[pos]
        columns.append(col)

    permuted_columns = []
    perm = keyword_to_permutation(keyword)

    for p in perm:
        permuted_columns.append(columns[p])

    return ''.join(permuted_columns)

def column_decrypt(ciphertext, key):
    width = len(key)
    height = math.ceil(len(ciphertext) / width)
    full_columns = len(ciphertext)%len(key)
    permutation = keyword_to_permutation(key)
    columns = ['' for a in range(width)]

    index = 0
    for p in permutation:
        column_length = height
        if p >= full_columns:
            column_length = height - 1
        columns[p] = ciphertext[index : index + column_length]
        index = index + column_length

    plaintext = ""

    for row in range(height):
        for column in range(width):
            if row < len(columns[column]):
                plaintext += columns[column][row]
    return plaintext

def column_decrypt_from_perm(ciphertext, permutation):
    width = len(permutation)
    height = math.ceil(len(ciphertext) / width)
    full_columns = len(ciphertext)%len(permutation)
    columns = ['' for a in range(width)]

    index = 0
    for p in permutation:
        column_length = height
        if p >= full_columns:
            column_length = height - 1
        columns[p] = ciphertext[index : index + column_length]
        index = index + column_length

    plaintext = ""

    for row in range(height):
        for column in range(width):
            if row < len(columns[column]):
                plaintext += columns[column][row]
    return plaintext
    

register("column_encrypt",column_encrypt)
register("column_decrypt",column_decrypt)
register("permutation_code",keyword_to_permutation)