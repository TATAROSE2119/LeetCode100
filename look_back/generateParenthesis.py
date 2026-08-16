from typing import List

class Solution:
    def generateParenthesis(self,n:int)->List[str]:
        ans=[]
        path=[]

        def backtrace(open_cnt:int,close_cnt:int,path:str):
            if open_cnt==n and close_cnt==n:
                ans.append(path)
                return
            if open_cnt < n:
                backtrace(open_cnt+1,close_cnt,path+"(")
            if close_cnt < open_cnt:
                backtrace(open_cnt,close_cnt+1,path+")")

        backtrace(0,0,"")
        return ans

def main():
    n=int(input().strip())
    solution=Solution()
    ret=solution.generateParenthesis(n)
    for path in ret:
        print(" ".join(path))

if __name__ == "__main__":
    main()