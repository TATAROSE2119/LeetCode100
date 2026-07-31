from typing import List



class Solution:
    def searchMatrix(self,m:int,n:int,matrix:List[List[int]],target:int)->bool:
        if not matrix or not matrix[0]:
            return False

        start_row=0
        start_col=n-1
        while 0<=start_row<m and 0<=start_col<n:
            current=matrix[start_row][start_col]
            if target<current:
                start_col-=1
            elif target>current:
                start_row+=1
            else:
                return True

        return False

def main():
    m,n=map(int,input().split())

    matrix=[list(map(int,input().split())) for _ in range(m)]

    target=int(input().strip())

    solution=Solution()
    result=solution.searchMatrix(m,n,matrix,target)

    print("true" if result else "false")


if __name__ == "__main__":
    main()