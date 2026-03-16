import string
import random
from itertools import permutations
from breaking import fitness
from transforms.monoalphabetic_substitution import monosub_decrypt
import cProfile
import time
from registry import register

def shuffle_k(initial_key, k=2):
    key = initial_key
    while initial_key == key:
        key = list(initial_key)

        idx = random.sample(range(26), k)

        letters = [key[i] for i in idx]
        random.shuffle(letters)

        for pos, val in zip(idx, letters):
            key[pos] = val
        key = ''.join(key)
    return key

def swap(key):
    a,b = random.sample(range(26),2)
    key = list(key)
    key[a],key[b] = key[b],key[a]
    return "".join(key)

def randomkey():
    key = list(string.ascii_uppercase)
    random.shuffle(key)
    return ''.join(key)

def monosub_hillclimb(text, initial_key=randomkey(), no_improvement_threshold=2500): 
    child = ['',-1000,randomkey()]
    parent = ['',-1000,initial_key]
    parent[0] = monosub_decrypt(text, parent[2])
    counter = 0 
    while counter < no_improvement_threshold:
        child[2] = swap(parent[2])
        child[0] = monosub_decrypt(text,child[2])
        child[1] = fitness.fitness(child[0])
        if child[1] > parent[1]:
            parent = child.copy()
            counter = 0
        counter += 1
    return parent

def key_candidate_gathering(text):
    print('Scanning for candidate keys...')
    child = ['',-1000,randomkey()]
    restarts = 5
    initial_key = randomkey()
    no_improvement_threshold = 500
    candidate_keys = {}
    for a in range(restarts):
        parent = ['',-1000,initial_key]
        parent[0] = monosub_decrypt(text, parent[2])
        counter = 0 
        while counter < no_improvement_threshold:
            child[2] = swap(parent[2])
            child[0] = monosub_decrypt(text,child[2])
            child[1] = fitness.fitness(child[0])
            if child[1] > parent[1]:
                parent = child.copy()
                counter = 0
            counter += 1
        candidate_keys[parent[2]] = parent[1]
        print(str(a+1)+'/'+str(restarts),'keys found')
    candidate_keys = dict(sorted(candidate_keys.items(), key=lambda item: item[1],reverse=True))
    print('Candidate keys found:')
    print(candidate_keys)
    return list(candidate_keys.keys())[:3]

def monosub_hillclimb_attack(text):
    candidates = key_candidate_gathering(text)
    print('Testing best keys...')
    best = ['',-1000,'']
    for key in candidates:
        result = monosub_hillclimb(text,key,2500)
        if result[1] > best[1]:
            best = result.copy()
    return best


register("monosub_break",monosub_hillclimb_attack)
register("swap",shuffle_k)