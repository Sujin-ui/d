def avg_score(score_dict):
    if len(score_dict)==0:
        return None
    else:
        return sum(score_dict.values())/len(score_dict)
scores = {"kim":95,"lee":65}
avg = avg_score(scores)

if avg != None:
    print(f"평균 {avg}")
else:
    print("점수없음")