grades = { 'A+':4.5,
        'A0': 4.0,
        'B+':3.5,
        'B0':3.0,
        'C+':2.5,
        'C0':2.0,
        'D+':1.5,
        'D0':1.0,
        'F':0.0
}

scores = []
hakjum=0.0
jumsu=0.0


for _ in range(20):
    scores.append(list(map(str, input().split())))

for i in range(len(scores)):
    if scores[i][2] != 'P':
        hakjum += float(scores[i][1])
        jumsu += grades[scores[i][2]]*float(scores[i][1])


print(jumsu/hakjum)