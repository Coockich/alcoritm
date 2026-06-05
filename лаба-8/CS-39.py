from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(start, current, current_sum):
            if current_sum == target:
                result.append(current[:])
                return
            
            for i in range(start, len(candidates)):
                if current_sum + candidates[i] > target:
                    break
                current.append(candidates[i])
                backtrack(i, current, current_sum + candidates[i])
                current.pop()
        
        backtrack(0, [], 0)
        return result


def test_combination_sum():
    solution = Solution()
    
    test_cases = [
        ([2,3,6,7], 7, [[2,2,3],[7]], "Пример 1"),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]], "Пример 2"),
        ([2], 1, [], "Пример 3"),
    ]
    
    def normalize(combs):
        # Сортируем каждую комбинацию и общий список для сравнения
        return sorted([sorted(c) for c in combs])
    
    passed = 0
    for candidates, target, expected, desc in test_cases:
        result = solution.combinationSum(candidates, target)
        result_norm = normalize(result)
        expected_norm = normalize(expected)
        
        status = "✅" if result_norm == expected_norm else "❌"
        print(f"{status} {desc}: candidates={candidates}, target={target}")
        print(f"   Результат: {result}")
        print(f"   Ожидалось: {expected}")
        if result_norm == expected_norm:
            passed += 1

if __name__ == "__main__":
    test_combination_sum()