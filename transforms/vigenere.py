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

def cycle(keyword_letters):
    end = keyword_letters.pop(0)
    return keyword_letters.append(end)

def vigenere_encrypt(text, keyword):
    keyword = list(keyword)
    result = ""
    for c in text:
        if inalpha(c):
            result += chr((ord(c) + ord(keyword[0])) % 26 )
            cycle(keyword)
        else:
            result += c
    return result


def vigenere_decrypt(text, keyword):
    keyword = list(keyword)
    result = ""
    for c in text:
        if inalpha(c):
            result += chr((ord(c) - ord(keyword[0])) % 26 )
            cycle(keyword)
        else:
            result += c
    return result

register("vigenere_encrypt",vigenere_encrypt)
register("vigenere_decrypt",vigenere_decrypt)