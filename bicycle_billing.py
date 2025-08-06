from datetime import datetime

HOURLY_RATE = 400
total_fee = 0
total_time = 0

details = []
details.append("日付, 開始時刻, 終了時刻, レンタル時間")

with open("input/bicycle.csv", encoding="utf-8") as f:
    f.readline()
    for row in f:
        row = row.rstrip()
        cols = row.split(',')
        start_time = datetime.strptime(f"{cols[0]} {cols[1]}", "%Y/%m/%d %H:%M")
        end_time = datetime.strptime(f"{cols[0]} {cols[2]}", "%Y/%m/%d %H:%M")
        diff = end_time - start_time
        rental_hours = diff.total_seconds() / 3600
        total_time += rental_hours
        total_fee += rental_hours * HOURLY_RATE
        details.append(f"{start_time:%m-%d}, {start_time:%H:%M}, {end_time:%H:%M}, {rental_hours}時間")

print(f"合計レンタル時間は、{total_time}時間")
print(f"請求金額は、{int(total_fee):,}円")
print("---レンタルの詳細---")
for detail in details:
    print(detail)

with open("output/invoice.txt", "w", encoding="utf-8") as f:
    f.write("# 請求書\n")
    f.write(f"## レンタル時間\n{total_time}時間\n")
    f.write(f"## 請求金額\n{int(total_fee):,}円\n")
    f.write("## レンタルの詳細\n")
    for detail in details:
        f.write(f"{detail}\n")
