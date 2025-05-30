import pytest
from string_utils import StringUtils

class TestStringUtils:

    def test_capitalize_string(self):
        assert StringUtils.capitalize_string("hello") == "Hello"
        assert StringUtils.capitalize_string("") == ""
        assert StringUtils.capitalize_string(" ") == " "
        assert StringUtils.capitalize_string("h") == "H"
        assert StringUtils.capitalize_string("123") == "123"
        assert StringUtils.capitalize_string(None) is None

    def test_reverse_string(self):
        assert StringUtils.reverse_string("hello") == "olleh"
        assert StringUtils.reverse_string("") == ""
        assert StringUtils.reverse_string(" ") == " "
        assert StringUtils.reverse_string("123") == "321"
        assert StringUtils.reverse_string(None) is None

    def test_count_vowels(self):
        assert StringUtils.count_vowels("hello") == 2
        assert StringUtils.count_vowels("HELLO") == 2
        assert StringUtils.count_vowels("") == 0
        assert StringUtils.count_vowels(" ") == 0
        assert StringUtils.count_vowels("123") == 0
        assert StringUtils.count_vowels(None) == 0

    def test_is_palindrome(self):
        assert StringUtils.is_palindrome("madam") is True
        assert StringUtils.is_palindrome("racecar") is True
        assert StringUtils.is_palindrome("") is True
        assert StringUtils.is_palindrome(" ") is True
        assert StringUtils.is_palindrome("hello") is False
        assert StringUtils.is_palindrome(None) is True