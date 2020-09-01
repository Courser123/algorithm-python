# https://leetcode-cn.com/problems/climbing-stairs/
import math


class Solution:

    def climbStairs(self, n: int) -> int:

        # return self.climbStairsA(n)
        return self.climbStairsB(n)

    # 斐波那契数列通项公式

    def climbStairsA(self, n: int) -> int:

        math_sqrt5 = math.sqrt(5)

        return int((pow((1 + math_sqrt5) / 2, n + 1) - pow(
            (1 - math_sqrt5) / 2, n + 1)) / math_sqrt5)

    # f(n) = f(n-1) + f(n-2)
    """
    思考方式: 要到达第n个台阶, 最后一步只有两种方式:
    1. 跨了一个台阶到达
    2. 跨了两个台阶到达
    而且跨一个台阶到达和跨两个台阶到达必然是不同的走法(因为最后一步阶数不同)
    所以, 到达第n阶的方法数等于到达n-1阶的方法数加上到达n-2阶的方法数
    """

    def climbStairsB(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairsB(n - 1) + self.climbStairsB(n - 2)


test = Solution()

print(test.climbStairs(3))
