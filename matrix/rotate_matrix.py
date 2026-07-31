from typing import List
class Solution:
    def rotate(self,matrix:List[List[int]],n:int)->None:
        if n==0:
            return
        for i in range(n):
            for j  in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(n):
            matrix[i].reverse()




def main():

    n=int(input().strip())

    matrix=[list(map(int,input().split())) for _ in range(n)]

    solution=Solution()
    solution.rotate(matrix,n)

    for row in matrix:
        print(" ".join(map(str,row)))

if __name__ == "__main__":
    main()