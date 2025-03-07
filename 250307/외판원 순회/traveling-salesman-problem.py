import sys

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize
answer = []
## 이건 MST 같은데.. 근데 사이클을 만드는 것이기 때문에 MST는 아니다.
## 아닌데 가장 마지막에 방문한 노드와 첫 방문한 노드와의 합으로 구할 수 있지않나?
## 아닌 것 같네 MST는 사이클이 없는 경로에서 최소한의 비용으로 방문할 때 쓰는 것이기 때문에
## 마지막 노드에서 첫 노드로 이동하는 경로를 더하면 그것이 최소한의 경로로 사이클을 만드는 것은 아니라고 생각
## 가장 짧은 길이는 어떻게 찾을건데..? 완전 탐색?
## 백트래킹을 통해서 모든 경로를 파악하기

def find_route(cur_node, cur_num):
    global ans

    ## 시도 3. 순회가 가능해야한다.
    if cur_num == n and A[cur_node][0] != 0:
        ans = min(ans, sum(answer) + A[cur_node][0])
        return
    
    ## cur_node의 이동할 수 있는 배열에서 for문 사용
    for next_node in range(n):
        if visited[next_node] or A[cur_node][next_node] == 0:
            continue

        answer.append(A[cur_node][next_node])
        visited[next_node] = True

        find_route(next_node, cur_num + 1)

        visited[next_node] = False
        answer.pop()
        
visited = [False for i in range(n)]

visited[0] = True
find_route(0, 1)

print(ans)


## 시도 2.
## 가지 못하는 간선도 존제한다.

## 시도 3.
## 순회를 할 수 있는가?