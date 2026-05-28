# Structure of binary tree node
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
'''

class Solution:
    def verticalSum(self, root):
        mp = {}

        def dfs(node, hd):
            if not node:
                return

            # Add node value to its vertical line sum
            mp[hd] = mp.get(hd, 0) + node.data

            # Traverse left and right subtree
            dfs(node.left, hd - 1)
            dfs(node.right, hd + 1)

        # Start traversal from root with horizontal distance 0
        dfs(root, 0)

        # Return sums from leftmost to rightmost
        return [mp[i] for i in sorted(mp)]