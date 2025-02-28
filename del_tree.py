# สมาชิกกลุ่ม
# 1) ธนกร พิชัย
# 2) ตรีวิทย์ สุทธมุสิก 
# 3) สถาปนา ฮวดวิเศษ
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end=" ")
        if self.right:
            self.right.PrintTree()

    def find_min(self):
        # หาค่าที่น้อยที่สุดทางซ้ายของโหนด 
        current = self
        while current.left:
            current = current.left
        return current

    def delete(self, data):
        # ฟังก์ชันลบโหนดใน BST 
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            # กรณี 1: ไม่มีลูก
            if not self.left and not self.right:
                return None
            # กรณี 2: มีลูกข้างเดียว
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            # กรณี 3: มีลูกสองข้าง
            min_larger_node = self.right.find_min()  # หา Inorder Successor
            self.data = min_larger_node.data
            self.right = self.right.delete(min_larger_node.data)  # ลบค่าที่ซ้ำกัน
        return self


# ตัวอย่างการใช้งาน
root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)

print("Tree ก่อนลบ:")
root.PrintTree()

root = root.delete(30)  # ลบโหนดที่มีค่า 30

print("\nTree หลังลบ 30:")
root.PrintTree()
