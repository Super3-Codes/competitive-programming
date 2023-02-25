  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def reverse(head,left,right):

            prev = None
            current = head

            while(current and left != right+1):
                next = current.next
                current.next = prev
                prev = current
                current = next
                left = left + 1
        
            return [prev,current]
        
        count = 1
        dummy = ListNode(0,head)
        temp = dummy
        while(temp):
            if(count == left):
                print(count)
                x = reverse(temp.next,left,right)
                print(x)
                temp.next = x[0]
                
                while(temp.next != None):
                    temp = temp.next
                temp.next = x[1]
                break

            temp = temp.next
            count += 1
          
        return dummy.next
