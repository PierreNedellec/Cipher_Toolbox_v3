# Cipher Toolbox

A Python toolbox for classical ciphers, built while working through a course on
classical cryptography and cryptanalysis. It's really two things in one:

1. **Cipher implementations** — encrypt and decrypt text with a range of
   classical ciphers.
2. **A cryptanalysis engine** — automatically *break* several of those ciphers
   from ciphertext alone, using the same statistical techniques cryptanalysts
   have used since before computers existed: index of coincidence, quadgram
   frequency scoring, hill-climbing key search, and dictionary attacks.

The second part is the more interesting one. For example, this recovers an
unknown 26-letter substitution key from ciphertext alone, with no crib and no
hints, in about 20 seconds:

```
python cli.py monosub_break "ZITJXOEAWKGVFYGBPXDHLGCTKZITSQMNRGUVIOSTZITEOHITKESTKATFEGRTLLTEKTZDTLLQUTLYGKZITUTFTKQSVIGVQOZLHQZOTFZSNQZZITYKGFZWTYGKTZITWQZZSTWTUOFLQZRQVFFTQKZITKOCTKVITKTZITTFTDNEQDHSOTLIORRTFQDGFUZITZKTTLQFRKGEAL"
```

## Ciphers

| Cipher | Encrypt/decrypt | Notes |
|---|---|---|
| Caesar | `caesar_encrypt` / `caesar_decrypt` | Simple shift cipher |
| Vigenère | `vigenere_encrypt` / `vigenere_decrypt` | Classic polyalphabetic cipher |
| Beaufort | `beaufort_encrypt` / `beaufort_decrypt` | Reciprocal cipher, implemented as Vigenère through an Atbash reflection |
| Variant Beaufort | `variant_beaufort_encrypt` / `variant_beaufort_decrypt` | |
| Monoalphabetic substitution | `monosub_encrypt` / `monosub_decrypt` | Takes a 26-letter key; includes Atbash as a special case |
| Columnar transposition | `column_encrypt` / `column_decrypt` | Keyword-based column permutation |
| Porta | `porta` | Reciprocal polyalphabetic cipher |
| FurGod | `furgod_encrypt` / `furgod_decrypt` | Custom cipher from the course, built on the same polyalphabetic machinery |

Plus text-formatting helpers (`strip`, `capitalise`, `remove_spaces`,
`block5_spacing`, ...) for cleaning up ciphertext before/after processing.

## Breaking attacks

| Attack | Command | What it does |
|---|---|---|
| Caesar brute force | `brute_force_caesar` | Tries all 26 shifts, scores each with quadgram fitness |
| Vigenère auto-break | `vigenere_break` | Detects key length via index of coincidence, then solves each column as an independent Caesar cipher |
| Vigenère hill-climb | `vigenere_break_given_period` | Local search over keys for a known key length |
| Monoalphabetic hill-climb | `monosub_break` | Random-restart hill-climbing over the key space, scored with quadgram fitness |
| Columnar transposition brute force | `bf_transposition` | Tries all column permutations up to a given key length |
| Dictionary attacks | `vigenere_dictionary`, `beaufort_dictionary`, `furgod_dictionary` | Tries English words as keys |
| Key-length inspection | `inspect_period` | Plots index of coincidence / "twist" across candidate key lengths (requires `matplotlib`) |

## Usage

```
python cli.py <transform> <text> [key]
```

Run with no arguments to see the full list of available transforms.

Examples:

```
python cli.py caesar_encrypt "HELLOWORLD" 3
python cli.py vigenere_encrypt "ATTACKATDAWN" LEMON
python cli.py brute_force_caesar "KHOORZRUOG"
python cli.py vigenere_break "LLGKLQVITVQQENHVBYOJJWOCJXJYCISWVSIQYQECLLGWZXACJGNYISXLUSFYJAXAJIVGVALYYIUZFZMFWKGHVZTJOLQQRQMQHEVCVVMJQEVNYMYPGRVVVNHPWXJYSIMRDIDYXQGQSXFUNVGCSVVBVZBTWVYBVZXRZIGHVURASQRFZMLFAHFYEIFMFKVBVBKCWWCHUZHACW"
python cli.py monosub_break "ZITJXOEAWKGVFYGBPXDHLGCTKZITSQMNRGUVIOSTZITEOHITKESTKATFEGRTLLTEKTZDTLLQUTLYGKZITUTFTKQSVIGVQOZLHQZOTFZSNQZZITYKGFZWTYGKTZITWQZZSTWTUOFLQZRQVFFTQKZITKOCTKVITKTZITTFTDNEQDHSOTLIORRTFQDGFUZITZKTTLQFRKGEAL"
```

## Requirements

Python 3.11+. Only external dependency is `matplotlib`, and only for
`inspect_period`.

## Tests

```
python -m pytest tests/ -m "not slow"
```

The `monosub_break` hill-climbing test is marked `slow` (~20-30s) and
excluded by default; run `python -m pytest tests/` to include it.

## Project layout

- `transforms/` — cipher and formatting implementations
- `breaking/` — cryptanalysis attacks and fitness scoring (quadgram/monogram
  frequency tables trained on the Brown corpus)
- `scripts/` — one-off scripts for regenerating the frequency tables and word
  lists used by `breaking/`
- `cli.py` — command-line entry point
