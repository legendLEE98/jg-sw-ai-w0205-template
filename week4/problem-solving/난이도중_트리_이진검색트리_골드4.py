# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
import sys
from collections import deque

sys.setrecursionlimit(20000)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

input = sys.stdin.read().split()
inputValue = deque(map(int,input))

def makeTree(inputValue:deque, minimum, maximum):
    if not inputValue:
        return None
    
    if not (minimum < inputValue[0] < maximum):
        return None
    
    root = TreeNode(inputValue.popleft())
    # min 
    # 다음값이 최소한 미니멈보단 크면서, 현재값보단 작은거 
    root.left = makeTree(inputValue, minimum, root.val)
    # max
    # 다음 값이 최소한 현재보단 크면서, 맥시멈보단 작은 값
    root.right = makeTree(inputValue, root.val, maximum)

    return root

def postorder(root:TreeNode):
    resultList = []
    
    if root is None:
        return []
    
    resultList += postorder(root.left)
    resultList += postorder(root.right)
    resultList.append(root.val)
    
    return resultList
tree = makeTree(inputValue, 0, float("inf"))
result = postorder(tree)
for i in range(len(result)):
    print(result[i])