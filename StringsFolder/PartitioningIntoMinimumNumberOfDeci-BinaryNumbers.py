class Solution:
    def minPartitions(self, n: str) -> int:
        answer = 0
        counter = 0
        while counter < len(n):
            if int(n[counter])> answer:
                answer = int(n[counter])
            counter+=1
        return answer
