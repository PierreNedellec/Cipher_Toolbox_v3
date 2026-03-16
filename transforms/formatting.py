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

def assign_value_for_k_characters(text,k=2):
    k = int(k)
    alphabet = list(string.ascii_letters)[::-1]
    assign_table = {}
    result = ''
    for i in range(0,len(text),k):
        block = text[i:i+k]
        if block not in assign_table.keys():
            assign_table[block] = alphabet.pop(0)
        result += assign_table[block]
    if len(text)%k != 0:
        print("WARNING: length of text is not a multiple of k. Last block was shorter, and has been replaced by its own character.")
    return result

def remove_whitespace(text):
    return remove_linebreaks(remove_spaces(text))
    
register("capitalise",capitalise)
register("remove_spaces",remove_spaces)
register("block5_spacing",block5_spacing)
register("remove_linebreaks",remove_linebreaks)
register("remove_whitespace",remove_whitespace)
register("strip",remove_all_but_letters)
register("assign_values",assign_value_for_k_characters)