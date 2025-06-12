import module.main_functions
import module.error_class
from module.prt_module import prt_time, prt_menu


def main():
    qty = False
    ord_num = False

    points = {}
    # # 메뉴 저장 리스트 -> 메뉴 추가 시 여기서.
    menu = [
        {'name':'샤프', 'price': 6000},
        {'name':'볼펜', 'price': 3000},
        {'name':'지우개', 'price': 1000},
        {'name':'화이트', 'price': 3000},
        {'name':'공책', 'price': 3500}
    ]
    
    while True:
        prt_menu(menu)
        # 다중 주문 저장 리스트
        order_list = []
    
        while True: 
            ord_num = module.main_functions.add_qty()
            if ord_num == False:
                break
            
            menut = menu[ord_num]['name']
            
            print('='*44)
            print(f'{"고객님이 선택하신 제품은":^33}')
            print(f'{menut + " 입니다.":^33}')
            print(f'{"몇 개를 드릴까요?":^33}')
            
            
            qty = module.main_functions.add_qty()
            if qty == False:
                break
                 
            module.main_functions.add_lst(order_list, ord_num, qty, menu)
            
            if module.main_functions.yesno() == 'n':
                break

            print('-'*44)

        if qty != False and ord_num != False:
            total = module.main_functions.calc_cost(order_list)
            
            module.main_functions.prt_points(points, total)
            
            print(f'{"결제가 완료되었습니다.":^37}')
            print(f'{"잠시만 기다려주세요. 😊":^37}')
        
            prt_time()

if __name__ == "__main__":
    main()