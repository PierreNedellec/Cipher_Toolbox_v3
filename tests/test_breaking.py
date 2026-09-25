import pytest

from transforms.caesar import caesar_encrypt
from transforms.vigenere import vigenere_encrypt, beaufort_encrypt
from transforms.monoalphabetic_substitution import monosub_encrypt
from breaking.caesar_break import brute_force_caesar
from breaking.vigenere_break import auto_break, beaufort_break_given_period
from breaking.monosub_break import monosub_hillclimb_attack

LONG_PLAINTEXT = (
    "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOGWHILETHECIPHERCLERKENCODES"
    "SECRETMESSAGESFORTHEGENERALWHOWAITSPATIENTLYATTHEFRONTBEFORE"
    "THEBATTLEBEGINSATDAWNNEARTHERIVERWHERETHEENEMYCAMPLIESHIDDEN"
    "AMONGTHETREESANDROCKS"
)

# Longer sample (Declaration of the Rights of Man) for the monosub hill-climb
# test: with only ~200 letters the key search can settle for a substitution
# that is close-but-imperfect (rare letters like J/Q/X/Z are underdetermined),
# so a longer sample is used to keep the test reliable.
DECLARATION_EXCERPT = (
    "THEREPRESENTATIVESOFTHEPEOPLEOFFRANCEFORMEDINTOANATIONALASSEMBLY"
    "CONSIDERINGTHATIGNORANCENEGLECTORCONTEMPTOFHUMANRIGHTSARETHESOLE"
    "CAUSESOFPUBLICMISFORTUNESANDCORRUPTIONSOFGOVERNMENTHAVERESOLVEDTO"
    "SETFORTHINASOLEMNDECLARATIONTHESENATURALIMPRESCRIPTIBLEANDINALIE"
    "NABLERIGHTSTHATTHISDECLARATIONBEINGCONSTANTLYPRESENTTOTHEMINDSOF"
    "THEMEMBERSOFTHEBODYSOCIALTHEYMAYBEFOREVERKEPTATTENTIVETOTHEIRRIG"
    "HTSANDTHEIRDUTIESTHATTHEACTSOFTHELEGISLATIVEANDEXECUTIVEPOWERSOF"
    "GOVERNMENTBEINGCAPABLEOFBEINGEVERYMOMENTCOMPAREDWITHTHEAIMOFEVER"
    "YPOLITICALINSTITUTIONMAYTHEREBYBEMORERESPECTED"
)


def test_brute_force_caesar_recovers_key():
    ciphertext = caesar_encrypt(LONG_PLAINTEXT, 11)
    plaintext, key, fitness = brute_force_caesar(ciphertext)
    assert key == 11
    assert plaintext == LONG_PLAINTEXT


def test_vigenere_auto_break_recovers_key():
    ciphertext = vigenere_encrypt(LONG_PLAINTEXT, "SECURITY")
    plaintext, key, fitness = auto_break(ciphertext)
    assert key == "SECURITY"
    assert plaintext == LONG_PLAINTEXT


def test_vigenere_auto_break_raises_cleanly_on_too_short_ciphertext():
    with pytest.raises(ValueError):
        auto_break("AB")


def test_beaufort_break_given_period_recovers_key():
    ciphertext = beaufort_encrypt(LONG_PLAINTEXT, "SECURITY")
    plaintext, fitness, key = beaufort_break_given_period(ciphertext, 8)
    assert key == "SECURITY"
    assert plaintext == LONG_PLAINTEXT


@pytest.mark.slow
def test_monosub_hillclimb_recovers_key():
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    ciphertext = monosub_encrypt(DECLARATION_EXCERPT, key)
    plaintext, fitness, found_key = monosub_hillclimb_attack(ciphertext)
    assert plaintext == DECLARATION_EXCERPT
