# 반복문
# 1~10 까지 정수 출력
for i in range(1, 10+1,):
    print(i)


# 2~10 사이 짝수 출력
for i in range(2, 10+1, 2):
    # print(i)
    print(i, end=' ')

for i in range(2, 10+1):
    if i % 2 == 0: print(i)


# 입력한 횟수만큼 메일발송 문자열 출력
times = int(input('메일 발송 횟수를 입력하세요. '))
for times in range(times):
    print('메일발송!')


# 1~10 사이의 정수출력, 3의배수는 '3의배수' 출력
for i in range(1, 10+1):
    print(f'num = {i}')
    if i % 3 == 0:
        print('3의 배수!')

for i in range(1, 10+1):
    if i % 3 == 0:
        print('3의 배수!')
    else: print(f'num = {i}')

# 구구단 5단 출력하기
for i in range(1, 10):
    print(f'5 x {i} = {5*i}')

# 사용자로부터 숫자(1 - 9)를 하나 입력 받아, 구구단을 출력하는 프로그램을 작성해보세요
dan = int(input('출력할 단을 입력하세요'))
for i in range(1, 10):
    print(f'{dan} x {i} = {dan * i}')


# 1~10 까지 정수의 합 출력
sum = 0
for i in range(1, 11):
  sum += i
print(sum)


 # 3 과 7의 공배수와 최소공배수
# data = []
# for i in range(1, 101):
#     if i % 3 == 0 and i % 7 == 0:
#         print(i)
#         data.append(i)
# print('최소공배수 :', min(data))

for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0:
        print(i)

min = 100
for i in range(100, 1, -1):
    if i % 3 == 0 and i % 7 == 0:
        if min >= i: min = i
        print(i, end=',')
print('최소공배수 : ', min )

# -10~0까지 정수 출력
for i in range(-10, 1, 1):
    print(i, end=',')

# 1 ~ 10까지 출력
for i in range(10):     # range(시작과 단계를 생략할수 있음 생략시 0에서 시작하고 1단계씩증가)
    print(i + 1)

# 반복문에 range 대신 문자열 사용
for ch in 'Hello':
    print(ch, end=',')
print()

# 50 보다 작은 7의배수
for i in range(51):
    if i % 7 == 0:
        print(i, end=',')
print()

# 1~10 까지 출력
num = 1
while num < 11:
    print(num)
    num += 1

# 1~30 까지의 정수중 홀수와 짝수를 구분하여 출력하기
num = 1
while num <= 30:
    if num % 2 == 0:
        print(f'짝수 : {num}')
    else:
        print(f'홀수 : {num}')
    num += 1

# 구구단 3단 출력하기
i = 1
while i <= 9:
    print(f'3 x {i} = {3 * i}')
    i += 1

# 1~100 까지 정수중 3과 8의 공배수와 최소공배수 출력하기
i = 1
min = 100
while i <= 100:
    if i % 3 == 0 and i % 8 == 0:
        print(f'공배수 : {i}')
        if min > i:
            min = i
    i += 1
print(f'최소공배수 : {min}')

# 게임 진행과 종료
flag = True
while flag:
    code = int(input('1: 진행, 2: 종료'))
    if code == 1:
        print('게임진행')
    else:
        flag = False
        print('게임종료')

# 1 ~ 50까지 정수중 3의 배수를 더하기
sum = 0
for i in range(1, 51):
    if i % 3 != 0: continue
    sum += i
print(sum)

sum = 0
for i in range(1, 51):
    if i % 3 == 0:
        sum += i
print(sum)

# 1 ~ 100까지 모든 정수 더하기. 단, 정수의 총합이 500이 넘었을때의 정수는 무엇인가?
sum = 0
for i in range(1, 101):
    sum += i
    if sum >= 500:
        print(i)
        break
print(sum, i)

# 1 ~ 10까지 정수의 총합을 구하고 반복이 끝나는 경우 완료 메세지 출력
sum = 0
for i in range(10):     # 0~9
    sum += (i + 1)
else:
    print(f'총합 계산 끝! : {sum}')

# 삼각형의 넓이 구하기. 너비가 150을 넘으면 프로그램종료
width = 2
height = 3
area = 0
while area <= 150:
    area = (width * height) / 2
    print(area, width, height)
    width += 2
    height += 3



# 1 ~ 100 중 5 또는 7의 배수를 제외한 정수 출력
for i in range(101):
    if i % 5 != 0 and i % 7 != 0:
        print(i)

for i in range(101):
    if i % 5 == 0 or i % 7 == 0: continue   # 조건에 해당하면 처음으로 이동
    print(i, end=',')


# 구구단 출력
for j in range(2, 10):
    for i in range(1, 10):
        print(f'{j} x {i} = {i * j}\t', end=' ')

for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j:2d} x {i:2d} = {i * j:2d}\t', end=' ')
    print()
print()








