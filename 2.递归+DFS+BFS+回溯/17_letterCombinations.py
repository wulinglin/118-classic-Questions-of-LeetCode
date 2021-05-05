"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![](./img/17.png)

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

题解：
明明是递归，哪里有回溯？
"""


def f(n):
    if n <= 2:
        return 2
    else:
        return f(n - 1) * n


class Solution:
    """
    完全自己写出来的哦。
    """

    def letterCombinations(self, str_):
        map_dict = {
            '0': [],
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        s_list = [map_dict[i] for i in str_]

        def combination_between_two(l1, l2):
            combin_list = []
            for i in l1:
                for j in l2:
                    combin_list.append(i + j)
            return combin_list

        def dfs(s_list):
            if len(s_list) == 0:
                return []
            elif len(s_list) <= 1:
                return s_list[0]
            elif len(s_list) == 2:
                return combination_between_two(s_list[0], s_list[1])
            else:
                return dfs([combination_between_two(s_list[0], s_list[1])] + s_list[2:])

        return dfs(s_list)


class Solution:
    def letterCombinations(self, digits):
        """

        官方题解！
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits

                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


s = Solution()
str_ = '234'
res = s.letterCombinations(str_)
print(res)
print(len(res))
print(len(set(res)))
