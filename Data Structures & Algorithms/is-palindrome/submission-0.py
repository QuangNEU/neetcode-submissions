class Solution:
    def isPalindrome(self, s: str) -> bool:
        validate_s = "".join(char.lower() for char in s if char.isalnum())
        return validate_s == validate_s[::-1]