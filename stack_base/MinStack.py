

class MiniStack:
    def __init__(self):
        pass
    def push(self,val:int)->None:
        pass
    def pop(self)->None:
        pass
    def top(self)->int:
        return 0
    def getMin(self)->int:
        return 0

def main():
    q=int(input().strip())

    stack=MiniStack()

    for _ in range(q):
        parts=input().split()
        op=parts[0]
        if op =="push":
            stack.push(int[parts[1]])
        elif op =="pop":
            stack.pop()
        elif op=="top":
            print(stack.top())
        elif op=="getMin":
            print(stack.getMin())

if __name__ == "__main__":
    main()
