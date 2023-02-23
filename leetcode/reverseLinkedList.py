class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        
        prev = None

        while slow:
            next = slow.next
            slow.next  = prev
            prev = slow
            slow = next
        
        

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False 
            left = left.next 
            right = right.next
        return True
