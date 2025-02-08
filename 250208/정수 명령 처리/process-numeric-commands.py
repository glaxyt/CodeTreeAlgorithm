class Stack:
    def __init__(self):
        self.arr = []
    
    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if self.arr == 0:
            raise Exception("Stack is empty")

        last = self.arr.pop()
        print(last)

    def size(self):
        print(len(self.arr))
    
    def empty(self):
        if len(self.arr) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        print(self.arr[-1])


n = int(input())
st = Stack()
for i in range(n):
    orders = input().split()
    order = orders[0]
    if order == "push":
        st.push(orders[1])
    elif order == "size":
        st.size()
    elif order == "empty":
        st.empty()
    elif order == "pop":
        st.pop()
    elif order == "top":
        st.top()
    else:
        print("not valid order")