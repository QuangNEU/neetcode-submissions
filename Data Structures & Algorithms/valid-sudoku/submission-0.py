class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                box_coor = (r//3, c//3)
                if val in row[r] or val in col[c] or val in boxes[box_coor]:
                    return False
                row[r].add(val)
                col[c].add(val)
                boxes[box_coor].add(val)
        return True