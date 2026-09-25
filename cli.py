import sys
from main import run
from registry import TRANSFORMS

if len(sys.argv) < 3:
    print(f"Usage: python cli.py <transform> <text> [key]")
    print(f"Available transforms: {', '.join(sorted(TRANSFORMS))}")
    sys.exit(1)

name = sys.argv[1]
text = sys.argv[2]
key = sys.argv[3] if len(sys.argv) > 3 else None

try:
    output = str(run(name, text, key))
except (ValueError, TypeError, IndexError) as e:
    print(f"Error: {e}")
    sys.exit(1)

print(output)
with open('output.txt', 'w') as outpage:
    outpage.write(output)