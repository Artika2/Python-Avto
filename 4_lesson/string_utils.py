class StringUtils:

    @staticmethod
    def capitalize_string(s: str) -> str:
        if not s:
            return s
        return s[0].upper() + s[1:].lower() if len(s) > 0 else s

    @staticmethod
    def reverse_string(s: str) -> str:
        return s[::-1]

    @staticmethod
    def count_vowels(s: str) -> int:
        vowels = "AEIOUYaeiouy"
        return sum(1 for char in s if char in vowels)

    @staticmethod
    def is_palindrome(s: str) -> bool:
        s = s.lower().replace(" ", "")
        return s == s[::-1]