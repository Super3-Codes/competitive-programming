def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummyNode = ListNode(0)
        prevNode = dummyNode
        currNode = head

        while currNode and currNode.next:
            prevNode.next = currNode.next
            currNode.next = prevNode.next.next
            prevNode.next.next = currNode

            prevNode = currNode
            currNode = currNode.next
        return dummyNode.next
