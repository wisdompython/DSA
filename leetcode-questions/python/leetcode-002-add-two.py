# a single linked list consists of nodes which have 2 parts:  a data value and a pointer to the next node, the last node points null
from typing import *


class ListNode:

    def __init__(self, val):

        self.data = val
        self.next = None
    
    # creating a function to transverse:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def transverse_transform(l:Optional[ListNode]):
    a = []
    current = l
    for i in range(100):

        if current.val == None:
            break
        
        else:
            a.append(current.val)

            if current.next == None:
                break

            current = current.next
        
    # convert into string
    print(a)
    a= reversed(a)
    a = "".join(map(str,a))
    print(int(a))
    return int(a)


def update_node(l_next, val):
    res_next = ListNode()
    res_next.val = val

    
    return res_next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    

        res = str(transverse_transform(l1) + transverse_transform(l2))
        res = list(map(int, res))
        res = list(reversed(res))
        
        current = ListNode()
        curr_res = current

        current.val = res[0]
        for i in range(1, len(res)):
            if i == len(res):
                break       
            print(res[i])
            current.next = ListNode(res[i])
            current = current.next    
        return curr_res





        
## optimized solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        current = ListNode(0)

        head_point = current
        rem = 0
        print(l2.val)
        while l1 or l2 or rem:
            v1 = (l1.val if l1 else 0 )
            v2 = (l2.val if l2 else 0 )
            
            #carry the remainder 
            rem, out = divmod((v1 + v2 + rem), 10)

            
            current.next = ListNode(out)
            current = current.next
            

            # move to the next node until it reaches none

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return head_point.next 

    




        


        
        