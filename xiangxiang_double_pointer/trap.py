from typing import List

class Solution:
    def trap(self,n:int,height:List[int])->int:
        ans=0
        if n==0:
            return 0

        left=0
        right=n-1
        left_max,right_max=0,0
        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])
            if height[left]<height[right]:
                ans+=left_max-height[left]
                left+=1
            else:
                ans+=right_max-height[right]
                right-=1

        return ans

def main():
    n=int(input())
    height=list(map(int,input().split()))
    solution=Solution()
    print(solution.trap(n,height))

if __name__ == "__main__":
    main()
