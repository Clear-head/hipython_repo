from module.prt_module import prt_alarm

def add_qty():
    """
    
        input: 사용자 입력
        return:
            x: 취소
            0 or not digit: continue
            int: 입력받은 수
    
    """
    while True:
        qty = input('\t수량을 입력하세요(취소: x): ')

        if qty in ["x", "X"]:
            return False
        
        elif qty == "0" or qty not in [str(i) for i in range(10)]:
            prt_alarm()

        else:
            return int(qty)

def add_lst(order_list, ord_num, qty, menu):
    item = menu[ord_num]

    for i in order_list:
        if i['name'] == item['name']:
            i['qty'] += qty
            return order_list 
        
    order_list.append({
        'name': item['name'],
        'qty': qty,
        'price': item['price']
    })

    return order_list

def yesno():
    while True:

        a=input('더 주문하시겠습니까?(y/n):')

        if a in ['y','n','Y','N']:
            return a.lower()
        
        else:
            prt_alarm()
            continue

def calc_cost(order_list):
    print('='*44)
    print(f'\t\t{"주문 내역"}')
    print('-'*44)

    total = 0

    for order in order_list:
        item_total = order['qty'] * order['price']
        total += item_total

        print(f'{order["name"]}\t{order["qty"]}개\t-\t{item_total:,}원')

    print('-'*44)
    print(f'총 결제 금액: {total:,}원')
    print('='*44)

    return total

def prt_points(points, total):
    
    while True:
        ab = input('포인트를 적립하시겠습니까? (y/n): ')

        if ab.lower() not in ['y', 'n']:
            prt_alarm()
            continue

        elif ab.lower()=='n':
            return
        
        else:
            while True:
                phone = input('전화번호를 입력해 주세요: ')

                if not phone.isdigit() or len(phone) < 11 or phone == "x":
                    prt_alarm()
                    continue

                user_id = f'user_{phone[-4:]}'
                point = int(total * 0.05)

                if user_id in points:
                    points[user_id] += point

                else:
                    points[user_id] = point

                print('='*44)
                print(f'🎁{user_id}고객님, {point}점 적립 되었습니다!🎁')
                print(f' 고객님의 총 적립포인트는 {points[user_id]:,}점 입니다!')
                print('='*44)
                
                return points