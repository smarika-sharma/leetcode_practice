from typing import Optional

class ListNode():
    def __init__(self, data, next=None):
        self.data= data
        self.next= next
    
    def __str__(self):
        # Print all values in the linked list in a nice format
        result = []
        current = self
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)

class Solution():

    def addTwoNumbers(self, l1:Optional[ListNode],l2:Optional[ListNode])-> Optional[ListNode]:

        head= ListNode(0)
        current_ptr= head

        carry=0

        while(l1 or l2):
            sum= 0+carry
            if (l1):
                sum= sum + l1.data
                l1= l1.next
            if (l2):
                sum= sum+ l2.data
                l2= l2.next
            
            # Use integer division to get carry's value in int and not float
            carry= sum//10  
            sum= sum%10

            current_ptr.next= ListNode(sum)
            current_ptr= current_ptr.next
        
        if (carry==1 or carry>1):
            current_ptr.next= ListNode(carry)
            
        return head.next

sol= Solution()

# creating l1
l1= ListNode(9)
head=l1
current=l1
current.next= ListNode(8)
current= current.next
current.next= ListNode(0)
current= current.next
current.next= ListNode(6)
current= current.next
current.next= ListNode(4)
current= current.next
print(f"The linked list 1 is {l1}")

# creating l2
l2= ListNode(2)
head=l2
current=l2
current.next=ListNode(2)
current=current.next
current.next=ListNode(4)
current=current.next
print(f"The linked list 2 is {l2}")

result= sol.addTwoNumbers(l1,l2)
print(f"The sum of two linked list is {result}")



        
            
