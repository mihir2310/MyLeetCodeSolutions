class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        list = s.split()
        final = list[-1]
        return len(final)
