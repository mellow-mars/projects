# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

length = 0

for test_case in range(1, T + 1):
    word = input()
    for i in range(1,len(word)): 
        if word[:i]==word[i:i+i]: 
            length = i
            break   
    print(f"#{test_case} {length}")

