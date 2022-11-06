# 점수 환산할 때, 0점이 없다는 것 체크 (리스트는 0부터니깐 헷갈리지 말기)

from collections import defaultdict
def solution(survey, choices):
    type_score = defaultdict(int)
    score = [0,3,2,1,0,1,2,3]
    for i in range(len(survey)):
        left, right = survey[i][0], survey[i][1]
        # 모르겠음을 기준으로 비동의(1,2,3)면 왼쪽 동의(5,6,7)면 오른쪽 점수 부여
        if choices[i] < 4:
            type_score[left] += score[choices[i]]
        else:
            type_score[right] += score[choices[i]]
    
    answer = ""
    for case in [("R","T"),("C","F"),("J","M"),("A","N")]:
        left, right = case
        if type_score[left] < type_score[right]:
            answer += right
        else:
            answer += left

    return answer