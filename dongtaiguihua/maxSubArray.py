from typing import List

class Solution:
    def maxSubArray(self,n:int,nums:List[int])->int:
        dp=[0]*n
        dp[0]=nums[0]

        ans=nums[0]
        for i in range(1,n):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            ans=max(ans,dp[i])
        return ans

def main()->None:
    n=int(input().strip())
    nums=list(map(int,input().split()))
    solution=Solution()
    ret=solution.maxSubArray(n,nums)
    print(ret)

if __name__=="__main__":
    main()