TRANSFORMS = {}

def register(name, func):
    TRANSFORMS[name] = func