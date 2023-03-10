 def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fast = head
        slow = head

        while(fast != None and fast.next != None):
            
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        return False
