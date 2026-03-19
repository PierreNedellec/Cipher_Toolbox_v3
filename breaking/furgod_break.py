from breaking.attacks import dictionary_attack
from transforms.furgod import furgod_decrypt, keyword_is_valid
from breaking.fitness import fitness
import random
from registry import register

def furgod_dictionary(text):
    result = dictionary_attack(text, furgod_decrypt)
    return result

def tick_key(keyword,index):
    key = list(keyword)
    new = (ord(key[index])+ random.randint(1,25))
    if new > ord("Z"):
        new -= 26
    key[index] = chr(new)
    if not keyword_is_valid("".join(key)):
        return tick_key(keyword,index)
    return "".join(key)

def furgod_break_set_period(text,period):
    period = int(period)
    parent = ['',-1000,"A"*period]
    child = ['','','']
    iterations = 0
    no_improvement_counter = 0
    while no_improvement_counter < 3000:
        child[2] = tick_key(parent[2],iterations%period)
        child[0] = furgod_decrypt(text,child[2])
        child[1] = fitness(child[0])
        if child[1] > parent[1]:
            parent = child.copy()
            no_improvement_counter = 0
        iterations += 1
        no_improvement_counter += 1
    return parent

register("furgod_dictionary",furgod_dictionary)
register("furgod_break",furgod_break_set_period)