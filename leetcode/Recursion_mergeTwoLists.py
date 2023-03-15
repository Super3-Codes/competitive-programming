 def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val > list2.val:
                head = list2
                list2 = list2.next
            else:
                head = list1
                list1 = list1.next
            head.next = self.mergeTwoLists(list1,list2)
            return head
                
        else:
            return list1 or list2
