A,B,V = map(int, input().split())

# height = 0
# count = 0

# while True:
#     count += 1
#     height += A
#     if height >= V:
#         break
#     else:
#         height -= B

# print(count)

if (V-A)%(A-B)==0:
    print(((V-A)//(A-B))+1)
else:
    print(((V-A)//(A-B))+2)

