from registry import TRANSFORMS
from transforms import reverse, caesar, vigenere, formatting, columnar_transposition
from breaking import fitness, caesar_break, vigenere_break

def run(name, text, key=None):
    if name not in TRANSFORMS:
        raise ValueError("Unknown Transform")
    
    func = TRANSFORMS[name]
    if key:
        return func(text, key)
    else:
        return func(text)