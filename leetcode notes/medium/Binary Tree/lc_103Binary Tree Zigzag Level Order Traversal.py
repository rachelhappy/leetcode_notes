# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #import collections  错误不能这么用
        lis = []
        if root is None:
            return lis
        # lis = []
        q = collections.deque()
        q.append(root)
        #q =deque([root])
        #l = []    #l的位置不应该在这里，应该在下面，每次for之前得保证l是一个空list
        is_left_to_right = True    #不能true = is_left_to_right 
        while q:
            l = []
            # 另一种写法，都可lenth = len(q)
            for i in range(len(q)):
                note = q.popleft()
                # print(q)
                l.append(note.val)
                if note.left:
                    q.append(note.left)   #这里是一个node，不是root
                if note.right:
                    q.append(note.right)
            if is_left_to_right is not True:
                l.reverse()
            is_left_to_right = not is_left_to_right
            lis.append(l)
        return lis
