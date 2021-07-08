# 구매상품 할인율 계산
# 1개 - 5%
# 2개 - 10%
# 3개 - 20%
# 4개이상 - 30%

# def checkDiscount(goods):
#
#     flag = True
#     goods = []
#     sum = 0
#     sale = 0
#
#     if len(goods) == 1:
#         sale = 5
#     elif len(goods) == 2:
#         sale = 10
#     elif len(goods) == 3:
#         sale = 20
#     elif len(goods) >= 4:
#         sale = 30
#     fare = sum * ((100 - sale) / 100)
#     print(f'할인율 : {sale} %')
#     print(f'총구매금액 : {sum}')
#     print(f'할인 적용 구매금액 : {fare}')
#     flag = False
#
#
#
# def discountGoods(goods):
#     flag = True
#     goods = []
#     sum = 0
#     sale = 0
#     while flag:
#         buy = input('상품을 구매 하시겠습니가?\n 1.구매, 2.종료')
#         if buy == '1':
#             price = int(input('구매한 상품의 금액은? '))
#             goods.append(price)
#             sum += price
#         elif buy == '2':
#
#             fare = sum * ((100 - sale) / 100)
#             print(f'할인율 : {sale} %')
#             print(f'총구매금액 : {sum}')
#             print(f'할인 적용 구매금액 : {fare}')
#             flag = False
#             checkDiscount(goods)
#         else:
#             print('잘못입력하셨습니다!')
#
# def checkDiscount(goods):
#     sum = 0
#     sale = 0
#
#     if len(goods) == 1:
#         sale = 5
#     elif len(goods) == 2:
#         sale = 10
#     elif len(goods) == 3:
#         sale = 20
#     elif len(goods) >= 4:
#         sale = 30
#     fare = sum * ((100 - sale) / 100)
#     print(f'할인율 : {sale} %')
#     print(f'총구매금액 : {sum}')
#     print(f'할인 적용 구매금액 : {fare}')
#
#
# def discountGoods(a):
#     flag = True
#     goods = []
#     sum = 0
#     sale = 0
#     while flag:
#         buy = input('상품을 구매 하시겠습니가? 1.구매, 2.종료')
#         if buy == '1':
#             price = int(input('구매한 상품의 금액은? '))
#             goods.append(price)
#             sum += price
#         else:
#             flag = False
#             checkDiscount(goods)

def checkDiscount(goods):
    rate = 0.3
    sum = 0

    if len(goods) == 1:
        rate = 0.05
    elif len(goods) == 2:
        rate = 0.1
    elif len(goods) == 3:
        rate = 0.2

    for i in range(len(goods)):
        sum += goods[i]

    fare = sum - (sum * rate)

    print(f'할인율 : {rate}')
    print(f'총구매금액 : {sum}')
    print(f'할인적용 구매금액 : {fare}')


def discountGoods():
    goods = []
    flag = True

    while flag:
        job = input('원하시는 작업을 선택하세요\n'
                    '1.구매 2. 종료')

        if job == '1':
            price = int(input('구매한 상품의 금액을 입력하세요 '))
            goods.append(price)

        elif job == '2':
            flag = False
            checkDiscount(goods)

        else:
            print('잘못입력하셨습니다!!')
