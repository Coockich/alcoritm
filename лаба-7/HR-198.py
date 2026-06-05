from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, current
        
        return prev1


def test_rob():
    solution = Solution()
    
    test_cases = [
        ([1, 2, 3, 1], 4, "Пример 1"),
        ([2, 7, 9, 3, 1], 12, "Пример 2"),
    ]
    
    passed = 0
    for nums, expected, desc in test_cases:
        result = solution.rob(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} {desc}: {nums} → {result} (ожидалось {expected})")
        if result == expected:
            passed += 1


if __name__ == "__main__":
    test_rob()