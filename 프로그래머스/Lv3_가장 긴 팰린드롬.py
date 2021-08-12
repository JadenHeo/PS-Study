def is_palindrome(s):
    return s == s[::-1]

def solution(s):
    max_length = 1
    for length in range(len(s), 1, -1):
        for start in range(len(s)+1-length):
            substring = s[start:start+length]
            if is_palindrome(substring):
                return len(substring)
    return max_length

def solution_fast(s):
    if len(s) == 1:
        return 1
    start, max_length = 0, 0
    for end in range(len(s)):
        if is_palindrome(s[end-max_length:end+1]):
            start, max_length = end - max_length, max_length + 1
        elif end - max_length > 0 and is_palindrome(s[end-max_length-1:end+1]):
            start, max_length = end - max_length -1, max_length + 2
    return max_length