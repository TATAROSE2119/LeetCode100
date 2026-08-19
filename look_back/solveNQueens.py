from typing import List

class Solution:
    def solveNQueens(self,n)->List[List[int]]:
        ans=[]
        board=[["."]*n for _ in range(n)]
        if n<=3:
            return []

        cols=set()
        diag1=set()
        diag2=set()
        def backtrack(row:int):
            if row==n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row -col) in diag1
        
        return ans

def main():
    n=int(input().strip)

    solution=Solution()
    ret=solution.solveNQueens(n)
    for path in ret:
        print(" ".join(path))

if __name__ == "__main__":
    main()