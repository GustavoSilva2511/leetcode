

from collections import deque


class NodeTree:
    def __init__(self, val):
        self.val = val
        self.left: NodeTree = None
        self.right: NodeTree = None

class BinaryTree:
    def dfs(self, node: NodeTree):
        if node is None:
            return []
        
        return [node.val] + self.dfs(node.left) + self.dfs(node.right)

    def bfs(self, node: NodeTree):
        if not node:
            return []
        stack = deque()
        stack.append(node)
        result = []
        
        while len(stack) > 0:
            curr: NodeTree = stack.popleft()
            result.append(curr.val)
            
            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        return result



raiz = NodeTree(1)
raiz.left = NodeTree(2)
raiz.left.left = NodeTree(4)
raiz.left.right = NodeTree(5)
raiz.right = NodeTree(3)
raiz.right.left = NodeTree(6)
raiz.right.right = NodeTree(7)

bt = BinaryTree()

print(bt.dfs(raiz))
print(bt.bfs(raiz))