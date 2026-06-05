from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_gas += diff
            current_tank += diff
            
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
        
        return start_index if total_gas >= 0 else -1


def test_gas_station():
    solution = Solution()
    
    test_cases = [
        ([1,2,3,4,5], [3,4,5,1,2], 3, "Пример 1"),
        ([2,3,4], [3,4,3], -1, "Пример 2"),
    ]
    
    passed = 0
    for gas, cost, expected, desc in test_cases:
        result = solution.canCompleteCircuit(gas, cost)
        status = "✅" if result == expected else "❌"
        print(f"{status} {desc}: gas={gas}, cost={cost} → {result} (ожидалось {expected})")
        if result == expected:
            passed += 1

if __name__ == "__main__":
    test_gas_station()