# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#       res = ListNode()
#       i = 0
#       j = 0
#       k = 0
#       while(l1.val != None):
#         if(l1.val[i] < l2.val[j]):
#         else: 
#           res.val.append(l2.val[j])
#       return res

def node(n):
  if(n.next == None):
    return n.val
  return n.val + node(n.next)

# n1 = ListNode(0)
# n2 = ListNode(1)
# n3 = ListNode(2)
# n1.next = n2
# n2.next = n3
# print(node(n1))

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
a = 1
b = 0
ab = a or b
print(ab)
test = Solution()
l1 = ListNode([1,2,4])
l2 = ListNode([1,3,4])
res = test.mergeTwoLists(l1, l2)
print(node(res))