li = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]
d = {}
s = set()


def main():

    print(li)

    li.sort(key=lambda x: x[1])
    print(li)

    for i in li:
        d[i[1]] = [i[0], i[2], i[3]]
    print(d)

    for k in d:
        d[k].sort(reverse=True)
    print(d)

    for k in d:
        for v in d[k]:
            s.add(v)
    print(s)

    string = str(s)
    print(string)


if __name__ == "__main__":
    main()
