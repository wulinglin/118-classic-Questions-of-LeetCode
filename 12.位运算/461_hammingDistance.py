"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:
输入: x = 1, y = 4
输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # print(bin(x), bin(y))
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        len_ = max(len(x_bin), len(y_bin))
        x_bin = x_bin if len(x_bin) == len_ else '0' * (len_ - len(x_bin)) + x_bin
        y_bin = y_bin if len(y_bin) == len_ else '0' * (len_ - len(y_bin)) + y_bin
        dis = 0
        for i in range(len_):
            if x_bin[i] != y_bin[i]:
                dis += 1
        return dis


if __name__ == "__main__":
    s = Solution()
    x, y = 1, 4
    print(s.hammingDistance(x, y))
