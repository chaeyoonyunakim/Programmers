def solution(s):
    p = s.lower().count('p')
    y = s.lower().count('y')

    if(p != y):
        answer = False
    else:
        answer = True

    return answer
