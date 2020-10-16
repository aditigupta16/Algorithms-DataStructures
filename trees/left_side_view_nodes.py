
class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


def left_view(root):
    queue = []
    left_view_nodes = []
    if not root:
        return left_view_nodes
    queue.append(root)
    while queue:
        left_view_nodes.append(queue[0].data)
        for i in range(0,len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    print(left_view_nodes)


if __name__ == '__main__':

    root = Node(12) 
    root.left = Node(10) 
    root.right = Node(20) 
    root.right.left = Node(25) 
    root.right.right = Node(40) 
    left_view(root) 
