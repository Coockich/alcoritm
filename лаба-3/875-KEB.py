def minEatingSpeed(piles: list[int], h: int) -> int:
    def can_eat_all(k: int) -> bool:
        total_hours = 0
        for pile in piles:
            total_hours += (pile + k - 1) // k
        return total_hours <= h

    left = 1
    right = max(piles)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_eat_all(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

print(minEatingSpeed([3,6,7,11], 8))
print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))
