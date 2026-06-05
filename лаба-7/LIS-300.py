from typing import List
import bisect

class Solution:
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)


def test_lis():
    solution = Solution()
    
    test_cases = [
        ([10,9,2,5,3,7,101,18], 4, "Пример 1"),
        ([0,1,0,3,2,3], 4, "Пример 2"),
    ]
    
    passed = 0
    for nums, expected, desc in test_cases:
        result = solution.lengthOfLIS(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} {desc}: {nums} → {result} (ожидалось {expected})")
        if result == expected:
            passed += 1

if __name__ == "__main__":
    test_lis()