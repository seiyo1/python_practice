def main():
    total = 0
    with open("input/sales.csv", encoding="utf-8") as f:
        for row in f:
            cols = row.rstrip().split(',')
            month = int(cols[0])
            sale = int(cols[1]) * 1000
            if month <= 6:
                total += sale
    avg = total / 6
    print(f'1月から6月までの月売上の平均は{avg:,.2f}円です。')


if __name__ == '__main__':
    main()
