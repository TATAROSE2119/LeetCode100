from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 表示凑成金额 i 所需的最少硬币数
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1


def main() -> None:
    coins = list(map(int, input().split()))
    amount = int(input())
    print(Solution().coinChange(coins, amount))


if __name__ == "__main__":
    main()
