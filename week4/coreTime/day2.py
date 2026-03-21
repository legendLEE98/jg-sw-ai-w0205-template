# 레벨 별 노드의 평균 값

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# if root.val is not None:
#     print("안녕하세요")

resultR = []
def levelAvg(tree:TreeNode):
    if tree is None:
        return 0
    
    leftVal = levelAvg(tree.left)
    rightVal = levelAvg(tree.right)

    if rightVal == 0 or leftVal == 0:
        avg = (leftVal + rightVal) / 1
    else:
        avg = (leftVal + rightVal) / 2

    if avg != 0:
        resultR.append(avg)

    return tree.val

levelAvg(root)

resultR.append(root.val)

result = []
for i in range(len(resultR) -1 , -1, -1):
    result.append(resultR[i])
print(result)