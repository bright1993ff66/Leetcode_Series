class Solution:
    def minimumTotal(self, triangle):
        if not triangle: return
        res = triangle[-1][:] # set res' length as the longest one in the triangle
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        print(res)
        return res[0]


if __name__ == '__main__':
    check_solution = Solution()
    result = check_solution.minimumTotal(triangle=[[2],[3,4],[6,5,7],[4,1,8,3]])
    print(result)