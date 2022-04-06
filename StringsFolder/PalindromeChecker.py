import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        acceptablecharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        s.lower()
        for i in string.punctuation:
            s = s.replace(i,"").lower()
            s = s.replace(" ",'')
            
        if s[-1::-1] == s[0:len(s):1]:
            return True
        else:
            return False
