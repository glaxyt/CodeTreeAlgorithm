class stack:
    def init():
        arr = []
    
    def push(num):
        arr.push(num)

    def pop(num):
        last = arr.pop()
        print(last)

    def size(num):
        print(len(arr))
    
    def empty():
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    def top():
        print(arr[-1])


n = int(input())
st = stack()
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
    elif order = "top":
        st.top()
    else:
        print("not valid order")