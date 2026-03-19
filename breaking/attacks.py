from breaking.fitness import fitness
import random

def null_function(text,key):
    return text

def dictionary_attack(ciphertext = str,cipher_decryptor = null_function, wordlist = "breaking/words_alphabetical.txt"):
    words = open(wordlist,'r').read().splitlines()
    best = ['',-1000,'']
    section = ciphertext[:(min(50,len(ciphertext)))]
    for w in words:
        if random.randint(1,1000) == 1:
            print('Attempting to break with',w,'...')
        try:
            decrypted = cipher_decryptor(section,w)
            fit = fitness(decrypted)
            if fit>4:
                print(decrypted,w,fit)
            if fit > best[1]:
                best[0] = cipher_decryptor(ciphertext,w)
                best[1] = fitness(best[0])
                best[2] = w
        except ValueError:
            pass
    return best


