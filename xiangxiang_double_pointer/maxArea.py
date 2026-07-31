from typing import List

class Solution:
    def maxArea(self,n:int,height:List[int])->int :
        if n ==0:
            return 0



        return 0


def main():
    n=int(input())
    height=list(map(int,input().split()))

    solution=Solution()
    print(solution.maxArea(n,height))

if __name__=="__main__":
    main()