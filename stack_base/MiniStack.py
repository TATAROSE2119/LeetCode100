class MinStack:
    def __init__(self):
        # 请在这里初始化最小栈
        self.stack=[]

    def push(self, val: int) -> None:
        # 请在这里实现 push 操作
        if not self.stack:
            self.stack.append((val,val))
        else:
            current_min=self.stack[-1][-1]
            new_min=min(val,current_min)
            self.stack.append((val,new_min))

    def pop(self) -> None:
        # 请在这里实现 pop 操作
        self.stack.pop()

    def top(self) -> int:
        # 请在这里实现 top 操作
        return self.stack[-1][0]

    def getMin(self) -> int:
        # 请在这里实现 getMin 操作
        return self.stack[-1][-1]


def main():
    # 读取操作次数
    q = int(input().strip())

    # 创建最小栈对象
    stack = MinStack()

    # 依次处理每个操作
    for _ in range(q):
        parts = input().split()
        op = parts[0]

        if op == "push":
            stack.push(int(parts[1]))
        elif op == "pop":
            stack.pop()
        elif op == "top":
            print(stack.top())
        elif op == "getMin":
            print(stack.getMin())


if __name__ == "__main__":
    main()
