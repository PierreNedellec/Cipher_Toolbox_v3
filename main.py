from registry import TRANSFORMS
from transforms import reverse, caesar, vigenere, formatting

def run(name, text, key=None):
    if name not in TRANSFORMS:
        raise ValueError("Unknown Transform")
    
    func = TRANSFORMS[name]
    return func(text, key)