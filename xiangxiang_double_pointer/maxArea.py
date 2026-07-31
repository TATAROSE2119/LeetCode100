from typing import List

class Solution:
    def maxArea(self,n:int, height: List[int]) -> int:
        if n==0:
            return 0

        left_pt=0
        right_pt=n-1

        ans=0
        while left_pt <right_pt:
            width=right_pt-left_pt
            a=width*min(height[left_pt],height[right_pt])
            ans=max(a,ans)

            if height[left_pt] <= height[right_pt]:
                left_pt+=1
            else:
                right_pt-=1


        return ans


def main():
    # 输入格式：第一行 n，第二行 n 个高度
    n = int(input())
    height = list(map(int, input().split()))

    solution = Solution()
    print(solution.maxArea(n,height))


if __name__ == "__main__":
    main()