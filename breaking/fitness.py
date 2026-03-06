import string
from registry import register
import math

def ord(letter):
    return string.ascii_uppercase.index(letter)

def chr(index):
    return string.ascii_uppercase[index]

QUADRAGRAM_FREQUENCIES = open("breaking\quadragram_freq.txt",'r').read().split('\n')
MONOGRAM_FREQUENCIES = open("breaking\monogram_freq.txt",'r').read().split('\n')
for i in range(26):
    MONOGRAM_FREQUENCIES[i] = int(MONOGRAM_FREQUENCIES[i])

def fitness(text):
    sum_of_scores = 0
    for i in range(len(text)-3):
        sum_of_scores += rate(text[i:i+4])
    return sum_of_scores/(len(text)-3)

def rate(quadgram):
    scale_factor = 1
    index = ord(quadgram[0])*26**3 + ord(quadgram[1])*26**2 + ord(quadgram[2])*26**1 + ord(quadgram[3])
    rating = scale_factor*float(QUADRAGRAM_FREQUENCIES[index])
    return rating
    
def monogram_fitness(text):
    return cos_angle_vectors(count_monograms(text), MONOGRAM_FREQUENCIES)

def cos_angle_vectors(u, v):
    dot_product = sum(i*j for i, j in zip(u, v))
    mag_u = math.sqrt(sum(i**2 for i in u))
    mag_v = math.sqrt(sum(i**2 for i in v))
    return dot_product/(mag_u*mag_v)

def count_monograms(text):
    freq = [0 for a in range(26)]
    for i in text:
        freq[ord(i)] += 1
    return freq

def ioc(text):
    letter_frequencies = [0 for a in range(26)]
    length = len(text)
    for i in range(length):
        letter_frequencies[ord(text[i])] += 1
    
    ioc_sum = 0

    for freq in letter_frequencies:
        ioc_sum += freq*(freq-1)

    ioc = ioc_sum/(length*(length-1))
    return ioc

register("ioc",ioc)
register("fitness",fitness)
register("monogram_fitness",monogram_fitness)
register("rate_quadragram",rate)