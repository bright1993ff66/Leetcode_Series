from typing import List
from sys import maxsize


class Solution:
    # No.121
    # Buy once and sell once
    def maxProfit_121(self, prices: List[int]) -> int:
        min_price, max_profit = maxsize, 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

    # No.122
    def maxProfit_122(self, prices: List[int]) -> int:
        """
        Say you have an array prices for which the ith element is the price of a given stock on day i.
        Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e.,
        buy one and sell one share of the stock multiple times).
        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you
        buy again).
        :param prices: the price of a given stock
        :return:
        """
        buy, sell, total_profit = 0, 0, 0
        for index in range(0, len(prices) - 1):
            if prices[index + 1] > prices[index]:
                buy, sell = prices[index], prices[index + 1]
                total_profit += sell - buy
        return total_profit

    # No.123
    def maxProfit_123(self, prices: List[int]) -> int:
        """
        Say you have an array for which the ith element is the price of a given stock on day i.
        Design an algorithm to find the maximum profit. You may complete at most two transactions.
        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before
        you buy again).
        :param prices: the price of a given stock
        :return:
        """
        n = len(prices)
        MP = [[[0, 0] for _ in range(2 + 1)] for _ in range(n)]
        # Initialize the data for the first day
        MP[0] = [[0, 0]] + [[0, -prices[0]]] * 2
        for i in range(1, n):
            for kk in range(1, 2 + 1):
                MP[i][kk][1] = max(MP[i - 1][kk][1], MP[i - 1][kk - 1][0] - prices[i])
                MP[i][kk][0] = max(MP[i - 1][kk][0], MP[i - 1][kk][1] + prices[i])
        return max(map(lambda x: x[0], MP[n - 1]))

    # No.188
    def maxProfit_188(self, k: int, prices: List[int]) -> int:
        """
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
        Design an algorithm to find the maximum profit. You may complete at most k transactions.
        Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before
        you buy again).
        """
        if not prices: return 0
        MP = [[[0, 0] for _ in range(k + 1)] for _ in range(len(prices))]
        # Initialize the data for the first day
        MP[0] = [[0, 0]] + [[0, -prices[0]]] * k
        for i in range(1, len(prices)):
            for kk in range(1, k + 1):
                # Buy one stock means one transaction. Because in the end, we would sell all stocks
                MP[i][kk][1] = max(MP[i - 1][kk][1], MP[i - 1][kk - 1][0] - prices[i])
                MP[i][kk][0] = max(MP[i - 1][kk][0], MP[i - 1][kk][1] + prices[i])
        return max(map(lambda x: x[0], MP[-1]))


if __name__ == '__main__':
    solution = Solution()
    profits = solution.maxProfit_188(k=2, prices= [2,4,1])
    print(profits)
