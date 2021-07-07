# 컴프리헨션 comprehension
# 반복문 축약
# 파이썬에서는 4가지 축약을 지원
# list(py2) set, dict, generator(py3)

# 다양한 데이터객체에 사용하는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원하는 기능

# 1~10 정수를 리스트에 저장
numlist = []
for i in range(1, 11):
    numlist.append(i)

# for 축약문
# [표현식 for 항목 in 반복가능객체]
numlist2 = [i for i in range(1, 10+1)]

# ex) 0~20 사이 짝수를 리스트로 저장
evenlist = []
for i in range(2, 21, 2):
    evenlist.append(i)
evenlist2 = [i for i in range(2, 21, 2)]

# ex) 1~10사이 제곱수를 리스트로 저장
sqrlist = []
for i in range(1, 10+1):
    sqrlist.append(i*i)

sqrlist2 = [i ** 2 for i in range(1, 11)]

# ex) 다음 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트로 생성하세요

val = [1, 2, 'A', False, 9, 100]
sqrlist3 = [v ** 2 for v in val]

sqrlist3 = []
for v in val:
    if type(v) == int:
        sqrlist3.append(v ** 2)

# for if 축약문
# [표현식 for 항목 in 반복가능객체 if 조건]
sqrlist4 = [v ** 2 for v in val if type(v) == int]

# ex) 1 - 50 사이 홀수를 리스트로 저장
oddlist = [i for i in range(1, 50+1) if i % 2 == 1]

oddlist = []
for i in range(1, 51):
    if i % 2 == 1:
        oddlist.append(i)

# 다중 조건을 사용하는 for 축약문
# [표현식1 if 조건 else 표현식2 for 항목 in 반복가능객체 ]

# ex) 1 - 100 사이 정수중 짝수면 even, 홀수면 odd로 구분해서 리스트로 저장
evenodd = ['even' if i % 2 == 0 else 'odd' for i in range(1, 100+1)]

# 중첩 for문을 사용하는 for 축약문
# [표현식 for 항목1 in 반복가능객체1 ]
#        for 항목2 in 반복가능객체2 ]

# ex) 구구단 중 7단, 8단 계산값을 리스트에 저장
gugu = []
for i in range(7, 8+1):
    for j in range(1, 9+1):
        gugu.append(i * j)

gugu2 = [i * j for i in range(7, 8+1)
         for j in range(1, 9+1)]

# ex) 1~100 사이의 제곱수가 아닌 수를
# 찾아서 리스트로 생성 ( 제안 : sqrt()함수 사용)

from math import sqrt

square = [i for i in range(1, 100+1) if sqrt(i) % 1 != 0]

