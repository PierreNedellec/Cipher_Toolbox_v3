from transforms import caesar
from breaking import fitness
from registry import register

def brute_force_caesar(text,x):
    best_key = 0
    best_fitness = 0
    for key in range(26):
        decrypt = caesar.caesar_decrypt(text, key)
        fit = fitness.fitness(decrypt,x)
        if fit > best_fitness:
            best_fitness = fit
            best_key = key
    return best_key

register("brute_force_caesar",brute_force_caesar)