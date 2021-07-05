# if문
# num = int(input('숫자를 하나 입력하세요'))
# if (num > 10) :
#     print('num은 10보다 크다')


# # 속도위반 경고하기
# speed = int(input('자동차의 현재 속도는 : '))
# if speed > 50:
#     print('속도위반!!')
# else:
#     print('>>>')


# # 합격/불합격 출력 : if ~ else
# score = int(input('점수를 입력하세요 '))
#
# if score >= 80:
#     print('합격입니다')
# else:
#     print('아쉽습니다. 다시 도전해주세요~')


# 실행문이 아직 정해지지 않은 경우 pass 키워드로 대체 작성 가능
# if score >= 80:
#     pass
# else:
#     pass


# # 자동 온도 조절장치 만들기
# temp = int(input('기계온도를 입력하세요. '))
# if temp >= 40:
#     print('팬(Fan) 가동')
# if temp < 40:
#     print('팬(Fan) 중지')


# # 입력받은 정수를 3으로 나누어 반올림해서 출력
# num = int(input('정수를 하나 입력하세요 '))
# result = num / 3
# if (result - int(result)) >= 0.5:
#     result = int(result) + 1   #소수이하자리 버린후 올림
# else:
#     result = int(result)
#
# print(f'결과 : {result}')


# mileage = int(input('마일리지를 입력하세요 '))
# if mileage >= 1000:
#     print('마일리지 사용가능')
# else:
#     print('마일리지 사용불가')


# 성적처리
# jumsu = int(input('점수를 입력하세요 '))
# if 60 <= jumsu < 70:
#     print('양')
# elif 70 <= jumsu < 80:
#     print('미')
# elif 80 <= jumsu < 90:
#     print('우')
# elif 90 <= jumsu <= 100:
#     print('수')
# else:
#     print('가')


# # 자동주문 시스템 만들기
# lang = input('Good morning. Nice to meet you. \n'
#              'where are you from? \n'
#              'please select a number \n'
#              '1.대한민국 2.USA 3.中國')
# if lang == '1':
#     print('주문하시겠어요?')
# elif lang == '2':
#     print('Would you like to order?')
# elif lang == '3':
#     print('您要点菜吗？')
# else:
#     print('Would you like to order?')


# # 국가 재난지원금 수령액 조회하기
# fam = int(input('인원수를 입력하세요. '))
# if fam == 1:
#     print('400,000원 지원')
# elif fam == 2:
#     print('600,000원 지원')
# elif fam == 3:
#     print('800,000원 지원')
# elif fam >= 4:
#     print('1,000,000원 지원')

# fam = int(input('인원수를 입력하세요. '))
# if fam == 1:
#     money = 400_000
# elif fam == 2:
#     money = 600_000
# elif fam == 3:
#     money = 800_000
# elif fam >= 4:
#     money = 1_000_000
# print(f'{money:,}원 지원')


# # BMI 지수
# BMI = int(input('BMI 지수를 입력하세요 '))
# if BMI <= 90:
#     print('저체중')
# elif 90 < BMI <= 110:
#     print('정상체중')
# elif 110 < BMI <= 120:
#     print('과체중')
# elif 120 < BMI <= 140:
#     print('비만')
# elif 140 < BMI:
#     print('고도비만')

# weight = int(input('몸무게(kg)를 입력하세요'))
# height = float(input('신장(m)을 입력하세요'))
# bmi = weight/(height*height)
#
# if bmi > 30: print('고도비만')
# elif bmi > 25: print('비만')
# elif bmi > 23: print('과체중')
# elif bmi > 18.5: print('정상체중')
# elif bmi < 18.5: print('저체중')



# # 버스 전용차로 단속 프로그램
# day = input('1.월~금, 2.토요일, 3.공휴일\n'
#             '요일을 선택하세요. ')
# if day == '1':
#    car = input('버스 전용차로 단속 중 입니다.\n'
#                '1.버스 2.승용차\n'
#                '차종을 선택하세요. ')
#    if car == '1':
#        print('버스입니다.')
#    else: print('버스 전용차로 위반!!')
# else: print('토요일 및 공휴일은 단속하지 않습니다.')




# 마스크 구매가능 요일 출력 프로그램
birth = int(input('출생 연도 끝자리 입력 : '))
age = int(input('만 나이 입력 : '))

if age >= 65:
    print('언제든지 구매 가능합니다.')
else:
    if birth == 1 or birth == 6:
        print('월요일 구매 가능합니다')
    elif birth == 2 or birth == 7:
        print('화요일 구매 가능합니다.')
    elif birth == 3 or birth == 8:
        print('수요일 구매 가능합니다.')
    elif birth == 4 or birth == 9:
        print('목요일 구매 가능합니다.')
    elif birth == 5 or birth == 0:
        print('금요일 구매 가능합니다.')
