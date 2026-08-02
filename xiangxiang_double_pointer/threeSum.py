from typing import List

class Solution:
    def threeSum(self,n:int,nums:List[int])->List[List[int]]:
        nums.sort()
        return

def main():
    n=int(input())
    nums=list(map(int,input().split()))
    solution=Solution()
    res=solution.threeSum(n,nums)
    for triple in res:
        print(*triple)

if __name__ == "__main__":
    main()