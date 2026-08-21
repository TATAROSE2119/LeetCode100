from typing import List
class Solution:
    def numIslands(self,m:int,n:int,grid:List[List[str]]) -> int:
        ans=0
        rows=len(grid)
        if rows==0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0

        if not grid or not grid[0]:
            return 0
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]

        def bfs(start_x,start_y):
            q=[(start_x,start_y)]
            grid[start_x][start_y]='0'

            head=0
            while head<len(q):
                x,y=q[head]
                head+=1

                for i in range(4):
                    newx=x+dx[i]
                    newy=y+dy[i]

                    if 0<=newx <rows and 0<=newy<cols and grid[newx][newy]=='1':
                        grid[newx][newy]='0'
                        q.append((newx,newy))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    ans+=1
                    bfs(i,j)

        return ans

def main():
    m,n=map(int,input().split())
    grid=[list(input().strip()) for _ in range(m)]
    print(Solution().numIslands(m,n,grid))

if __name__ == "__main__":
    main()