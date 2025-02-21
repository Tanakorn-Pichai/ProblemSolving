# Inorder traversal

# Left -> Root -> Right

def inorderTraversal (self, root):

    res = []

    if root:

        res = self.inorderTraversal(root.left)

    res.append(root.data)

    res = res + self.inorderTraversal(root.right)

    return res

# Preorder traversal

# Root -> Left ->Right

def PreorderTraversal (self, root):

    res = []

    if root:

        res.append(root.data)

        res = res + self.PreorderTraversal(root.left)

        res = res + self. PreorderTraversal(root.right)

    return res
# Postorder traversal

# Left ->Right -> Root

def PostorderTraversal (self, root):

    res = []

    if root:

        res = self. PostorderTraversal(root.left)

        res = res + self. PostorderTraversal(root.right)

        res.append(root.data)

    return res

print(root.inorderTraversal (root))

print(root.PreorderTraversal (root))

print(root.PostorderTraversal(root))