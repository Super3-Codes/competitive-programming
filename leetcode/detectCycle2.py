def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                while(head != slow):
                    head = head.next
                    slow = slow.next
                return head
                
        return None
