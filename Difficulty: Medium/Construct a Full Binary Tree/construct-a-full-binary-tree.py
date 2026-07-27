class Solution:
    def constructBinaryTree(self, pre, preMirror):
        i, j = 0, len(pre) - 1

        def construct():
            nonlocal i, j

            if pre[i] == preMirror[j]:
                root = Node(pre[i])
                i += 1
                j -= 1
                return root

            root = Node(pre[i])
            i += 1
            root.left = construct()
            root.right = construct()
            j -= 1
            return root

        return construct()
