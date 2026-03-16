from registry import TRANSFORMS
from transforms import reverse, caesar, vigenere, formatting, columnar_transposition, monoalphabetic_substitution
from breaking import fitness, caesar_break, vigenere_break, monosub_break

def run(name, text, key=None):
    if name not in TRANSFORMS:
        raise ValueError("Unknown Transform")
    
    func = TRANSFORMS[name]
    if key:
        return func(text, key)
    else:
        return func(text)