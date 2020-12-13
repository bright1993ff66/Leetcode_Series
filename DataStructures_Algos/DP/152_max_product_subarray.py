from typing import List
from functools import reduce


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        currentMax, currentMin, result = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_val = nums[i]
            temp = currentMax
            currentMax = max(cur_val, cur_val*currentMax, cur_val*currentMin)
            currentMin = min(cur_val, cur_val*temp, cur_val*currentMin)
            result = max(currentMax, result)
        return result

    def maxProduct_2(self, nums: List[int]) -> int:
        if min(nums) > 0: return reduce(lambda x, y: x * y, nums)
        size = len(nums)
        dp = [[1, 1]] * size
        dp[0] = [nums[0], nums[0]]  # dp[0][0] indicate max and dp[0][1] indicate min
        for i in range(1, size):
            if nums[i] == 0:
                dp[i] = [0, 0]
            elif nums[i] > 0:
                curmax = max(nums[i], nums[i]*dp[i-1][0])
                curmin = min(nums[i], nums[i]*dp[i-1][1])
                dp[i] = [curmax, curmin]
            else:
                curmax = max(nums[i], nums[i] * dp[i - 1][1])
                curmin = min(nums[i], nums[i] * dp[i - 1][0])
                dp[i] = [curmax, curmin]
        return max([x[0] for x in dp])


if __name__ == '__main__':
    check_solution = Solution()
    print(check_solution.maxProduct_2(nums=[-4, -3, -2]))
