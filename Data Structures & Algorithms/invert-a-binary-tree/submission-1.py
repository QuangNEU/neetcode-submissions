class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Điểm dừng: Nếu đã đi quá lá, chạm vào khoảng không
        if not root:
            return None
            
        # Hành động: Đổi chỗ cành trái và cành phải
        root.left, root.right = root.right, root.left
        
        # Đệ quy: Ra lệnh cho 2 cành con tự đi làm việc y hệt
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root