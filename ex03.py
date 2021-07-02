# 이름, 국어, 영어, 수학을 입력 받아
# 총점, 평균, 학점을 출력하는 프로그램

name = input('이름을 입력하세요')
kor = int(input('국어점수를 입력하세요'))
eng = int(input('영어점수를 입력하세요'))
mat = int(input('수학점수를 입력하세요'))
tot = kor + eng + mat
avg = tot / 3

grd = '수' if (avg >= 90) else \
        '우' if(avg>=80) else \
        '미' if(avg>=70) else \
        '양' if(avg>=60) else '가'

print(f'이름 : {name}, 국어 : {kor}, 영어 : {eng},수학 : {mat}, 총점 : {tot}'
      f'평균 : {avg}, 학점 : {grd}')


# if avg >= 90 : grd = '수'
# elif avg >= 80 : grd = '우'
# elif avg >= 70 : grd = '미'
# elif avg >= 60 : grd = '양'
# else : grd = '가'

print(f'이름 : {name}')
print(f'국어 : {kor}')
print(f'영어 : {eng}')
print(f'수학 : {mat}')
print(f'총점 : {tot}')
print(f'평균 : {avg}')
print(f'학점 : {grd}')

