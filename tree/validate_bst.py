

class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None



def validate_bst(root, min_value=float('-inf'), max_value=float('inf')):
    if not root:
        return True
    elif not min_value < root.data < max_value:
        return False
    else:
        return (validate_bst(root.left, min_value, root.data) and 
                validate_bst(root.right, root.data, max_value))


if __name__ == '__main__':

    root = Node(5) 
    root.left = Node(1) 
    root.right = Node(4) 
    root.right.left = Node(3) 
    root.right.right = Node(6) 
    print(validate_bst(root))
