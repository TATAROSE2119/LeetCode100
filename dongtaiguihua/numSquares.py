class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n+1]*(n+1)
        dp[0]=0
         
        for i in range(1,n+1):
            j=1
            while j*j<=i:
                square=j*j
                remain=i-square
                candidate=dp[remain]+1
                if candidate<dp[i]:
                    dp[i]=candidate
                j+=1
        return dp[n]
                 


def main():
    n = int(input())
    print(Solution().numSquares(n))


if __name__ == "__main__":
    main()
