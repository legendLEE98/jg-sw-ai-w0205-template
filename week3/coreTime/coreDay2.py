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
        default = ListNode(0)
        current = default

        current1 = l1
        current2 = l2

        carry = 0
        while current1 is not None or current2 is not None or carry != 0:
            # 삼항연산자 로직
            # value1 = current1.val if current1 is not None else 0
            # value2 = current2.val if current2 is not None else 0
            
            if current1.val is not None:
                value1 = current1.val
            else:
                value1 = 0

            if current2.val is not None:
                value2 = current2.val
            else:
                value2 = 0

            value = value1 + value2 + carry
            carry = 0
            if value >= 10:
                value -= 10
                carry += 1
            
            current.next = ListNode(value)
            current = current.next

            current1 = current1.next if current is not None else None
            current2 = current2.next if current is not None else None

        return default.next

            

        
        # 링크드 리스트의 특성,
        # 처음 값 부터 시작 함.

        # ListNode{val: 4, next: ListNode{val: 3, next: None}}