from registry import register
import string

def polyalphabetic_encrypt(text = str, alphabets = list):
    period = len(alphabets)
    ciphertext = ''
    for i in range(len(text)):
        plaintext_letter = text[i]
        index = string.ascii_uppercase.index(plaintext_letter)
        encrypted_letter = alphabets[i%period][index]
        ciphertext += encrypted_letter
    return ciphertext

def polyalphabetic_decrypt(text = str, alphabets = list):
    period = len(alphabets)
    plaintext = ''
    for i in range(len(text)):
        ciphered_letter = text[i]
        index = alphabets[i%period].index(ciphered_letter)
        deciphered_letter = string.ascii_uppercase[index]
        plaintext += deciphered_letter
    return plaintext

def porta_generate_alphabet_key(keyword, mode=2):
    alphabet_key = []
    alphabets = []
    alph1 = list(string.ascii_uppercase[:13])
    alph2 = list(string.ascii_uppercase[13:])
    for a in range(13):
        alphabets.append("".join(alph2)+"".join(alph1))
        end = alph2.pop(0)
        alph2.append(end)
        alph1 = alph1[::-1]
        end = alph1.pop(0)
        alph1.append(end)
        alph1 = alph1[::-1]
        
    if mode == 1:
        for letter in keyword:
            index = ord(letter)- ord("A")
            alphabet_key.append(alphabets[index//2])
    
    if mode == 2:
        for letter in keyword:
            index = (ord(letter)- ord("A"))//2
            if index == 0:
                index = 0
            else:
                index = 13-index
            alphabet_key.append(alphabets[index])
    return alphabet_key

def porta(text,keyword):
    return polyalphabetic_encrypt(text, porta_generate_alphabet_key(keyword))

register("porta_key",porta_generate_alphabet_key)
register("porta",porta)