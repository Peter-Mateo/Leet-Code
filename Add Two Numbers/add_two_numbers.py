def iterate(list):
    reverbed = ""
    done = ""
    count = 0
    while (list):
        reverbed += str(list.val)
        count +=1
        list = list.next
    for numbers in reversed(reverbed):
        done += numbers      
    return int(done)
        
    return int(reverbed)

def breaks(string):
    final = SinglyLinkedList()
    for number in reversed(string):
        final.add(listNode(number))
    return final.head


class listNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list_1 = iterate(l1)
        list_2 = iterate(l2)
        combo = str(list_1 + list_2)
        return breaks(combo)
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        