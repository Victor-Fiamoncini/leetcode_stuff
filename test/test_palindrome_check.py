from src.palindrome_check import palindrome_check


def test_palindrome_check() -> None:
    assert palindrome_check("o") == True
    assert palindrome_check("ovo") == True
    assert palindrome_check("ovvo") == True
    assert palindrome_check("ovvvo") == True
    assert palindrome_check("ovovo") == True
    assert palindrome_check("oovoo") == True
    assert palindrome_check("oooo") == True

    assert palindrome_check("") == False
    assert palindrome_check("ov") == False
    assert palindrome_check("ovv") == False
    assert palindrome_check("oov") == False
