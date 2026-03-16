from transforms import caesar
from breaking import fitness, caesar_break
from misc import pretty_print
from registry import register

def vigenere_slices(text, keysize):
    slices = [[] for a in range(keysize)]
    for i in range(len(text)):
        slices[i%keysize].append(text[i])
    return slices


def vigenere_break_given_keysize(text, keysize):
    keysize = int(keysize)
    plaintext_slices = [[] for b in range(keysize)]
    key = ['' for a in range(keysize)]

    ciphertext_slices = vigenere_slices(text, keysize)

    for j in range(keysize):
        slice = ciphertext_slices[j]
        solved = caesar_break.brute_force_caesar_monogram_freq_attack(slice)
        plaintext_slices[j] = list(solved[0])
        key[j] = fitness.chr(solved[1])

    plaintext = ''
    for i in range(len(text)):
        plaintext += plaintext_slices[i%keysize].pop(0)
    return plaintext, key, fitness.fitness(plaintext)

def possible_keyword_lengths(text):
    return_top_n = 20
    significance = 2 #minimum number of times the keyword must appear. lower= more calculation
    longest_keyword = len(text)//significance
    lengths_iocs = [0 for a in range(longest_keyword)]
    for keyword_length in range(longest_keyword):
        lengths_iocs[keyword_length] = avg_ioc_of_slices(text, keyword_length+1)
    
    accepted_iocs = []
    keysizes = []
    for ioc in lengths_iocs:
        if ioc < 0.085 and ioc > 0.050:
            accepted_iocs.append(ioc)
            keysizes.append(lengths_iocs.index(ioc)+1) #+1 because the list is 0 indexed
    if len(set(accepted_iocs)) < len(accepted_iocs):
        print('WARNING: duplicate ioc --> one keysize may have been missed.')
    return keysizes, accepted_iocs

    
def avg_ioc_of_slices(text, keylength):
    avg = 0
    slices = vigenere_slices(text, keylength)
    for slice in slices:
        avg += fitness.ioc(''.join(slice))/len(slices)
    return avg

def auto_break(text):
    keysizes, iocs = possible_keyword_lengths(text)
    best_fitness = -1000
    for size in keysizes:
        print("Breaking keysize",size)
        plaintext, key, fit = vigenere_break_given_keysize(text, size)
        print("Fitness found:",fit)
        if best_fitness < fit:
            best_plaintext = plaintext
            best_key = key
            best_fitness = fit
    return best_plaintext, best_key, best_fitness

register("vigenere_break_given_keysize",vigenere_break_given_keysize)
register("vigenere_determine_keysize", possible_keyword_lengths)
register("vigenere_break", auto_break)