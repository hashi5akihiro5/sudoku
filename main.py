input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 3, 0], # 1行目
    [0, 0, 0, 0, 0, 0, 0, 0, 2], # 2行目
    [0, 0, 7, 0, 9, 8, 0, 0, 0], # 3行目
    [0, 0, 0, 3, 5, 0, 0, 0, 6], # 4行目
    [0, 0, 0, 0, 0, 0, 0, 0, 0], # 5行目
    [9, 0, 8, 0, 0, 0, 4, 0, 0], # 6行目
    [3, 6, 0, 0, 1, 0, 0, 0, 0], # 7行目
    [2, 0, 0, 0, 0, 0, 0, 0, 0], # 8行目
    [0, 0, 0, 0, 0, 9, 8, 0, 0], # 9行目
]

backtracks = 0


# 数字を入れるマスを取得
def find_next_cell(grid):
    for row in range(9):
        for col in range(9):
            # 0の座標を返す
            if grid[row][col] == 0:
                return row, col
    # 全てのマスに数字が入っている状態
    return -1, -1

# 数字が数独の法則に違反していないかチェック
def is_valid(grid, row, col, value):
    # 行のチェック
    is_row = value not in grid[row]
    # 列のチェック
    is_col = value not in [grid_col[:][col] for grid_col in grid]
    # ブロックのチェック
    block_row, block_col = (row//3) * 3, (col//3) * 3
    is_block = [i[block_col:block_col + 3] for i in input_grid[block_row:block_row + 3]]
    is_block = value not in sum(is_block, [])
    return all([is_row, is_col, is_block])


# 問題解決の関数
def solve_sudoku(grid, row=0, col=0):
    global backtracks
    # 空白のセルを探す
    row, col = find_next_cell(input_grid)
    # 終了判定
    if row == -1 or col == -1:
        return True
    
    # 入力
    for value in range(1, 10):
        if is_valid(grid, row, col, value):
            grid[row][col] = value
            # 次へ
            if solve_sudoku(grid, row, col):
                return True
            backtracks += 1
            grid[row][col] = 0
    return False


if __name__ == "__main__":
    print(solve_sudoku(input_grid))
    print("試行回数：", backtracks)
    [print(i) for i in input_grid]