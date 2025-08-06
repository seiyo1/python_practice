food_expense = 0
with open("input/money_book.csv", encoding="utf-8") as f:
    f.readline()
    for row in f:
        row = row.rstrip()
        cols = row.split(',')
        if cols[2] == "食費":
            food_expense += int(cols[3])

print(f"食費の合計額は、{food_expense}円です")