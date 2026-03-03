from registry import TRANSFORMS
from transforms import reverse, caesar, vigenere, formatting
from breaking import fitness, caesar_break

def run(name, text, key=None):
    if name not in TRANSFORMS:
        raise ValueError("Unknown Transform")
    
    func = TRANSFORMS[name]
    return func(text, key)