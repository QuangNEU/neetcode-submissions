class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Khởi tạo Hash Map lưu {giá_trị : vị_trí} của mảng inorder
        # Ví dụ: {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Con trỏ duyệt mảng preorder. Dùng list để có thể thay đổi bên trong hàm đệ quy.
        # (Ở Python 3, bạn cũng có thể dùng biến nonlocal)
        preorder_index = 0
        
        # Hàm đệ quy chỉ nhận vào ranh giới [left, right] của mảng inorder
        def array_to_tree(left, right):
            nonlocal preorder_index
            
            # Cờ dừng: Nếu ranh giới chéo nhau (trái lớn hơn phải), nghĩa là không còn Nút nào
            if left > right:
                return None
            
            # Bước 1: Rút Nút Gốc hiện tại từ preorder và tăng con trỏ lên 1 bước
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1
            
            # Bước 2: Lấy vị trí của Gốc trên mảng inorder từ Hash Map (Tốc độ O(1))
            mid = inorder_map[root_val]
            
            # Bước 3: Phái đệ quy đi xây 2 nhánh bằng cách thu hẹp ranh giới
            # CHÚ Ý: Bắt buộc phải xây nhánh Trái trước nhánh Phải!
            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)
            
            return root
            
        # Kích hoạt đệ quy với ranh giới ban đầu là toàn bộ mảng inorder
        return array_to_tree(0, len(inorder) - 1)