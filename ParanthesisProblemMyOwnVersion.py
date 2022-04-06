class Solution:
    def isValid(self, s: str) -> bool:
        openlist = ["[","{", "("]
        closelist = ["]","}", ")"]
        counter = int(0)
        
        for n in range(len(closelist)): #Edge Cases
            if s[counter] == closelist[n]:
                return False
        for n in range(len(openlist)):
            if s[-1] == openlist[n] :
                return False
    
        if len(s)>1: 
            if len(s)%2 == 0:
                for n in range(len(s)):
                    for i in range(len(openlist)):
                        if s[2*n] == openlist[i]:
                            if s[(2*n)+1] == closelist[i]:
                                return True
                            else:
                                return False
                        else:
                            return False
            
            else: #Edge Case
                return False
        else:
            return False
