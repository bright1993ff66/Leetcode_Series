class Solution:
    def myPow_1(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1/self.myPow_1(x, -n)
        if n & 1:
            return self.myPow_1(x, n - 1) * x
        return self.myPow_1(x * x, n // 2)

    def myPow_2(self, x: float, n: int) -> float:
        if n==0: return 1
        if n<0:
            x = 1/x
            n = -n
        power = 1
        while n:
            if n & 1:
                power *= x
            x *= x
            n >>= 1
        return power


if __name__ == '__main__':
    check_solution = Solution()
    result = check_solution.myPow_2(x=2, n=10)
    print(result)