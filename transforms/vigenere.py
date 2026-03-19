from registry import register
from transforms.monoalphabetic_substitution import atbash
import string

def inalpha(letter):
    if letter in string.ascii_uppercase:
        return True
    return False

def cycle(keyword_letters):
    end = keyword_letters.pop(0)
    return keyword_letters.append(end)

def vigenere_encrypt(text, keyword):
    keyword = list(keyword)
    result = ""
    for c in text:
        if inalpha(c):
            new_order = (ord(c) + (ord(keyword[0]) - ord("A")))
            if new_order > ord("Z"):
                new_order -= 26
            result += chr(new_order)
            cycle(keyword)
        else:
            result += c
    return result


def vigenere_decrypt(text, keyword):
    keyword = list(keyword)
    result = ""
    for c in text:
        if inalpha(c):
            new_order = (ord(c) - (ord(keyword[0]) - ord("A")))
            if new_order < ord("A"):
                new_order += 26
            result += chr(new_order)
            cycle(keyword)
        else:
            result += c
    return result

def beaufort_encrypt(text,keyword):
    keyword = atbash(keyword)
    text = atbash(text)
    return vigenere_encrypt(text,keyword)

def beaufort_decrypt(text,keyword):
    keyword = atbash(keyword)
    text = atbash(text)
    return vigenere_decrypt(text,keyword)

register("vigenere_encrypt",vigenere_encrypt)
register("vigenere_decrypt",vigenere_decrypt)
register("beaufort_encrypt",beaufort_encrypt)
register("beaufort_decrypt",beaufort_decrypt)