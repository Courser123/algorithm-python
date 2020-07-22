# https://leetcode-cn.com/problems/climbing-stairs/
import math


class Solution:

    def climbStairs(self, n: int) -> int:

        return self.climbStairsA(n)

    # 斐波那契数列通项公式

    def climbStairsA(self, n: int) -> int:

        math_sqrt5 = math.sqrt(5)

        return int((pow((1 + math_sqrt5) / 2, n + 1) - pow(
            (1 - math_sqrt5) / 2, n + 1)) / math_sqrt5)


test = Solution()

print(test.climbStairs(3))
