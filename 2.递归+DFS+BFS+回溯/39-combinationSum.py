"""组合总数：
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
"""
from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates = []
        res = []
        path = []
        # candidates.sort() # todo 先排序，目的是结果比较稳定
        self.dfs(candidates, target, path, res, 0, size=len(candidates))
        return res

    def dfs(self, candidates, target, path, res, begin, size):
        # path = []
        # while target>0:
        if target == 0:
            res.append(path[:])  # TODO 一定是[:]或者。copy
            return
        for index in range(0, size):  # todo 如果变成range(0, size) 就是最全结果：[[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]

            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break

            # # todo 注意前/后三行的区别！ 不能是target-=candidates[index]
            # if target - candidates[index] < 0:
            #     break
            # target -= candidates[index]
            path.append(candidates[index])
            print(index, begin, target, path[:], res)

            # todo 这里怎么使得path在纵向传递而不是横向传递？
            self.dfs(candidates, residue, path, res, index, size)
            path.pop()


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝是为了提速，在本题非必需
        candidates.sort()  # TODO 这里不加sort结果就变成[[7]] ??
        # 在遍历的过程中记录路径，它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])
            print(target, path, res)

            return

        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []

        def dfs(candidates, target, tmp):
            if target == 0:
                res.append(tmp[:])
                return

            for each in candidates:
                if target - each < 0:
                    continue
                remaind = target - each
                tmp.append(each)
                dfs(candidates, remaind, tmp)
                tmp.pop()

        dfs(candidates, target, tmp)
        return res


if __name__ == '__main__':
    candidates = [2, 6, 3, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)
