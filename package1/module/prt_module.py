import time

def prt_menu(menu):
    print('╔' + '═' * 40 + '╗')
    print(f'빵꾸똥꾸 문구야'.center(34))
    print(f"에 오신 것을 환영합니다!💥".center(34))
    print('╚' + '═' * 40 + '╝') 
    print(f'{"번호"}\t\t{"제품명"}\t\t{"가격"}')
    print('-'*44)

    for i, m in enumerate(menu):
        print(f'{i+1}\t\t{m["name"]}\t\t{m["price"]:,}원')
    
    print('-'*44)

def prt_alarm():
    print('='*44)
    print(f'{"[알림]❌ 잘못된 입력입니다.":^35}')
    print(f'{"[알림]✅ 다시 입력해주세요.":^35}')
    print('='*44)


def prt_time():
    for i in range(3, 0, -1):
        print('=' * 44)
        print(f'{i}초 뒤에 시작화면으로 돌아갑니다.'.center(34))
        time.sleep(1)