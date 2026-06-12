from collections import deque


class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if node is None:
        return node

    cloned = {}
    q = deque([node])
    cloned.update({node.val: Node(node.val, [])})
    while q:
        curr = q.popleft()
        curr_clone = cloned.get(curr.val)
        for n in curr.neighbors:
            if not n.val in cloned:
                cloned.update({n.val: Node(n.val, [])})
                q.append(n)
            
            curr_clone.neighbors.append(cloned.get(n.val))

    return cloned.get(node.val)