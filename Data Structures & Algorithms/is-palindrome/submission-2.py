class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(char for char in s if char.isalnum())
        print(result[::-1].lower())

        return result.lower() == result[::-1].lower()
        