import random


def game_start():
    random_number = random.randint(1, 100)
    tries = 1

    while True:
        try:
            number = int(input("숫자를 입력하세요: "))
            if 0 <= number <= 100:
                if number < random_number:
                    tries += 1
                    print("업")
                if number > random_number:
                    tries += 1
                    print("다운")
                if number == random_number:
                    print("정답")
                    print(f"시도한 횟수: {tries}")
                    return tries
            else:
                print("유효한 범위 내의 숫자를 입력 해세요")
        except ValueError:
            print('숫자를 입력해주세요')
            continue


max_tries = game_start()

while True:
    retry = input('again? (y/n): ').lower()
    if retry in ('y', 'n'):
        if retry == 'y':
            print(f'이전 게임 최고 시도 횟수 {max_tries}')
            max_tries = game_start()
        else:
            break
