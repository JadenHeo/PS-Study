def solution(board, nums):
    answer = 0
    size = len(board)
    nums = set(nums)
    bingos = {'row' : [size for _ in range(size)], 'col' : [size for _ in range(size)], 'diagonal' : [size, size]}
    for row in range(size):
        for col in range(size):
            if board[row][col] in nums:
                bingos['row'][row] -= 1
                bingos['col'][col] -= 1
                if row == col:
                    bingos['diagonal'][0] -= 1
                if row + col + 1 == size:
                    bingos['diagonal'][1] -= 1
    for sub_bingos in bingos.values():
        answer += sub_bingos.count(0)
    return answer