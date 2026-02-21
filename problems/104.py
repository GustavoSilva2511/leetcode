from classes import generate_binary_tree
from collections import deque
root = generate_binary_tree(from_array=[1,2,3,4,None,None,5])

def maxDepth(subtree):
    if subtree is None:
        return 0

    q = deque([subtree])
    level = 1
    l_level = 0
    r_level = 0

    while q:
        curr = q.popleft()
        
        if curr.left:
            l_level = maxDepth(curr.left)

        if curr.right:
            r_level = maxDepth(curr.right)

        level += max(l_level, r_level)

    return level

def _maxDepth(root):
    if root is None:
        return 0

    q = deque([root])


    while q:
        curr = q.popleft()
        curr_level += 1
        
        if curr.left is None and curr.right is None:
            max_level = max(max_level, curr_level)
            curr_level = 0

        if curr.left:
            q.append(curr.left)

        if curr.right:
            q.append(curr.right)

    return levels

print(maxDepth(root))