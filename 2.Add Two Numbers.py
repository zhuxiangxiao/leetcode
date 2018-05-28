import json
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answers=[]
        carry=0
        sums=l1.val+l2.val
        if sums>=10:
            sums-=10
            carry=1
        else:
            carry=0
        tmp=ListNode(sums)
        result=tmp
        l1=l1.next
        l2=l2.next
        while l1 or l2 or carry:
            sums=carry
            if l1:
                sums+=l1.val
                l1=l1.next
            if l2:
                sums+=l2.val
                l2=l2.next
            if sums>=10:
                sums-=10
                carry=1
            else:
                carry=0
            tmp.next=ListNode(sums)
            tmp=tmp.next
        return result

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

l1=stringToListNode('[2,4,3]')
l2=stringToListNode('[2,4,3]')
print listNodeToString(Solution().addTwoNumbers(l1, l2))

        
