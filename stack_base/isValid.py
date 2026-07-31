from inspect import stack


class Solution:
    def isValid(self,s:str)->bool:
        if not s:
            return True
        stack=[]
        map={")":"(",
            "}":"{",
            "]":"["}
        for char in s:
            if char in map:
                if not stack:
                    continue
                top_element=stack.pop()
                if map[char]!=top_element:
                    return False
            else:
                stack.append(char)

        return not stack

def main():
    s=input().strip()
    solution=Solution()
    ret=solution.isValid(s)
    print("true" if ret else "false")
if __name__ == "__main__":
    main()