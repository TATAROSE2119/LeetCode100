from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 请在这里实现
        return -1


def main() -> None:
    coins=list(map(int,input().split()))
    amount=int(input())
    print(Solution().coinChange(coins,amount))

if __name__ == "__main__":
    main(   )