from typing import List

class Solution:
    def letterCombinations(self,digits:str)->List[str]:
        ans=[]
        map={
            "2": "abc", "3": "def",  "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        path=[]
        n=len(digits)
        if n == 0:
            return[]

        def backtracek(index:int):
            if index==n:
                ans.append("".join(path))
                return
            for char in map[digits[index]]:
                 path.append(char)
                 backtracek(index+1)
                 path.pop()

        backtracek(0)
        return ans

def main()->None:
    digits=input().strip()
    solution=Solution()
    ret=solution.letterCombinations(digits)
    print(" ".join(ret))

if __name__ == "__main__":
    main()