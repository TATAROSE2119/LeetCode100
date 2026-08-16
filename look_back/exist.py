from typing import List

class Solution:
    def exist(self,m,n,matrix,word)->bool:
        length=len(word)
        def backtrack(r,c,k)->bool:
            if r<0 or r >=m or c<0 or c>= n or matrix[r][c]!=word[k]:
                return False
            if k==length-1:
                return True

            temp=matrix[r][c]
            matrix[r][c]="#"

            found=(
                backtrack(r+1,c,k+1) or 
                backtrack(r-1,c,k+1) or 
                backtrack(r,c+1,k+1) or
                backtrack(r,c-1,k+1)
            )
            matrix[r][c]=temp

            return found

        for r in range(m):
            for c in range(n):
                if word[0]==matrix[r][c]:
                    if backtrack(r,c,0):
                        return True

        return False

def main():
    m,n=map(int,input().split())
    matrix=[input().strip().split() for _ in range(m)]
    word=input().strip()

    solution=Solution()
    ret=solution.exist(m,n,matrix,word)
    print("true" if ret else "false")

if __name__ == "__main__":
    main()