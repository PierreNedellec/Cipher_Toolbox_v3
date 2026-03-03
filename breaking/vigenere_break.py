from transforms import caesar
from breaking import fitness, caesar_break
from misc import pretty_print
from registry import register

def vigenere_break_given_keysize(text, keysize):
    keysize = int(keysize)
    slices = [[] for a in range(keysize)]
    plaintext_slices = [[] for b in range(keysize)]
    key = ['' for a in range(keysize)]

    for i in range(len(text)):
        slices[i%keysize].append(text[i])

    for j in range(keysize):
        slice = slices[j]
        solved = caesar_break.brute_force_caesar(slice)
        plaintext_slices[j] = list(solved[0])
        key[j] = fitness.chr(solved[1])

    plaintext = ''
    for i in range(len(text)):
        plaintext += plaintext_slices[i%keysize].pop(0)

    return plaintext, key, fitness.fitness(plaintext)

register("vigenere_break_given_keysize",vigenere_break_given_keysize)