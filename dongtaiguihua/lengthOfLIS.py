from typing import List

class Solution:
    def lengthOfLIS(self,nums:List[int])->int:
        n=len(nums)
        dp=[1]*n
        ans=1
        for i in range(0, n):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
            ans=max(ans,dp[i])
        return ans

def main()->None:
    nums=list(map(int,input().split()))
    print(Solution().lengthOfLIS(nums)) 

if __name__ == "__main__":
    main()