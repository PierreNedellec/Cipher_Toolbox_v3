from transforms.columnar_transposition import column_decrypt_from_perm
from transforms.formatting import remove_all_but_letters, capitalise
from breaking.fitness import fitness
from itertools import permutations
from registry import register

def brute_force_keys(maxlength=6):
    maxlength = int(maxlength)
    perms = []
    for keylength in range(2,maxlength):
        perms += list(permutations(range(keylength)))
    return perms

def brute_force_break(ciphertext, maxlength = 6):
    perms = brute_force_keys(maxlength)
    best_fitness = -1
    best_plaintext = ''
    for key in perms:
        plaintext = column_decrypt_from_perm(ciphertext, key)
        plaintext_fitness = fitness(remove_all_but_letters(capitalise(plaintext)))
        if plaintext[-1] == ".":
            plaintext_fitness += 3
            print(plaintext,plaintext_fitness)
        if plaintext_fitness > best_fitness:
            best_fitness = plaintext_fitness
            best_plaintext = plaintext
            best_key = key
    return [best_plaintext, best_fitness, best_key]
brute_force_keys()

register("permutations",brute_force_keys)
register("bf_transposition",brute_force_break)