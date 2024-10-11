"""
Bài toán tìm phần tử trong cây nhị phân
Cho dãy số 3 4 1 5 2 
Dùng sơ đồ cây để sắp xếp chúng
"""
#Đầu tiên chúng ta khởi tạo lớp Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#tiếp theo tạo lớp BinarySearch
class BinarySearch:
    def __init__(self):
    	#Chưa có cây, Root = None
        self.root = None

    #Tạo 1 function Insert -->thêm giá trị
    def insert(self, data):
        if self.root is None:
        	#Chưa có cây thì sẽ làm gốc
            self.root = Node(data)
        else:
        	#Có thì nhập vào cây
            self._insert_recursively(self.root, data)

    def insert_arrange(self, node, data):
    	"""
    	Nếu giá trị của Node mới nhỏ hơn Node hiện tại --> Nhập vào bên trái
    	trong trường hợp Node bên trái đang rỗng. Ngược lại  thì so sánh tiếp.
    	Nếu giá trị của Node mới lớn hơn Node hiện tại --> Nhập vào bên phải
    	trong trường hợp Node bên phải đang rỗng. Ngược lại  thì so sánh tiếp.
       	"""
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_arrange(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_arrange(node.right, data)


    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left) # Duyệt Node bên trái
            print(node.data, end=' ') # In ra dữ liệu của Node
            self.inorder_traversal(node.right) # Duyệt Node bên phải


bst = BinarySearch()
bst.insert(3)
bst.insert(4)
bst.insert(1)
bst.insert(5)
bst.insert(3)

print("Tìm kiếm tuần tự như sau:")
bst.inorder_traversal(bst.root)
