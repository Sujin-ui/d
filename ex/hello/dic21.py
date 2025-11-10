def add_dict(scores_dict, name, score):
    if name in scores_dict:
        return False
    scores_dict[name] = score
    return True


scores = {"kim":95,"lee":65}
if add_dict(scores,"peark",100):
    print("입력완료")
else:
    print("동일학생있음")
if add_dict(scores,"Kim",100):
    print("입력완료")
else:
    print("동일학생있음")