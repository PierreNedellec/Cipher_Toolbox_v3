from transforms import caesar
from registry import register

def keyword_to_permutation(word):
    indexes = []
    permutation = []
    for i in word:
        indexes.append(caesar.ord(i))
    for j in range(len(word)):
        smallest = min(indexes)
        position_of_smallest = indexes.index(smallest)
        permutation[position_of_smallest] = j
    return permutation

def column_encrypt(text, keyword):
    keylength = len(keyword)
    last_element = len(text)-1
    matrix = [['' for a in range(keylength)] for b in range((last_element//keylength)+1)]
    for i in range(len(text)):
        row = i//keylength
        column = i%keylength
        matrix[row][column] = text[i]
    print(matrix)

register("column_encrypt",column_encrypt)