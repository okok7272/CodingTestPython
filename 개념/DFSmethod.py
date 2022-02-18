# DFS의 형태와 구현하기
# 일단 깊이 탐색은 이중트리형태에서 보면 루트 노드에서 탐색을 시작한다고 가정하자
# 탐색 대상이 루트 바로 아래 노드 첫번째 것이 아니면 자신의 형제 노드를 탐색하지 않고
# 자신의 자식 노드부터 탐색하는 방식을 말한다.

##탐색할 그래프
graph = dict()
#graph는 dictionary 구조를 가진다.

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']
###################

#list로 구현
def DFS(graph, startNode):

    #미방문노드 리스트
    notVisited = list()
    #방문노드리스트
    visited = list()

    #아직 시작노드 미방문이니 시작노드 미방문 노드에 입력
    notVisited.append(startNode)

    #미방문 노드 리스트 반복문 시작부터 끝까지
    while notVisited:

        #pop은 삭제할 대상을 출력하고 감
        node = notVisited.pop()

        #만약 그 노드가 아직 visited 리스트에 있지 않다면
        if node not in visited:

            #이제 방문하니까 추가해주고
            visited.append(node)

            #해당 노드와 연결된 하위노드로 notVisit 리스트 확장
            notVisited.extend(graph[node])

    return visited

#단점 list의 pop은 좋지 않은 방법임

#이제 collection의 deque를 이욯해보자
def DFSdeque(graph, startNode):

    from collections import deque

    visited = []

    notVisited = deque()

    notVisited.append(startNode)

    while notVisited:

        node = notVisited.popleft()

        if node not in visited:

            visited.append(node)

            notVisited.extend(graph[node])

    return visited

#재귀함수 이용
def DFSrecur(graph, startNode, visited = []):
    visited.append(startNode)

    for node in graph[startNode]:
        if node not in visited:
            DFSrecur(graph, node, visited)

    return visited


def main():

    DFS(graph,'A')

if __name__ == "__main__":
    main()

