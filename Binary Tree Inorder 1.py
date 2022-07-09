# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        stack = []
        values = []
        
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
                
            if stack == []:
                break
                
            node = stack.pop()
            values.append(node.val)
            node = node.right
            
        return values