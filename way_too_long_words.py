t = int(input())
for i in range(t):
    w = input()
    x = len(w)
    if len(w) > 10:
        print(w[0] + str(x - 2) + w[-1])
    else:
        print(w)
