  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        temp = mergedList
        
        while list1 and list2:
            if list1.val >= list2.val:
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
            else:
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next
                
        if list1 is None:
            temp.next = list2
        elif list2 is None:
            temp.next = list1
            
        return mergedList.next
