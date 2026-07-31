from typing import List

class Solution:
    def quickSort(self,nums:List[int],l_pointer:int,r_pointer:int)->None:
        if l_pointer>=r_pointer:
            return
        x=nums[r_pointer]

        i=l_pointer

        for j in range(l_pointer,r_pointer):
            if nums[j]<=x:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1

        nums[i],nums[r_pointer]=nums[r_pointer],nums[i]

        self.quickSort(nums,l_pointer,i-1)
        self.quickSort(nums,i+1,r_pointer)

def main():
    n=int(input())
    nums=list(map(int,input().split()))
    solution=Solution()
    solution.quickSort(nums,0,n-1)
    print(" ".join(map(str,nums)))

if __name__ == "__main__":
    main()
