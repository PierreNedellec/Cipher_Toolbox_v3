import string
import time
import math

def ord(letter):
    return string.ascii_uppercase.index(letter)

def chr(index):
    return string.ascii_uppercase[index]

def calculate_quad_freqs():
    frequencies = [0 for a in range(26**4)]
    corpus = open('breaking/brown_corpus_no_spaces.txt','r').read()
    print('corpus length=',len(corpus))
    time.sleep(2)
    for a in range(0,len(corpus)-4):
        if a%100000 == 0:
            print(a)
        index = ord(corpus[a])*26**3 + ord(corpus[a+1])*26**2 + ord(corpus[a+2])*26**1 + ord(corpus[a+3])
        frequencies[index] += 1

    for i in range(26**4):
        if frequencies[i] != 0: frequencies[i] = math.log(frequencies[i]) 
        else: frequencies[i] = math.log(0.0001)
        frequencies[i] = str(frequencies[i])

    filename = "breaking/quadragram_freq.txt"
    output = open(filename,'w')
    output.write('\n'.join(frequencies))

def calculate_mono_freqs():
    freq = [0 for a in range(26)]
    corpus = open('breaking/brown_corpus_no_spaces.txt','r').read()

    for i in range(len(corpus)):
        freq[ord(corpus[i])] += 1

    for i in range(26):
        freq[i] = str(freq[i])
    
    filename = "breaking/monogram_freq.txt"
    open(filename,'w').write('\n'.join(freq))

def generate_alphabetical_word_list():
    print('Running...')
    words = []
    text = open('breaking/brown_corpus_spaces.txt','r').read().split()
    one_percent = len(text)//100
    for w in range(len(text)):
        if w%one_percent == 0:
            print(w//one_percent,'% complete')
        if text[w] not in words:
            words.append(text[w])
    words = sorted(words)
    writeto = open('breaking/words_alphabetical.txt','w')
    writeto.write('\n'.join(words))

def generate_frequency_word_list():
    print('Running...')
    words = {'THE':0}
    text = open('breaking/brown_corpus_spaces.txt','r').read().split()
    one_percent = len(text)//100
    for w in range(len(text)):
        word = text[w]
        if w%one_percent == 0:
            print(w//one_percent,'% complete')
        if word not in words.keys():
            words[word] = 0
        words[text[w]] += 1
    words_sorted = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
    words_list_with_relfreq = []
    for a in range(len(words_sorted)):
        item = words_sorted.keys()[a]+' '+str(words_sorted.values()[a]*10000/len(text))
        words_list_with_relfreq.append(item)
    writeto = open('breaking/words_frequencywise.txt','w')
    writeto.write('\n'.join(words_list_with_relfreq))

def find_signature_of_english():
    freq = open('breaking/monogram_freq.txt','r').read().split()
    total = 0
    for val in freq:
        total += int(val)
    for i in range(26):
        freq[i] = int(freq[i])/total
    print(sorted(freq,reverse=True))


generate_alphabetical_word_list()
