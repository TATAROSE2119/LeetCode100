from typing import  List

class Solution:
    def coinChange(self,coins,amount)->int:
        n=len(coins)
        dp=[0]
        return  -1

def main():
    coins=list(map(int,input().split()))
    amount=int(input())
    print(Solution().coinChange(coins,amount))

if __name__ =="__main__":
    main()