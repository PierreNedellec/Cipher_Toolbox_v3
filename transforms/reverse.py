from registry import register

def reverse(text, key=None):
    return text[::-1]

register("reverse",reverse)