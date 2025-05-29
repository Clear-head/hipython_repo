snack_box = ['초코파이']
new_snack = input('먹고 싶은 간식을 추가하세요.  단, 쉼표(,)로 연결하세요\n').lstrip(" ").split(',')
snack_box += new_snack

print(snack_box)

qty = int(input('간식박스 몇 세트로 포장할까요? 예: 2 -> 2box\n'))

snack_box *= qty
print(snack_box)

print(f'주문하신 간식상자는 {snack_box[0]},{snack_box[1]},{snack_box[2]} 등입니다. 확인해주세요.')

msg = '혹시 빼고싶은 간식이 있으면 입력하세요\n'
snack = input(msg).lstrip(" ")

while snack in snack_box:
    snack_box.remove(snack)

print("있어요" if snack in snack_box else "없어요")

print("주문하신 간식 박스는 다음과 같습니다\n")
print(*snack_box)