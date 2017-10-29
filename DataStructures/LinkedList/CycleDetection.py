"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head == None:
        return False
    
    slow = head
    fast = head
    
    while (fast != None and fast.next != None):
        # use a slow to walk one step each time
        # use a fast to walk two steps each time
        # if they meet, it means there must be a cycle
        slow = slow.next
        fast = fast.next.next
        
        if(slow == fast):
            return True
    return False
    
    

