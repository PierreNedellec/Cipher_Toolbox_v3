import string
import time

def ord(letter):
    return string.ascii_uppercase.index(letter)

def chr(index):
    return string.ascii_uppercase[index]

frequencies = [0 for a in range(26**4)]
corpus = open('brown_corpus_no_spaces.txt','r').read()
print('corpus length=',len(corpus))
time.sleep(2)
for a in range(0,len(corpus)-4):
    if a%1000 == 0:
        print(a)
    index = ord(corpus[a])*26**3 + ord(corpus[a+1])*26**2 + ord(corpus[a+2])*26**1 + ord(corpus[a+3])
    frequencies[index] += 1

for i in range(26**4):
    frequencies[i] = str(frequencies[i])

filename = "quadragram_freq.txt"
output = open(filename,'w')
output.write('\n'.join(frequencies))
