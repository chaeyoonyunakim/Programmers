def solution(n):
    check = n ** (1 / 2)
    if check % 1 == 0:
        answer = (check + 1) ** 2
    else:
        answer = -1

    return answer
