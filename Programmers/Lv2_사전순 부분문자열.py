def solution(s):
    answer = []
    for alphabet in s[::-1]:
        if not answer or answer[-1] <= alphabet:
            answer.append(alphabet)
    return ''.join(reversed(answer))