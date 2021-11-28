class Solution:
    def customSortString(self, order: str, str: str) -> str:
        answer = ""
        for i in order:
            for j in str:
                if (i == j):
                    answer += i
        for i in str:
            if (i not in order):
                answer += i
        return answer