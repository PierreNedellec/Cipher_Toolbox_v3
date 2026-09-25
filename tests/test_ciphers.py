from transforms.caesar import caesar_encrypt, caesar_decrypt
from transforms.vigenere import (
    vigenere_encrypt, vigenere_decrypt,
    beaufort_encrypt, beaufort_decrypt,
    variant_beaufort_encrypt, variant_beaufort_decrypt,
)
from transforms.monoalphabetic_substitution import monosub_encrypt, monosub_decrypt, atbash
from transforms.columnar_transposition import column_encrypt, column_decrypt
from transforms.polyalphabetic_substitution import porta

MONOSUB_KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"
PLAINTEXT = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"


def test_caesar_roundtrip():
    ciphertext = caesar_encrypt(PLAINTEXT, 7)
    assert caesar_decrypt(ciphertext, 7) == PLAINTEXT


def test_vigenere_known_answer():
    assert vigenere_encrypt("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
    assert vigenere_decrypt("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"


def test_vigenere_roundtrip():
    ciphertext = vigenere_encrypt(PLAINTEXT, "KEY")
    assert vigenere_decrypt(ciphertext, "KEY") == PLAINTEXT


def test_beaufort_roundtrip():
    ciphertext = beaufort_encrypt(PLAINTEXT, "KEY")
    assert beaufort_decrypt(ciphertext, "KEY") == PLAINTEXT


def test_variant_beaufort_roundtrip():
    ciphertext = variant_beaufort_encrypt(PLAINTEXT, "KEY")
    assert variant_beaufort_decrypt(ciphertext, "KEY") == PLAINTEXT


def test_atbash_is_involutive():
    assert atbash(atbash(PLAINTEXT)) == PLAINTEXT


def test_monosub_roundtrip():
    ciphertext = monosub_encrypt(PLAINTEXT, MONOSUB_KEY)
    assert monosub_decrypt(ciphertext, MONOSUB_KEY) == PLAINTEXT


def test_monosub_rejects_bad_key():
    import pytest
    with pytest.raises(ValueError):
        monosub_encrypt(PLAINTEXT, "NOTALONGENOUGHKEY")


def test_columnar_transposition_roundtrip_length_divisible_by_key():
    # Regression test: length exactly divisible by key length used to drop
    # a whole column of characters (full_columns=0 treated as "all short").
    text = "ABCDEFGHIJKLMNOPQRSTUVWXY"  # 25 chars, key length 5
    key = "ZEBRA"
    ciphertext = column_encrypt(text, key)
    assert column_decrypt(ciphertext, key) == text


def test_columnar_transposition_roundtrip_length_not_divisible_by_key():
    text = "WEAREDISCOVEREDFLEEATONCE"  # 26 chars, key length 5
    key = "ZEBRA"
    ciphertext = column_encrypt(text, key)
    assert column_decrypt(ciphertext, key) == text


def test_porta_is_reciprocal():
    ciphertext = porta(PLAINTEXT, "KEY")
    assert porta(ciphertext, "KEY") == PLAINTEXT
