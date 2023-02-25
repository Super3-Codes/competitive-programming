 def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerNodesHead = ListNode(-1)
        smallerNodes = smallerNodesHead
        greaterNodesHead = ListNode(-1)
        greaterNodes = greaterNodesHead

        temp = head
        while(temp):
            if(temp.val < x):
                smallerNodes.next = temp
                smallerNodes  = smallerNodes.next
            else:
                greaterNodes.next = temp
                greaterNodes = greaterNodes.next
            temp = temp.next
        greaterNodes.next = None
        smallerNodes.next = greaterNodesHead.next
        return smallerNodesHead.next
