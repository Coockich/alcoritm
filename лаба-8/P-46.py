from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False] * n
        current = []
        
        def backtrack():
            if len(current) == n:
                result.append(current[:])
                return
            
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    backtrack()
                    current.pop()
                    used[i] = False
        
        backtrack()
        return result


def test_permute():
    solution = Solution()
    
    test_cases = [
        ([1, 2, 3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], "Пример 1"),
        ([0, 1], [[0,1],[1,0]], "Пример 2"),
        ([1], [[1]], "Пример 3"),
    ]
    
    def normalize(perms):
        # Сортируем каждую перестановку и общий список для сравнения
        return sorted([tuple(p) for p in perms])
    
    passed = 0
    for nums, expected, desc in test_cases:
        result = solution.permute(nums)
        result_norm = normalize(result)
        expected_norm = normalize(expected)
        
        status = "✅" if result_norm == expected_norm else "❌"
        print(f"{status} {desc}: nums={nums}")
        print(f"   Результат: {result}")
        print(f"   Ожидалось: {expected}")
        if result_norm == expected_norm:
            passed += 1

if __name__ == "__main__":
    test_permute()