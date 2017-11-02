
def foo():
    for i in range(47+2, 0, -1):
        if 33 % i == 3 and 47 % i == 2:
            print(i)
            return i

if __name__ == '__main__':
    foo()
