from datetime import date


# 誕生日から現在の年齢を計算する関数calc_age
def calc_age(year, month, day):
    today = date.today()
    birthday = date(year, month, day)
    age = today.year - birthday.year
    this_year_birthday = date(today.year, month, day)
    if today < this_year_birthday:
        age -= 1
    return age

def main():
    # 佐藤さんの年齢を求めて表示する
    sato_age = calc_age(1975, 12, 27)
    print('佐藤さんは', sato_age, '歳')

    # 鈴木さんの年齢を求めて表示する
    suzuki_age = calc_age(1995, 1, 10)
    print('鈴木さんは', suzuki_age, '歳')


if __name__ == '__main__':
    main()
