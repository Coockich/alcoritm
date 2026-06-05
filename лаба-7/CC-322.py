from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1


def test_coin_change():
    solution = Solution()
    
    test_cases = [
        ([1, 2, 5], 11, 3, "Пример 1"),
        ([2], 3, -1, "Пример 2"),
        ([1], 0, 0, "Пример 3"),
    ]
    
    passed = 0
    for coins, amount, expected, desc in test_cases:
        result = solution.coinChange(coins, amount)
        status = "✅" if result == expected else "❌"
        print(f"{status} {desc}: coins={coins}, amount={amount} → {result} (ожидалось {expected})")
        if result == expected:
            passed += 1

if __name__ == "__main__":
    test_coin_change()