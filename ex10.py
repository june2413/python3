# 전기 요금 계산기
# elec = int(input('전기 사용량을 입력하세요. '))
# print(f'사용량 : {elec}kwh')
# if elec <= 200:
#     print((elec * 99.3) + 910)
# elif 200 < elec < 400:
#     print((elec * 187.9) + 1600)
# else:
#     print((elec * 280.6) + 7300)

etro = int(input('전기 사용량을 입력하세요. '))
rate = 0  #기본요금
price = 0   # 단가

if etro > 400:
    rate = 7300
    price = 280.6
elif etro > 200:
    rate = 1600
    price = 187.9
elif etro <= 200:
    rate = 910
    price = 99.3

fare = rate + (etro * price)

print(f'\n사용량 : {etro:.1f} kwh\n'
      f'기본요금 : {rate:,}원 \n'
      f'단가 : {price} 원\n'
      f'전기요금 : {fare:,} 원')

