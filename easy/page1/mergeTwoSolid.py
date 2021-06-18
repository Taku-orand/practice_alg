# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      res = ListNode([])
      i = 0
      j = 0
      k = 0
      while(l1.val[i] != None):
        if(l1.val[i] < l2.val[j]):
          res.val.append(l1.val[i])
          i += 1
        else: 
          res.val.append(l2.val[j])
          j += 1
      return res

l1 = ListNode([1,2,4])
l2 = ListNode([1,3,4])
print(l1.val[3] == None)

test = Solution()
res = test.mergeTwoLists(l1, l2)
#print(res.val)