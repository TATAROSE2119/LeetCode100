from typing import List

class Solution:
    def solveNQueens(self,n)->List[List[int]]:
        ans=[]
        path=[]
        if n<=3:
            return []

        
        return ans

def main():
    n=int(input().strip)

    solution=Solution()
    ret=solution.solveNQueens(n)
    for path in ret:
        print(" ".join(path))

if __name__ == "__main__":
    main()