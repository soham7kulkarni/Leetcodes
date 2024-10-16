# TC - O(MN)
# SC - O(MN)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        n = amount
        # Initial column is dummy ('0') hence n+1
        #                                    We have dummy row at the start hence m+1
        dp = [[0 for c in range(n+1)] for r in range(m+1)]
        # Above line creates matrix (m*n) of all 0's 

        # We fill initial dummy row with max number except 1st cell
        # 1st cell is 0
        for j in range(1, n+1):
            dp[0][j] = 999999
        for i in range(1, m+1):
            for j in range(1, n+1):
                # In case of 5, we copy first 5 elements from above row
                # In case of 1, we just copy 1 element from above row
                if j < coins[i-1]:
                    # Since our i is 1, we take i-1 to fetch correct coin
                    dp[i][j] = dp[i-1][j]
                else:
                    # We want minimum between above row and current
                    # in current we add 1 (since we are considering the coin)
                    # We go backwards in the same row, 'coin' times and then add 1
                    # If we have 5, we go 5 places backward and then add 1
                    # If we have 1, we go 1 place backward and then add 1
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])

        # If last cell value is greater than amount, it is invalid answer
        # In worst case, using all 1s coins, we need at least 11 coins to get 11 as a sum
        if dp[m][n] > amount:
            return -1
        return dp[m][n]