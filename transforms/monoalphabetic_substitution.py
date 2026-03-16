import string
from registry import register
from transforms.caesar import ord, chr


def monosub_encrypt(text, key):
    if len(set(list(key))) != 26 or len(key) != 26:
        raise ValueError("Key in monoalphabetic substitution must have 26 letters, which are all unique.")
    key_lookup = {}
    result = ''
    alphabet = string.ascii_uppercase
    for i in range(26):
        key_lookup[alphabet[i]] = key[i]
    for letter in text:
        if letter not in key_lookup.keys():
            result += letter
        else:
            result += key_lookup[letter]
    return result

def monosub_decrypt(text, key):
    if len(set(list(key))) != 26:
        raise ValueError("Key in monoalphabetic substitution must have 26 letters, which are all unique.")
    new_key = inverse_key(key)
    return monosub_encrypt(text, new_key)


def inverse_key(key):
    inverse = ['' for a in range(26)]
    for i in range(26):
        letter = key[i]
        inverse[ord(letter)] = chr(i)
    return ''.join(inverse)

def remove_duplicates(word):
    valid = []
    for letter in word:
        if letter not in valid:
            valid.append(letter)
    return ''.join(valid)

def generate_key(keyword):
    alphabet = string.ascii_uppercase
    key = remove_duplicates(keyword)
    last_letter_index = ord(key[-1])
    alphabet = alphabet[last_letter_index:] + alphabet[:last_letter_index]
    return remove_duplicates(key+alphabet)
        


register("monosub_encrypt",monosub_encrypt)
register("monosub_decrypt",monosub_decrypt)
register("monosub_inverse_key", inverse_key)
register("monosub_gen_key",generate_key)