import csv
import json
import pickle


def save_world(f):
    """ decorator for extremly dengerous functions f2() & f3(),
        they can try divide by zero """
    def inner(*args):
        if args[0] == 0:
            print("NO GOD! PLEASE NO!!! NOOOOOOOOOO!!!")
            return
        if len(args) == 3:
            return f(args[0], args[1], args[2])
        else:
            return f(args[0])
    return inner


def f1(x):
    return x / (x + 100)


@save_world
def f2(x):
    return 1 / x


@save_world
def f3(x, f1x, f2x):
    return 20 * (f1x + f2x) / x


def gen_x():
    for x in range(5, 91):
        yield x
    yield 0


def make_dictionary():
    """ wery important calculations """

    d = {}

    for x in gen_x():
        f1x = f1(x)
        f2x = f2(x)
        f3x = f3(x, f1x, f2x)
        d[x] = (f1x, f2x, f3x)

    return d


def serialize(filename, obj):
    f = open(filename, 'wb')
    pickle.dump(obj, f)
    f.close()


def deserialize(filename):
    f = open(filename, 'rb')
    obj = pickle.load(f)
    f.close()
    return obj


def write_csv(filename, dictionary):
    """ write dictionary to csv file """
    with open(filename, 'w', newline='') as f:
        fn = ["X", "F1(x)", "F2(x)", "F3(x)"]
        writer = csv.DictWriter(f, fn)
        writer.writeheader()
        for(k, v) in dictionary.items():
            writer.writerow({fn[0]: k, fn[1]: v[0], fn[2]: v[1], fn[3]: v[2]})


def read_csv(filename):
    """ read dictionary from csv file """ 
    li = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            li.append(row)
    return li


def write_json(filename, obj):
    """ write dictionary to json file """    
    with open(filename, 'w') as f:
        json.dump(obj, f)


def read_json(filename):
    with open(filename) as f:
        obj = json.load(f)
    return obj


def main():

    d = make_dictionary()

    serialize("dictionary.pkl", d)
    d_pkl = deserialize("dictionary.pkl")

    write_csv("dictionary.csv", d_pkl)
    li_csv = read_csv("dictionary.csv")

    write_json("list.json", li_csv)


if __name__ == "__main__":
    main()
