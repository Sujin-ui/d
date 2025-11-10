
def get_students(score_dict):
    result = []
    for name in score_dict:
        result.append(name)
    return result
    

scores = {"kim":95,"lee":65}
students = get_students(scores)

if students:
    students = ",".join(students)
    print(f"명단: {students}")
else:
    print("없음")
