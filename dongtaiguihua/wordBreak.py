from typing import List

class Solution:
    def wordBreak(self,s,wordDict)->bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True

        for i in range(1,n+1):
            for j in range(i):

        
        return
    
def main():
    s=input().strip()
    wordDict=input().split()
    print(str(Solution().wordBreak(s,wordDict)).lower)
if __name__ == "__main__":
    main()