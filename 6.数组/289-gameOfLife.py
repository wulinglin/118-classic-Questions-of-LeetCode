"""
这道题是有名的 康威生命游戏, 而我又是第一次听说这个东东，这是一种细胞自动机，每一个位置有两种状态，1为活细胞，0为死细胞，对于每个位置都满足如下的条件：
1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡
2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活
3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡
4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活
input_cell = [
[0,1,0],
[0,0,1],
[1,1,1],
[0,0,0]
]

"""
import copy


class Solution(object):
    def gameOfLife(self, board):
        eight_anchor_index = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        a, b = len(board), len(board[0])
        output_cell = copy.deepcopy(board)  # 不能用output_cell = input_cell[:]，元素会被改掉
        # copy.copy()是浅拷贝，但是python内置a.copy()是深拷贝
        for i in range(a):
            for j in range(b):
                live_cell_count = 0
                for m, n in eight_anchor_index:
                    if i + m < 0 or j + n < 0 or i + m >= a or j + n >= b:
                        continue

                    if board[i + m][j + n] == 1:
                        live_cell_count += 1

                if board[i][j] == 0 and live_cell_count == 3:
                    output_cell[i][j] = 1
                elif board[i][j] == 1 and live_cell_count < 2:
                    output_cell[i][j] = 0
                elif board[i][j] == 1 and 2 <= live_cell_count <= 3:
                    output_cell[i][j] = 1
                elif board[i][j] == 1 and live_cell_count > 3:
                    output_cell[i][j] = 0

        return output_cell


board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
# [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
s = Solution()
res = s.gameOfLife(board)
print(res)

# def get_next_state(input):
#     kernel = [1, 1, 1, 1, 0, 1, 1, 1, 1]
#
#     padding = np.array([[0 for i in range(len(input[0])+2)] for j in range(len(input)+2)])
#
#     padding[1:-1, 1:-1] = input
#
#     input_col = [a for col in padding for a in col]
#
#     out_size_x = len(input)
#     out_size_y = len(input[0])
#     convertW = len(kernel)
#     kernel_size = 3
#
#
#     temp_matrix = [0 for i in range(out_size_x * out_size_y * convertW)]
#
#     feature_size_x = padding.shape[1]
#     feature_size_y = padding.shape[0]
#
#     for i in range(0, out_size_x):
#         for j in range(0, out_size_y):
#             for k in range(convertW):
#                 row = int(k / kernel_size)
#                 col = int(k % kernel_size)
#                 start = int(i * feature_size_x + j)
#                 value = input_col[int(start + row*feature_size_x + col)]
#                 index = int((i * out_size_y + j) * convertW + k)
#                 temp_matrix[index] = value
#
#     result = input.copy()
#     for i in range(len(input)):
#         for j in range(len(input[i])):
#             temp = 0
#             for k in range(len(kernel)):
#                 temp += temp_matrix[(i*out_size_y + j)*convertW + k] * kernel[k]
#             if temp < 2:
#                 result[i][j] = 0
#             elif (temp == 2 or temp == 3) and input[i][j] == 1:
#                 result[i][j] = 1
#             elif temp > 3:
#                 result[i][j] = 0
#             elif temp == 3 and input[i][j] == 0:
#                 result[i][j] = 1
#     return result
