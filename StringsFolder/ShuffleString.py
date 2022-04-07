class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict = {}
        counter = 0
        while counter < len(s):
            dict[indices[counter]] = s[counter]
            counter += 1

        string = ""
        counter = 0
        while counter<len(s):
            string += dict[counter]
            counter +=1
            
        return string
