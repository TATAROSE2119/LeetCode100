from typing import List

class Solution:
    def partition(self,s:str)->List[List[int]]:
        res=[]
        path=[]
        n=len(s)
        def is_palindrome(left:int,right:int)->bool:
            while left<right:    
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def backtrace(start:int):
            if start==n:
                res.append(path[:])
                return
            for i in range(start,n):
                if not is_palindrome(start,i):
                    continue

                path.append(s[start:i+1])
                backtrace(i+1)
                path.pop()

        backtrace(0)
        return res


def main():
    s=input().strip()
    solution=Solution()
    ret=solution.partition(s)
    for path in ret:
        print(" ".join(path))

if __name__ == "__main__":
    main()