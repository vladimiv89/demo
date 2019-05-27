import ctypes

def shell():

    add_diff_number = 0

    a = int(10000000000)
    b = int(10000000000)

    print(id(a), id(b))

    for i in range(1000000000):
        if not add_diff_number:
            for k in range(i, i):
                if id(i) != id(k):
                    print(i, k)
                    print(id(i), id(k))
                    add_diff_number = i
                    break
        else:
            break

    print(add_diff_number)

if __name__ == "__main__":
    shell()
