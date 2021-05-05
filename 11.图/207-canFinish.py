"""
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

 
示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5

拓扑排序 入度 邻接矩阵 ：https://blog.csdn.net/HYbuery/article/details/82787646
步骤：
一、定义

1.入度就是有向图中指向这个点的边的数量。
2.出度就是从这个点出去的边的数量。
3.邻接矩阵{出发点：【到达点】}
二、
1.在有向图中找出（没有前驱）入度为零的点，并且输出。
2.从图中删除以它为弧尾的边（删除从它出发的边）
3.重复1、2两步直至所有顶点全部输出，或者图中不存在入度为零的顶点（剩下的就是环），说明有向图有环。
"""
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        print(numCourses, indegrees)
        """209
        有零入度点，是一张图是dag的必要条件。因为dag是有向树加向外的边。
        这意味着：有0入度点的图不一定是dag，没有0入度的图一定不是dag，一张图不是dag必有环
        """
        while queue:
            print(11)
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses


numCourses, prerequisites = 2, [[1, 0], [0, 1]]
s = Solution()
res = s.canFinish(numCourses, prerequisites)
print(res)
