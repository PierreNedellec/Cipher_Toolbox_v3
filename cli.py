import sys
from main import run

name = sys.argv[1]
text = sys.argv[2]
key = sys.argv[3] if len(sys.argv) > 3 else None

output = run(name, text, key)
print(output)