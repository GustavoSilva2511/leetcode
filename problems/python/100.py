# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
from classes import TreeNode, BinaryTree, generate_binary_tree

def dfs(self, node: TreeNode):
    if node is None:
        return [None]
    
    return [node.val] + self.dfs(node.left) + self.dfs(node.right)

def isSameTree(p: TreeNode, q: TreeNode):
    bt = BinaryTree()
    if p is None and q is None: return True
    if p is None or q is None: return False
    
    p_dfs = bt.dfs(p)
    q_dfs = bt.dfs(q)

    return p_dfs == q_dfs

# a1 = generate_binary_tree(20)
# a2 = generate_binary_tree(20)

a1 = TreeNode(1)
a1.left = TreeNode(2)

a2 = TreeNode(1)
a2.right = TreeNode(2)

print(isSameTree(a1, a2))
    