from typing import List

class Solution:
    def permute(self,nums)->List[List[int]]:
        ans=[]
        path=[]
        n=len(nums)

        used=[False]*n

        def backtrace():
            if len(path)==n:
                ans.append(path[:])
                return
            for i in range(n):
                if used[i]==True:
                    continue
                path.append(nums[i])
                used[i]=True
                backtrace()
                path.pop()
                used[i]=False


        backtrace()
        return ans

def main():
    nums=list(map(int,input().split()))
    solution=Solution()
    ret=solution.permute(nums)
    for path in ret:
        print(" ".join(map(str, path)))

if __name__=="__main__":
    main()