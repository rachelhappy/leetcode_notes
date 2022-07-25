def getLength(head: ListNode) -> int:
  length = 0
  while head:
      length += 1
      head = head.next
  return length


# url：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/
