fitness_count = {}

with open("input/fitness.csv", encoding="utf-8") as f:
    f.readline()
    for row in f:
        row = row.rstrip()
        cols = row.split(',')
        ex = cols[1]
        cnt = fitness_count.get(ex, 0)
        fitness_count[ex] = cnt + 1

for ex, cnt in fitness_count.items():
    print(f"{ex}は、{cnt}回")