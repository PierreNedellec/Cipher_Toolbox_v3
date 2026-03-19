from registry import register
from transforms.polyalphabetic_substitution import polyalphabetic_encrypt,polyalphabetic_decrypt

def furgod_alphabets():
    return open("transforms/furgod_alphabets.txt",'r').read().splitlines()

def keyword_is_valid(keyword):
    for banned in "JQXY":
        if banned in keyword:
            return False
    return True

def keyword_to_alphabet_keys(keyword=str):
    alphabet_key = []
    for banned in "JQXY":
        if banned in keyword:
            raise ValueError("Keyword for the FurGod cipher must not have the letters J,Q,X or Y.")
    for letter in keyword:
        index = ord(letter)-ord("A")
        alphabet_key.append(furgod_alphabets()[index])
    return alphabet_key

def furgod_encrypt(text=str,keyword=str):
    key = keyword_to_alphabet_keys(keyword)
    return polyalphabetic_encrypt(text,key)

def furgod_decrypt(text=str,keyword=str):
    key = keyword_to_alphabet_keys(keyword)
    return polyalphabetic_decrypt(text,key)

register("furgod_encrypt",furgod_encrypt)
register("furgod_decrypt",furgod_decrypt)
register("furgod_key",keyword_to_alphabet_keys)