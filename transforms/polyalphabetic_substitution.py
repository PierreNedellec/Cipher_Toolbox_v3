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


