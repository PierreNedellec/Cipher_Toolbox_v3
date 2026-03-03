from registry import register
import string

def inalpha(letter):
    alphabet = string.ascii_uppercase
    return letter in alphabet

def capitalise(text):
    return text.upper()

def remove_spaces(text):
    return text.replace(' ','')

def remove_linebreaks(text):
    return text. replace('\n','')

def remove_all_but_letters(text):
    result = ''
    for c in text:
        if inalpha(c):
            result += c
    return result

def block5_spacing(text):
    blocks = []
    for i in range(0,len(text),5):
        blocks.append(text[i:i+5])
    return ' '.join(blocks)
    
register("capitalise",capitalise)
register("remove_spaces",remove_spaces)
register("block5_spacing",block5_spacing)
register("remove_linebreaks",remove_linebreaks)
register("remove_all_but_letters",remove_all_but_letters)