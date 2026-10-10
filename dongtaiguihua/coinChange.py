from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0

        for current_amount in range(1,amount+1):
            for coin in coins:
                if coin<=current_amount:
                    remaining_amount=current_amount-coin
                    count_for_remaining=dp[remaining_amount]

                    count_if_use_this_coin=count_for_remaining+1
                    # if count_if_use_this_coin<dp[current_amount]:
                    #     dp[current_amount]=count_if_use_this_coin
                    dp[current_amount]=min(dp[current_amount],count_if_use_this_coin)
        if dp[amount]==amount+1:
            return -1
        
        return dp[amount]


def main() -> None:
    coins = list(map(int, input().split()))
    amount = int(input())
    print(Solution().coinChange(coins, amount))


if __name__ == "__main__":
    main()
