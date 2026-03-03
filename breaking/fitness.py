import string
from registry import register

def ord(letter):
    return string.ascii_uppercase.index(letter)

def chr(index):
    return string.ascii_uppercase[index]

QUADRAGRAM_FREQUENCIES = open("breaking\quadragram_freq.txt",'r').read().split('\n')
def fitness(text,x):
    sum_of_scores = 0
    for i in range(len(text)-3):
        sum_of_scores += rate(text[i:i+4],x)
    return sum_of_scores/(len(text)-3)

def rate(quadgram,x):
    index = ord(quadgram[0])*26**3 + ord(quadgram[1])*26**2 + ord(quadgram[2])*26**1 + ord(quadgram[3])
    rating = QUADRAGRAM_FREQUENCIES[index]
    return int(rating)

register("fitness",fitness)
register("rate_quadragram",rate)