    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        mainNode = ListNode(0)
        node = mainNode

        while head:
            isDuplicate = False
            while(head.next and head.val == head.next.val):
                isDuplicate = True
                head = head.next
            if not isDuplicate:
                node.next = head
                node = node.next
                head = head.next
                node.next = None
            else:
                head =  head.next
        return mainNode.next
