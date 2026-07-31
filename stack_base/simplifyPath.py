class Solution:
    def simplifyPath(self,path:str)->str:
        stack=[]
        if path is None:
            return ""

        path_after_split=path.split('/')
        for part in path_after_split:
            if part == '..':
                if stack:
                    stack.pop()
            elif part=='.':
                continue
            elif part:
                stack.append(part)
        return '/'+'/'.join(stack)

def main():
    path=input().strip()
    solution=Solution()
    ret=solution.simplifyPath(path)
    print(ret)

if __name__ == "__main__":
    main()