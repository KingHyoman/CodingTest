## Just Test
# strategy


def compare(a, b):
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")
a, b = input().split()
compare(int(a), int(b))
