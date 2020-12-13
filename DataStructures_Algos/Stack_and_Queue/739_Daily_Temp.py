from typing import List


class Solution:
    # Time: O(n)
    # Space: O(n)
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 1: return 0
        stack = [] # This stack would save all (index, value) pair which could not find the warmer day at the next day
        res = [0 for _ in range(len(T))]
        for index, val in enumerate(T):
            while stack and val > stack[-1][1]:
                res_index, res_val = stack.pop()
                res[res_index] = index - res_index
            stack.append((index, val))
        return res


if __name__ == '__main__':
    check_solution = Solution()
    result = check_solution.dailyTemperatures(T=[89,62,70,58,47,47,46,76,100,70])
    print(result)


