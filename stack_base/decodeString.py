
class Solution:
    def decodeString(self,s:str)->str:
        stack=[]

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                sub_str=""
                while stack[-1] !='[':
                    sub_str=stack.pop()+sub_str

                stack.pop()

                multi=""
                while stack and stack[-1].isdigit():
                    multi=stack.pop()+multi

                stack.append( int(multi) * sub_str)



        return "".join(stack)
def main():
    s=input().strip()
    solution=Solution()
    ret=solution.decodeString(s)
    print(ret)

if __name__ == "__main__":
    main()