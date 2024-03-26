n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))


def sort_key_func(item): return item[1]


print(xy)
