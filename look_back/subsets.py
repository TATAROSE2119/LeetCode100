import sys
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        curr=[]
        def dfs(index):
            if index == n:
                res.append(curr[:])
                return
        
            curr.append(nums[index])
            dfs(index+1)

            curr.pop()
            dfs(index+1)


        dfs(0)

        return res


def main() -> None:
    data = input().strip().split()
    nums = list(map(int, data))

    solution = Solution()
    ans = solution.subsets(nums)

    for subset in ans:
        if len(subset) == 0:
            continue
        print(" ".join(map(str, subset)))


if __name__ == "__main__":
    main()
