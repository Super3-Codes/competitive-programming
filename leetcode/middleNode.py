  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
            
        if head.next == None:
           return head
        
        slow = head
        fast = head
       
        while fast != None and fast.next != None:
           slow = slow.next
           fast = fast.next.next

        return slow
