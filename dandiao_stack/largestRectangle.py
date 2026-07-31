"""
LeetCode 84. 柱状图中最大的矩形
给定 n 个非负整数，表示柱状图中每个柱子的高度，每个柱子宽度为 1。
求柱状图中能够勾勒出的最大矩形面积。

解法：单调递增栈
时间复杂度：O(n)
空间复杂度：O(n)
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        单调递增栈解法。

        核心思路：
        1. 维护一个单调递增栈（存下标，对应高度递增）
        2. 遍历每个柱子 + 末尾哨兵 0
        3. 当遇到比栈顶更矮的柱子时，弹出栈顶并以该高度计算矩形面积
           - 高度 = heights[pop]
           - 宽度 = 当前索引 - 新栈顶索引 - 1（或当前索引，若栈为空）
        4. 更新最大面积

        示例：heights = [2, 1, 5, 6, 2, 3]

        索引:  0  1  2  3  4  5  6(哨兵)
        高度:  2  1  5  6  2  3  0

        i=0: stack=[], push 0          → stack=[0]
        i=1: 1<2, pop 0: area=2×1=2, push 1  → stack=[1]
        i=2: 5>1, push 2              → stack=[1,2]
        i=3: 6>5, push 3              → stack=[1,2,3]
        i=4: 2<6, pop 3: area=6×1=6
             2<5, pop 2: area=5×2=10
             2>1, push 4              → stack=[1,4]
        i=5: 3>2, push 5              → stack=[1,4,5]
        i=6: 0<3, pop 5: area=3×1=3
             0<2, pop 4: area=2×4=8
             0<1, pop 1: area=1×6=6
             栈空, push 6             → stack=[6]
        """
        n = len(heights)
        stack: List[int] = []  # 存下标，对应高度单调递增
        max_area = 0

        # 遍历到 n（哨兵），确保最后所有柱子都会弹出计算
        for i in range(n + 1):
            # 当前高度，哨兵为 0
            h = heights[i] if i < n else 0

            # 维护单调递增：遇到更矮的柱子时弹出并计算
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # 宽度：当前索引到新栈顶之间的距离
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area


def main():
    heights = list(map(int, input().split()))
    solution = Solution()
    print(solution.largestRectangleArea(heights))


if __name__ == "__main__":
    main()
