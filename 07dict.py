# 딕셔너리
ages = {'박찬호':48, '박지성':40, '박세리':50, '이승엽':43}

person = {'이름':'홍길동', '나이':25, '주소':'서울 종로구 삼일대로', '몸무게':88.8,
          '취미':['운동', '독서', '영화감상']}

sungjuk = {'C/C++':'A', 'Java':'B+', '네트워킹':'C',
           '보안':'A+', '해킹':'F', '시스템':'C+'}

# 홍길동의 나이와 취미 조회
person['나이']
person['취미']

# 홍길동의 혈액형 추가
# dict에 새로운 항목을 추가할때는
# 새로운 키와 값으로 구성해야 함
person['혈액형'] = 'A'
person

# dict에 기존 키와 값으로 구성한 항목을
# 추가하려 하면 기존키에 저장된 값이 변경됨
person['혈액형'] = 'O'

# dict에서 항목 삭제 : pop, remove
person.pop('몸무게')

# 반복문으로 삭제
dellist = ['나이', '취미']
for key in dellist:
    person.pop(key)

print(person)

# dict 모든항목 출력
person = {'이름':'홍길동', '나이':25, '주소':'서울 종로구 삼일대로', '몸무게':88.8,
          '취미':['운동', '독서', '영화감상']}

for key in person.keys():
    print(person[key])

# dict 의 키와 값 모두 가져오기 : items
person.items()

for k, v in person.items():
    print(k, v)

# 중간고사 성적관리 프로그램 만들기
midsj = {'C/C++':'A', 'Java':'B+', '모바일':'C',
           '보안':'A+', '해킹':'F', '시스템':'C+'}
midsj['Java']
midsj['시스템']
midsj['파이썬'] = 'A'
midsj['OS'] = 'A+'
midsj['Java'] = 'F'
midsj['시스템'] = 'A'
print(midsj.items())

for key in midsj.keys():
    print(key, '\t: ',midsj[key])

for k, v in midsj.items():
    print(f'{k} : {v}')

# 딕셔너리 for 축약문
# { 키/값 표현식 for 키,값 in zip(반복가능객체1, 반복가능객체2)}
# 이름과 성적 리스트를 dict 객체로 재생성하세요
name = ['혜교', '지현', '수지']   # 키
grd = ['수', '양', '미']         # 값
sj = {}

sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]

# 반복문 사용
for i in range(3):
    sj[name[i]] = grd[i]

# dict 컴프리헨션
# { 키/값 표현식 for 키,값 in zip(반복가능객체1, 반복가능객체2)}
sj2 = {key:val for key, val in zip(name, grd)}

# zip : 여러개의 데이터를 하나로 합쳐서
# iterable한 객체로 생성해 줌 = 개별 객체는 튜플로 반환
for pair in zip(name, grd):
    print(pair)


