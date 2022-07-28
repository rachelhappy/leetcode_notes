# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxdep = 0
        self.curdep(root,1)
        return self.maxdep   #为什么这里return又有self了呢
    def curdep(self,root,height):
        if root is None:
            return
        self.maxdep = max(height,self.maxdep) #为什么此行放在这，如果顺序倒了对不对？

        self.curdep(root.left,height+1)
        self.curdep(root.right,height+1)  #root.right前面为什么不加self？ 是否是调用函数就不用self了呢？否

        #为什么两个def是平行的？
        #self问题统一解答：因为再一个class里面def(self,)和self.意味着跟这个函数和变量都是在同一个class下可以被调用的，缺一不可
