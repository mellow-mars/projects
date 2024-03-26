n= int(input())
words=[]
for n in range(n):
    words.append(input())

for i, word in enumerate(words):
    if word[:] == word[::-1]:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 2")
