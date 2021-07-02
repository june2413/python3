num1 = 10
num2 = 20
num3 = num1 + num2

num1 = 30.5
num2 = 50.5
num3 = num1 + num2

num1 = 10
num2 = 50.5
num3 = num1 + num2

# 매출액 구하기
# month1 = int(input('1월의 매출을 입력하세요'))
# month2 = int(input('2월의 매출을 입력하세요'))
# month3 = int(input('3월의 매출을 입력하세요'))
# quater1 = month1 + month2 + month3
#
# print('1월 매출 : %d' % (month1))
# print('2월 매출 : %d' % (month2))
# print('3월 매출 : %d' % (month3))
# print('1분기 전체 매출 : %d' % (quater1))
#
# print('1분기 전체 매출 : {0}'.format(quater1))

num1 = 3.14
num2 = 0.25
num3 = num1 + num2
num3 = float(num3)
num3 = int(num3)

# # 수익 구하기
# sales1 = int(input('1분기 매출을 입력하세요'))
# buy1 = int(input('1분기 매입을 입력하세요'))
# profit = sales1 - buy1
# print('1분기 매출 : {0}'.format(sales1))
# print('1분기 매입 : {0}'.format(buy1))
# print('수익 : {0}'.format(profit))

# # 방 넓이 구하기
# width = int(input('가로길이를 입력하세요'))
# height = int(input('세로길이를 입력하세요'))
# area = width * height
# print('가로길이 : {0}'.format(width))
# print('세로길이 : {0}'.format(height))
# print('넓이 : {0} ㎠'.format(area))

str1 = 'Hello, World!! '
str1 * 3
3 * str1 * 2

# BMI 구하기
# weight = int(input('몸무게(kg)를 입력하세요'))
# height = float(input('신장(m)을 입력하세요'))
# bmi = weight/(height*height)
# print('몸무게(kg) : {0}'.format(weight))
# print('신장(m) : {0}'.format(height))
# print('BMI : {0:.2f}'.format(bmi))
# print(f'BMI : {bmi:.2f}')   # f-string : py 3.6 부터 지원

# print 출력속도 : .format > % > f-string


# 홀짝 게임하기
# coin = int(input('손 안에 동전 수를 입력하세요.'))
# isEven = coin % 2
# print(f'동전의 홀짝여부 (0:짝, 1:홀) : {isEven}')
# if isEven == 1 : print('홀')
# else: print('짝')

20 // 3     # 정수만 출력


# 빵 나누어 주기
# 빵, 나눠줄 빵 갯수 입력 받음
# 최대 몇명까지 나눠 줄수 있는지와 남는 빵 갯수 출력
# bread = int(input('빵의 총 갯수는?'))
# diver = int(input('나눠줄 빵의 갯수는?'))
# stud = bread // diver
# divmod = bread % diver
#
# print(f'{bread}개의 빵은 {diver}개씩, {stud}명의 학생에게 나눠줄 수 있고,')
# print(f'{divmod}개의 빵이 남음')

2 ** 3
2 ** 7
2 ** 8

2 ** 30

# 복리 계산기
# 원금, 유치기간, 연이율을 입력받아 복리 계산 후 총수령액 출력

money = 5000000
duration = 5
interest = 0.05
takes = money + (money * 0.05)
# takes = takes + (takes * 0.05)
# takes = takes + (takes * 0.05)
# takes = takes + (takes * 0.05)
# takes = takes + (takes * 0.05)
takes += takes * 0.05
takes += takes * 0.05
takes += takes * 0.05
takes += takes * 0.05

money * 1.05 ** 5


# 놀이기구 탑승 가능 판별
# height = int(input('어린이의 신장을 입력하세요'))
# isRide = height >=120
# print(height >= 120)
# print(f'탑승 가능여부 : {isRide}( true : 탑승가능)')
# print(f'{isRide}')
#
# if height >= 120 : print('탑승이 가능합니다')
# else : print('탑승하실 수 없습니다.')

'a' >= 'b'  # 아스키코드로 변환 후 비교
'a' <= 'b'

# 놀이기구 탑승 가능 판별 2
# height = int(input('어린이의 신장을 입력하세요.'))
# # isRide = height >= 120 and height < 170
# isRide = 120 <= height < 170
#
# print(f'탑승 가능 여부 {isRide}')
#
# if height >= 120 and height < 170 : print('탑승 가능합니다')
# else : print('탑승 불가합니다')
#
# if isRide : print('탑승 가능합니다')
# else : print('탑승 불가합니다')

# short circuit evaluation
num1 = 17
num2 = 20
(num1 < 15) and (num2 > 15)     # False and True

num1 = 10
num2 = 20
(num1 < 15) or (num2 < 15)     # True and False

# (num1 < 5) and xyz


# 삼항 연산자
# 참일때값 if 조건식 else 거짓일때 값

num = 11
'짝수' if num % 2 == 0 else '홀수'

# # 적자/흑자 판단하기
# income = input('수입을 입력하세요.')
# outcome = input('지출을 입력하세요.')
# print('적자' if income < outcome else '흑자')
# if income < outcome : print('적자')
# else: print('흑자')


# 윤년 여부 알아보기
# 4로 나누어 떨어지고 100으로 나누어 떨어지지 않음
# 400으로 나누어 떨어짐
# year = int(input('년도를 입력하세요'))
# isLeap = ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
# print('윤년' if (isLeap) else '평년')
#
# if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) : print('평년')
# else : print('윤년')


# operator 모듈을 이용하면 대량의 데이터 처리시 속도 향상이 존재함
import operator as op

op.add(10, 20)
op.sub(10, 20)
op.mul(10, 20)
op.floordiv(10, 3)  # 정수 몫 : //
op.truediv(10, 3)  # 실수 몫 : /
op.mod(10, 3)

op.eq(10, 20)
op.ne(10, 20)
op.gt(10, 20)
op.lt(10, 20)
op.ge(10, 20)
op.le(10, 20)

x = op.eq(10, 20)
y = op.gt(10, 20)
op.and_(x, y)
op.or_(x, y)

# 긴급 재난 지원금 대상자 판별하기
# 소득기준 4,000,000원 이하
# 다른지원금을 받지 않는 세대
income = int(input('소득을 입력하세요.'))
another = int(input('다른 지원금을 받고 있습니까? 1번 받고 있다. 2번 받고 있지 않다.'))
isTarget = op.and_(op.le(income, 4_000_000), op.eq(another, 2))
result = '수급대상자' if (isTarget) else '수급 미대상자'
print(result)


