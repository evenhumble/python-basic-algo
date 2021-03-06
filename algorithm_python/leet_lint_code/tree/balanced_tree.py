# -*- coding:utf-8 -*-

"""
# Questions

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left is None and root.right is None:
            return True
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return abs(self.depth(root.left) - self.depth(root.right)) <= 1
            else:
                return False

    def depth(self, node):
        if node is None: return -1
        return max(self.depth(node.left), self.depth(node.right)) + 1

    def isBalanced_new(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            if self.height(root) != -1:
                return True
            else:
                return False

    def height(self, root):
        # Return -1 if not balanced
        if root is None:
            return 0
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            if left_height == -1 or right_height == -1:
                return -1
            else:
                if abs(left_height - right_height) <= 1:
                    return max(left_height, right_height) + 1
                else:
                    return -1
