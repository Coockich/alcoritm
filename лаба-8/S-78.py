from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result


def test_subsets():
    solution = Solution()
    
    test_cases = [
        ([1, 2, 3], [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]], "Пример 1"),
        ([0], [[],[0]], "Пример 2"),
    ]
    
    def normalize(subsets):
        # Сортируем каждое подмножество и общий список для сравнения
        return sorted([sorted(s) for s in subsets])
    
    passed = 0
    for nums, expected, desc in test_cases:
        result = solution.subsets(nums)
        result_norm = normalize(result)
        expected_norm = normalize(expected)
        
        status = "✅" if result_norm == expected_norm else "❌"
        print(f"{status} {desc}: nums={nums}")
        print(f"   Результат: {result}")
        print(f"   Ожидалось: {expected}")
        if result_norm == expected_norm:
            passed += 1

if __name__ == "__main__":
    test_subsets()