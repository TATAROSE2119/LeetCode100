from typing import List

class Solution:
    def combinationSum(self,n,target,candidates)->List[int]:
        ans=[]
        path=[]

        def backtracing(startIndex,remain):
            if remain==0:
                ans.append(path[:])
                return

            for i in range(startIndex,n):
                if candidates[i]>remain:
                    continue

                path.append(candidates[i])
                backtracing(i,remain-candidates[i])
                path.pop()

        backtracing(0,target)

        return ans

def main():
    n,target=map(int,input().split())
    candidates=list(map(int,input().split()))
    solution=Solution()
    ret=solution.combinationSum(n,target,candidates)
    for comb in ret:
        print(" ".join(map(str,comb)))

if __name__ == "__main__":
    main()