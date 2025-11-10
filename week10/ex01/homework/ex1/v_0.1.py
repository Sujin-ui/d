import os

data_path = r"c:\A20250001\data"

def read_scores (filename):
    scotes = {}
    filepath = os.path.join(data_path, filename) #폴더+ 파일

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            hakbun = parts[0]
            values = list(map(int, parts[1:]))

            scotes[hakbun] = values
        
        return scotes 
    
data = {
    "a" : read_scores("a.txt"),
    "b" : read_scores("b.txt"),
    "c" : read_scores("c.txt"),
}

# 반별 평균 계산 함수
def class_average(class_data):
    total = 0
    count = 0
    for scores in class_data.values():
        total += sum(scores)
        count += len(scores)
    return total / count if count > 0 else 0

# 반별 평균 출력
for classname, class_data in data.items():
    avg = class_average(class_data)
    print(f"{classname} 반 평균: {avg:.2f}")


