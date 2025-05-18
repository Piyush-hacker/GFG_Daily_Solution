class Solution:
    def findSpiral(self, root):
        if not root:
            return []
        
        result = []
        queue = []
        queue.append(root)
        level = 0
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.pop(0)
                level_nodes.append(node.data)
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add nodes to result based on level
            if level % 2 == 0:  # Even level: right to left
                result.extend(level_nodes[::-1])
            else:  # Odd level: left to right
                result.extend(level_nodes)
            
            level += 1
        
        return result

        #code here
        


#{ 
 # Driver Code Starts
from collections import deque


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    q = deque()

    # Push the root to the queue
    q.append(root)

    # Starting from the second element
    i = 1
    while q and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)

        i += 1
    return root


# Driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        result = ob.findSpiral(root)
        for value in result:
            print(value, end=" ")
        print()
        print("~")

# } Driver Code Ends