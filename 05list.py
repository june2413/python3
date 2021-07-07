# 파이썬 리스트
attendList = ['순철', '병현', '민우', '찬호', '민태']
print(attendList)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

complex = [1, 2.0, 3.1415, 40, '5', "6"]
print(complex)

for data in numbers:
    print(data)

for data in complex:
    print(data)


len(numbers)
len(complex)

msg = 'Hello, World!!'
len(msg)

msg = input('메세지를 입력하세요. ')
print(len(msg))


# 리스트의 모든항목 조회
print(complex[0])
print(complex[1])
print(complex[2])
print(complex[3])
print(complex[4])
print(complex[5])

for i in range(len(complex)):
    print(complex[i])

for item in complex:
    print(item)

for idx, item in enumerate(complex):
    print(f'{idx}, {item}')

print(complex.index(3.1415))

# 마지막 인덱스값 출력
sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
print(sports.index('soccer'))
print(sports[len(sports)-1])
print(len(sports)-1)

# python 문자열의 인덱스 값 출력
languages = ['c/c++', 'c#', 'python', 'java']
print(languages.index('python'))

# 리스트 마지막에 삽입 append() 함수
# 특정위치에 삽입 insert()함수

# 취미 추가하기 마지막에 리스트 추가
hobby = ['독서', '등산', '요리']
print(f'홍길동 학생의 취미 : {hobby}')
hobby.append('배구')
print('홍길동 학생의 취미 :', hobby)

# 1 ~ 10 누락된 숫자 추가하기
number = [1, 2, 3, 4, 5, 7, 8, 9]
number.insert(5, 6)
print(number)
number.insert(9, 10)
print(number)


weather = ['The', 'weather', 'very']
weather.insert(2, 'is')
weather.insert(4, 'cold')
print(weather)


# 성적처리 프로그램 3명 학생 데이터 입력 후
# 총점, 평균, 학점 처리 후 결과 출력
names = []
kors = []
engs = []
mats = []


for i in range(3):
    name = input('이름은? ')
    names.append(name)
    kor = int(input('국어는? '))
    kors.append(kor)
    eng = int(input('영어는? '))
    engs.append(eng)
    mat = int(input('수학은? '))
    mats.append(mat)


tots = []
avgs = []
grds = []
for i in range(3):
    tots.append(kors[i] + engs[i] + mats[i])
    avgs.append(tots[i] / 3)
    grds.append('가')
    if avgs[i] >= 90: grds[i] = '수'
    if avgs[i] >= 80: grds[i] = '우'
    if avgs[i] >= 70: grds[i] = '미'
    if avgs[i] >= 60: grds[i] = '양'

for i in range(3):
    print(f'{names[i]}, {kors[i]}, {engs[i]}, {mats[i]}\n'
          f'{tots[i]}, {avgs[i]}, {grds[i]}\n')

# 리스트 수정
# 리스트[인덱스] = 수정할값
hobby
hobby[1] = '여행'
hobby


# 리스트 삭제
# pop() 함수 : 리스트 맨 끝 아이템을 삭제
# pop(인덱스값) : 해당인덱스의 아이템을 삭제
hobby
hobby.pop()

sports
sports.pop(2)

# remove : 항목으로 제거
languages
languages.remove('java')
languages.remove('c/c++')

# 과일리스트에서 당근,토마토 삭제
fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
fruits.remove('당근')
fruits.remove('토마토')
fruits.pop(2)   # 위치 값으로 삭제
fruits.pop(5)
fruits

# 합격 여부 판정
# 매과목 40점이상, 전과목 평균 60점 이상
exam = [80, 40, 70, 90, 85, 40]

cnt = len(exam)
sum = 0
fails = 0
result = '아쉽습니다. 불합격하셨습니다.'

for i in range(cnt):
    if exam[i] < 40: fails += 1     # 과락수 증가
    sum += exam[i]

avg = sum / cnt
if fails == 0 and avg >= 60:
    result = '축하합니다. 합격하셨습니다'

print(f'평균점수 : {avg:.2f}')
print(result)

# 정렬하기
numbers = [5, 1, 3, 4, 2, 6]
numbers.sort()
numbers

numbers.sort(reverse=True)
numbers

# 내림차순 정렬하기
score = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
score.sort(reverse=True)
score

# 문자 정렬 (한글)
names = ['김길동', '박길동', '이길동', '정길동', '홍길동']
names.sort(reverse=True)
names
# 문자 정렬 (영어)
units = ['scv', 'marine', 'firebat', 'ghost', 'dropship', 'battlecruiser',
         'valkyrie', 'medic']
units.sort(reverse=True)
units

# 리스트 슬라이싱
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 리스트 역순 출력
alphabet.sort(reverse=True)
alphabet

# 인덱스 2~5까지의 아이템을 출력
alphabet[2:6]
# 인덱스 0~4까지의 아이템을 출력
alphabet[:5]
# 인덱스 3~7까지의 아이템을 출력
alphabet[3:8]
# 인덱스 5부터 끝까지의 아이템을 출력
alphabet[5:]
# 인덱스 3~8까지의 아이템을 출력
alphabet[3:9]
# 6~ 끝까지 추출
alphabet[6:]
alphabet[-4:]  # 끝에서부터 왼쪽방향으로 4번째 요소에서 시작

# 슬라이싱 고급기능
alphabet[::-1]
alphabet[1::-1]
alphabet[3::-1]
alphabet[:-3:-1]

# d,c,b,a 추출
# step 기본값이 1인데 -7, -10의 경우 -7의 값이 리스트 위치상 -10보다 뒤에 있기 때문에
# step을 임의로 -1로 설정해주어야 한다.
alphabet[-7::-1]
alphabet[3::-1]
alphabet[-7:-11:-1]



# g,h,e,d 추출





