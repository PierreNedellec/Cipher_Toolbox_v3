from breaking.fitness import ord,chr
from breaking.vigenere_break import vigenere_slices
import matplotlib.pyplot as plt
from registry import register

def signature(text):
    frequencies = [0 for a in range(26)]
    length = len(text)
    for letter in text:
        frequencies[ord(letter)] += 1
    for i in range(26):
        frequencies[i] = frequencies[i]/length
    return sorted(frequencies,reverse=True)

def twist(sig):
    sig2 = [0.12496014535434441, 0.09250682086050632, 0.0804422164008742, 0.07592876339015997, 0.07286619860331199, 0.07095949756488905, 0.06547646768881409, 0.06131304014503403, 0.05437280009204764, 0.041338829498822956, 0.03967046609020289, 0.031027513350384343, 0.027143305399432584, 0.02542837027004644, 0.023329271127282197, 0.020219923887899973, 0.01949922124075072, 0.018786947864328357, 0.01722416107156261, 0.015345908821842938, 0.009961712145040776, 0.006572302385757567, 0.0019890971597783017, 0.0016099907088363413, 0.0010753642129832264, 0.0009516646650660886]
    # Signature of english text, from brown corpus
    sig1 = sig
    twist_value = 0
    for i in range(13):
        twist_value += (sig1[i]-sig2[i])
    for i in range(13,26):
        twist_value += (sig2[i]-sig1[i])
    return twist_value

def average_signatures(signatures):
    avg_signature = [0 for a in range(26)]
    for i in range(26):
        for sig in range(len(signatures)):
            avg_signature[i] += signatures[sig][i]
        avg_signature[i]/=len(signatures)
    return avg_signature

def find_keysize(text):
    keysize_used = []
    resultant_twist = []
    maximum_keyword_length = min(50,len(text))
    for keysize in range(1,maximum_keyword_length):
        print('Testing keysize',keysize,'...')
        slices = vigenere_slices(text,keysize)
        signatures = []
        for slice in slices:
            signatures.append(signature(slice))
        avg = average_signatures(signatures)
        twisted = twist(avg)
        keysize_used.append(keysize)
        resultant_twist.append(twisted)
    plt.bar(keysize_used,resultant_twist)
    plt.show()

register("signature",signature)
register("twist",twist)
register("twist_keysize",find_keysize)