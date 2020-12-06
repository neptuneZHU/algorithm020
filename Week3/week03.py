# -*- coding: utf-8 -*-
"""
Created on Sat Dec 05 22:08:16 2020
Week03 assignment
@author: zhuyuting
"""

#105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # separate with the root node, then build the left tree and right tree separately
        
        if not preorder or not inorder:
            return None
        
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        inorderIndex = inorder.index(rootVal)
        
        root.left = self.buildTree(preorder, inorder[:inorderIndex])
        root.right = self.buildTree(preorder, inorder[inorderIndex+1:])
        
        return root
    
    
# 236. Lowest Common Ancestor of a Binary Tree     
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        left = right = None
        
        if p == root or q == root or not root:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left:
            return right
        elif not right:
            return left
        else:
            return root
