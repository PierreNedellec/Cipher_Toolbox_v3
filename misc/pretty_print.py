from registry import register

def pretty_print(plaintext, key=None, fitness=None):
    print("Plaintext")
    print(plaintext)
    if key:
        print('\nKey:',key)
    if fitness:
        print('\nFitness:',fitness,'\n')
