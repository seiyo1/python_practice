breads = {
    'アンパン': 218,
    '食パン': 152,
    'カレーパン': 333,
    'メロンパン': 250,
    'ロールパン': 245,
    'クリームパン': 220,
}


def main():
    """メインの処理."""
    sum = 0
    for price in breads.values():
        sum += price
    mean = sum / len(breads)
    print(f'平均価格は{mean:.1f}円です。')


if __name__ == '__main__':
    main()

