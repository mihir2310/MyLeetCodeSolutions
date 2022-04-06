class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        counter = 0
        answer = 0
        while counter < len(sentences):
            newlist = sentences[counter].split()
            if len(newlist) > answer:
                answer = len(newlist)
                counter +=1

            else:
                counter +=1
        return answer
        
