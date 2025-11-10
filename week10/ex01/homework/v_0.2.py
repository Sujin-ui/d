import os
from datetime import datetime

path = r"c:\A20250001\data"   # 실제 경로 확인 필요
files = ["a.txt", "b.txt", "c.txt"]

data = []
for fname in files:
    with open(os.path.join(path, fname), encoding="utf-8") as f:  # 오타 수정
        for line in f:
            parts = line.strip().split(",")
            data.append(parts)

students = {'20201001': '홍길동', '20201002': '임꺽정'}

with open("score.txt", "w", encoding="utf-8") as out:
    for row in data:
        sid = row[0]
        try:
            scores = list(map(int, row[1:]))
        except ValueError:
            print(f"⚠️ 잘못된 데이터: {row}")
            continue
        total = sum(scores)
        avg = total / len(scores)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = students.get(sid, "Unknown")
        line = f"{name},{sid},{','.join(map(str, scores))},{total},{avg:.1f},{timestamp}\n"
        out.write(line)