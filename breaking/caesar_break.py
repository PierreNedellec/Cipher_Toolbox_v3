from transforms import caesar
from breaking import fitness
from misc import pretty_print
from registry import register

def brute_force_caesar(text):
    best_key = 0
    best_fitness = 0
    plaintext = ''
    for key in range(26):
        decrypt = caesar.caesar_decrypt(text, key)
        fit = fitness.monogram_fitness(decrypt)
        if fit > best_fitness:
            best_fitness = fit
            best_key = key
            plaintext = decrypt
    return (plaintext,best_key,best_fitness)

register("brute_force_caesar",brute_force_caesar)