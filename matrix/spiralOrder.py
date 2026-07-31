from typing import List

# from markdown import markdown


class Solution:
    def spiralOrder(self,matrix:List[List[int]],m:int,n:int)->List[int]:
        if not matrix:
            return []
        top,bottom=0,m-1
        left,right=0,n-1
        ans=[]
        while top <=bottom and left<=right:
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            top+=1

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1

            if top<=bottom and left<=right:
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                bottom-=1
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1

        return ans
def main():
    #读取行列
    m,n=map(int,input().split())
    matrix=[list(map(int,input().split())) for _ in range(m)]

    solution=Solution()
    result=solution.spiralOrder(matrix,m,n)

    print(" ".join(map(str,result)))

if __name__ == "__main__":
    main()
