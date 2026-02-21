from collections import deque


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class BinaryTree():
    def dfs(self, node: TreeNode):
        if node is None:
            return [None]
        
        return [node.val] + self.dfs(node.left) + self.dfs(node.right)

    def bfs(self, node: TreeNode):
        if not node:
            return []
        stack = deque()
        stack.append(node)
        result = []
        
        while len(stack) > 0:
            curr: TreeNode = stack.popleft()
            result.append(curr.val)
            
            if curr.left:
                stack.append(curr.left)
            else:
                stack.append(None)

            if curr.right:
                stack.append(curr.right)
            else:
                stack.append(None)
        return result

def generate_binary_tree(size=None, from_array=None):
    # Se receber apenas o tamanho, gera um array sequencial simples
    if size is not None and from_array is None:
        from_array = list(range(1, size + 1))
    
    if not from_array:
        return None

    # O primeiro elemento é sempre a raiz
    root = TreeNode(from_array[0])
    queue = deque([root])
    i = 1
    
    # Percorre o array e a fila simultaneamente para conectar os nós
    while queue and i < len(from_array):
        current = queue.popleft()
        
        # Filho à esquerda
        if i < len(from_array) and from_array[i] is not None:
            current.left = TreeNode(from_array[i])
            queue.append(current.left)
        i += 1
        
        # Filho à direita
        if i < len(from_array) and from_array[i] is not None:
            current.right = TreeNode(from_array[i])
            queue.append(current.right)
        i += 1
            
    return root