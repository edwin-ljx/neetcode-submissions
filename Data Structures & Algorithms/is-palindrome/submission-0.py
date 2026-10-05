class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove = []
        strlist = [v.lower() for v in s if v.isalnum()]
        return strlist[::-1] == strlist

