class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # Ghép độ dài + dấu '#' + nội dung chuỗi
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # 1. Tìm vị trí của dấu '#' gần nhất
            j = i
            while s[j] != '#':
                j += 1
                
            # 2. Cắt phần số ra để biết độ dài chuỗi
            length = int(s[i:j])
            
            # 3. Bắt đầu đọc chuỗi từ sau dấu '#' (j + 1)
            # Đọc đúng một lượng ký tự bằng 'length'
            string_content = s[j + 1 : j + 1 + length]
            res.append(string_content)
            
            # 4. Cập nhật con trỏ i nhảy tới khối tiếp theo
            i = j + 1 + length
            
        return res