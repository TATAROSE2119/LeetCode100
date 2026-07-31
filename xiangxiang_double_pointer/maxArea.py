from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        盛最多水的容器 - 相向双指针
        思路：左右指针向中间移动，每次移动较矮的一边
        因为面积由较矮的边决定，移动较高的边不会增加面积
        时间复杂度: O(n), 空间复杂度: O(1)
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # 当前面积 = 较矮高度 * 宽度
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            # 移动较矮的一边
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


def main():
    # 输入格式：第一行 n，第二行 n 个高度
    n = int(input())
    height = list(map(int, input().split()))

    solution = Solution()
    print(solution.maxArea(height))


if __name__ == "__main__":
    main()