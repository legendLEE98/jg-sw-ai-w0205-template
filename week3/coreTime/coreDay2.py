# 두 개의 비어 있지 않은 연결 리스트가 주어지는데, 
# 이 리스트들은 각각 음수가 아닌 정수를 나타냅니다. 
# 숫자는 역순으로 저장되어 있으며, 각 노드에는 한 자리 숫자만 있습니다. 
# 두 숫자를 더하고 그 합을 연결 리스트 형태로 반환하세요.

# 두 숫자에는 0을 제외하고 앞에 0이 없다고 가정합니다.

# 예시 1:
# 입력: 
# 출력: [7,0,8]
# 설명: 342 + 465 = 807.

# 예시 2:
# 입력: l1 = [0], l2 = [0]
# 출력: [0]

# 예시 3:
# 입력: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 출력: [8,9,9,9,0,0,0,1]

# 제약 조건:

# 각 연결 리스트의 노드 개수는 [1, 100] 범위 내에 있어야 합니다.

# 0 <= Node.val <= 9
# 리스트에 포함된 숫자는 앞에 0이 없어야 합니다.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currentl1 = l1.val
        currentl2 = l2.val

        result = []
        # for문 밖
        carry = 0
        for i in range(max(l1, l2)):
            currentValue = currentl1 + currentl2 + carry

            if currentValue >= 10:
                carry += 1
                currentValue -= 10
            
            currentl1 = currentl1.next
            currentl2 = currentl2.next

            result.append(currentValue)
            
        
        # 링크드 리스트의 특성
        # 처음 값 부터 시작 함.

        # ListNode{val: 4, next: ListNode{val: 3, next: None}}