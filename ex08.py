# 차량 2부제 프로그램
# date = int(input('오늘 날짜를 입력하세요'))
from datetime import datetime as dt
date = dt.now().day
date = dt.today().day

num = int(input('차량번호 4자리를 입력하세요'))

print(f'오늘 날짜 : {date}일')
if date % 2 == 0:

    print('오늘입차 : 번호가 짝수인 차량')
    if num % 2 == 0:
        print('입차 가능합니다')
    else:
        print('입차 불가 합니다.')
else:
    print('오늘입차 : 번호가 홀수인 차량')
    if num % 2 == 0:
        print('입차 불가 합니다')
    else:
        print('입차 가능 합니다.')

#
# if num % 2 == date % 2:
#     print('입차 가능합니다')
# else:
#     print('입차 불가 합니다.')

# evenOrodd = '짝수'
# if int(date) % 2 != 0: evenOrodd = '홀수'
# print(f'오늘 입차 : 번호가 {evenOrodd}인 차량')
#
# passOrNot = '입차불가'
# if int(num) % 2 == 0 and evenOrodd == '짝수':
#     passOrNot = '입차 가능'
# print(f'귀하의 차량은 {passOrNot}합니다')