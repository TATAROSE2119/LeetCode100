from typing import List

class Solution:
    def dailyTemperatures(self,n:int,temperatures:List[int])->List[int]:
        ans=[0]*n#保存天数答案
        stack=[]#日期的索引

        for i,t in enumerate(temperatures):
            while stack and t>temperatures[stack[-1]]:
                prev_index=stack.pop()
                ans[prev_index]=i-prev_index
            stack.append(i)
        return ans
                
def main():
    n=int(input())
    temperatures=list(map(int,input().split()))
    solution=Solution()
    ret=solution.dailyTemperatures(n,temperatures)
    print(" ".join(map(str,ret)))

if __name__ == "__main__":
    main()