from registry import register
import string

def inalpha(letter):
    if letter in string.ascii_uppercase:
        return True
    return False

def ord(letter):
    return string.ascii_uppercase.index(letter)

def chr(index):
    return string.ascii_uppercase[index]

def caesar_encrypt(text, shift):
    result = ""
    shift = int(shift)
    for c in text:
        if inalpha(c):
            result += chr((ord(c) + shift) % 26 )
        else:
            result += c
    return result

def caesar_decrypt(text, shift):
    shift = int(shift)
    return caesar_encrypt(text, shift*(-1))

register("caesar_encrypt",caesar_encrypt)
register("caesar_decrypt",caesar_decrypt)