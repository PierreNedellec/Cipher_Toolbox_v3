from registry import TRANSFORMS
from transforms import reverse, caesar, vigenere, formatting, columnar_transposition, monoalphabetic_substitution,furgod,polyalphabetic_substitution
from breaking import attacks, fitness, caesar_break, vigenere_break, monosub_break, polyalphabetic_analysis, furgod_break, transposition_break

def run(name, text, key=None):
    if name not in TRANSFORMS:
        raise ValueError("Unknown Transform")
    
    func = TRANSFORMS[name]
    if key:
        return func(text, key)
    else:
        return func(text)