def minEatingSpeed(piles: list[int], h: int) -> int:
    """
    Возвращает минимальную скорость поедания бананов (бананов в час)
    
    Args:
        piles: массив с количеством бананов в каждой куче
        h: количество часов до возвращения охранников
    
    Returns:
        int: минимальная скорость K
    """
    def can_eat_all(k: int) -> bool:
        """
        Проверяет, сможет ли Коко съесть все бананы за h часов
        со скоростью k бананов в час
        """
        total_hours = 0
        for pile in piles:
            # Время на одну кучу = ceil(pile / k)
            total_hours += (pile + k - 1) // k
        return total_hours <= h
    
    # Скорость может быть от 1 до max(piles)
    left = 1
    right = max(piles)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_eat_all(mid):
            # Если успевает, пробуем меньшую скорость
            right = mid
        else:
            # Если не успевает, увеличиваем скорость
            left = mid + 1
    
    return left


# Примеры
print(minEatingSpeed([3,6,7,11], 8))       # 4
print(minEatingSpeed([30,11,23,4,20], 5))  # 30
print(minEatingSpeed([30,11,23,4,20], 6))  # 23