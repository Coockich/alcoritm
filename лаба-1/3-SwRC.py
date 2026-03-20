def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    
    return max_length

print(length_of_longest_substring('abcabcbb'))
print(length_of_longest_substring('bbbbb'))
print(length_of_longest_substring('pwwkew'))