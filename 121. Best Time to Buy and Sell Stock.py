class Solution(object):
    def maxProfit(self, prices):
        buy_pointer = 0
        sell_pointer = 1
        profit = 0
        while sell_pointer < len(prices):
            if prices[buy_pointer] < prices[sell_pointer]:
                if (prices[sell_pointer] - prices[buy_pointer] > profit):
                    profit = prices[sell_pointer] - prices[buy_pointer]
            else:
                buy_pointer = sell_pointer
            sell_pointer += 1

        return profit

# Used two pointers technique to solve this particular problem
# The first pointer: buy_pointer started from index 0 and sell pointer started from 1 after that just checked the
# buying and selling price difference 