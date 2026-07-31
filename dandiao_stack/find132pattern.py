from typing import List

class Solution:
    def find132pattern(self,n:int,nums:List[int])->bool:
        if n<3:
            return False

        min_candidate=[float("inf")]*n
        min_candidate[0]=nums[0]

        for i in range(1,n):
            min_candidate[i]=min(min_candidate[i-1],nums[i])

        stack=[]
        for k in range(n):
            while stack and nums[stack[-1]]<=nums[k]:
                stack.pop()

            if stack and min_candidate[stack[-1]]<nums[k]:
                return True
            stack.append(k)


        return False

def main():
    n=int(input())
    nums=list(map(int,input().split()))

    solution=Solution()
    ret=solution.find132pattern(n,nums)
    print("true" if ret else "false")
if __name__== "__main__":
    main()