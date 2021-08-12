def solution(arr):
    START, END = 0, 1
    arr = sorted(arr, key=lambda conference : (conference[END], conference[START]))
    answer = 1
    now_time = arr[0][END]
    for start, end in arr[1:]:
        if start >= now_time:
            now_time = end
            answer += 1
    return answer