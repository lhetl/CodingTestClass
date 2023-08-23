def rec1(num):
    if num <= 0:
        return
    print(num, end=" ")
    rec1(num - 1)

def rec2(num):
    if num <= 0:
        return
    rec2(num - 1)
    print(num, end=" ")
    rec2(num - 1)

def rec3(num):
    if num <= 0:
        return
    rec3(num - 1)
    rec3(num - 2)
    rec3(num - 3)
    print(num, end=" ")


if __name__ == "__main__":
    rec1(3)
    print("\n")
    rec2(3)
    print("\n")
    rec3(4)
