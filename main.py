import csv
import json
import pickle


def save_world(f):
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

    d = {}

    for x in gen_x():
        f1x = f1(x)
        f2x = f2(x)
        f3x = f3(x, f1x, f2x)
        d[x] = (f1x, f2x, f3x)

    f = open("dictionary.pkl", 'wb')
    pickle.dump(d, f)

def write_csv(filename, dictionary):

    with open(filename, 'w', newline='') as f:
        fn = ["X", "F1(x)", "F2(x)", "F3(x)"]
        writer = csv.DictWriter(f, fn)
        writer.writeheader()
        for(k, v) in dictionary.items():
            writer.writerow({fn[0]: k, fn[1]: v[0], fn[2]: v[1], fn[3]: v[2]})


def read_csv(filename):
    
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        #print(reader)

def write_json(filename, dictionary):
    
    with open(filename) as f:
        json.dump(dictionary, f)


def main():

    make_dictionary()

    f = open("dictionary.pkl", 'rb')
    d = pickle.load(f)
    f.close()

    print(d)

#    write_csv("dictionary.csv", d)
#    read_csv("dictionary.csv")
#    write_json("dictionary.json", d)


if __name__ == "__main__":
    main()
