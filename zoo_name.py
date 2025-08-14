def main():
    with open("input/zoo.csv",  encoding="utf-8") as f:
        for row in f:
            row = row.rstrip()
            cols = row.split(',')
            if cols[0] == "東京" and int(cols[2]) == 0 and int(cols[3]) == 0:
                print(cols[1])

if __name__ == '__main__':
    main()
