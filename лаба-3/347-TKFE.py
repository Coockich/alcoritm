def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    unique_nums = list(freq.keys())
    unique_nums.sort(key=lambda x: freq[x], reverse=True)
    
    return unique_nums[:k]

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
print(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))