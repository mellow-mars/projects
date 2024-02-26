import random

win = 0
lose = 0
draw = 0
hands = ['가위', '바위', '보']


def rock_paper_scissor():
    while True:
        computer = random.choice(hands)
        player = input('가위, 바위, 보 중 하나를 선택 하세요: ')

        if player in (hands):
            print(f'컴퓨터 : {computer}, 플레이어 : {player}')
            if player == computer:
                print('비겼습니다')
                return 'draw'
            elif player == '가위':
                if computer == '바위':
                    print('졌습니다')
                    return 'lose'
                else:
                    print('이겼습니다')
                    return 'win'
            elif player == '바위':
                if computer == '보':
                    print('졌습니다')
                    return 'lose'
                else:
                    print('이겼습니다')
            elif player == '보':
                if computer == '가위':
                    print('졌습니다')
                    return 'lose'
                else:
                    print('이겼습니다')
                    return 'win'
            else:
                print('유효하지 않습니다')
                continue


result = rock_paper_scissor()

while True:
    if result == 'draw':
        draw += 1
    if result == 'win':
        win += 1
    if result == 'lose':
        lose += 1

    result = ''

    retry = input('다시 하시겠습니까? (y/n): ').lower()
    if retry in ('y', 'n'):
        if retry == 'n':
            print("게임을 종료합니다.")
            print(f'승 : {win}  패 : {lose}  무승부 : {draw}')
            break
        else:
            result = rock_paper_scissor()
    else:
        continue
