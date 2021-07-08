flag = True
a = []
b = 0
sale = 0
while flag:
    buy = input('상품을 구매 하시겠습니가? 1.구매, 2.종료')
    if buy == '1':
        price = int(input('구매한 상품의 금액은? '))
        a.append(price)
        b += price
    else:
        if len(a) == 1:
            sale = 5
        elif len(a) == 2:
            sale = 10
        elif len(a) == 3:
            sale = 20
        elif len(a) >= 4:
            sale = 30
        print(f'할인율 : {sale} %')
        print(b*((100 - sale)/100))
        flag = False