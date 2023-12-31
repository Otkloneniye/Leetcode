# faster than 70% 
from collections import deque
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = deque()
        
        pointer = head
        while pointer:
            a.append(pointer.val)
            pointer = pointer.next
        
        head1 = None
        while a:
            head1 = ListNode(a.popleft(), head1)
        
        return head1
