class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        counter = 0
        answer = 0
        while counter < len(operations):
            if operations[counter][0] == "+":
                answer += 1
            elif operations[counter][-1] == "+":
                answer += 1
            elif operations[counter][0] == "-":
                answer -= 1
            elif operations[counter][-1] == "-":
                answer -= 1
            counter += 1
        
        return answer
