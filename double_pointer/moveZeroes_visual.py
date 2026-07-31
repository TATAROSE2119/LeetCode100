from typing import List

class Solution:
    def moveZeros(self,n:int,nums:List[int])->List[int]:
        if n==0:
            return []

        i=0
        j=0
        for i in range(n):
            if nums[i]==0:
                continue
            else:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
            
        return nums

def main():
    n=int(input())

    nums=list(map(int,input().split()))
    solution=Solution()
    ret=solution.moveZeros(n,nums)
    print(" ".join(map(str, ret)))

if __name__=="__main__":
    main()

