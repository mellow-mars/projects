mirror_letters = {
    'b':'d',
    'd':'b',
    'p':'q',
    'q':'p'
}

T = int(input())

for i in range(T):
    new_word =''
    word = input()
    word = str(word)
    for j in word:
        new_word+=mirror_letters[j]

    print(f"#{i+1} {new_word[::-1]}") 