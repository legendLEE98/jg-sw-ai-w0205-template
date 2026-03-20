# 구체적으로 어떻게 하는가?
# 내려 올 때 현재 노드의 위치를 기록함
# curDepth (이거 필요한가)
# maxDepth

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(15)
root.right.right = TreeNode(7)

def depthCheck(tree, depth):
    if tree is None:
        return depth
    
    depth += 1
    depth1 = depthCheck(tree.left, depth)
    depth2 = depthCheck(tree.right, depth)

    return max(depth1, depth2)
