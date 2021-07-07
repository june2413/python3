# 헌혈 프로그램
# 1
abos = []
for i in range(10):
    abo = input('혈액형을 선택하세요 : ')
    abos.append(abo)
abos.sort()
abos
print('A형 : ', len(abos[:abos.index('ab')]),
      'B형 : ', len(abos[abos.index('b'):abos.index('o')]),
      'AB형 : ', len(abos[abos.index('ab'):abos.index('b')]),
      'O형 : ', len(abos[abos.index('o'):]),)

# 2
a = []
b = []
ab = []
o = []
for i in range(10):
    blood = input('헌혈해주셔서 감사합니다.\n'
            '혈액형을 선택하세요 (A,B,AB,O) ')
    if blood == 'A' or blood == 'a': a.append(blood)
    elif blood == 'B' or blood == 'b': b.append(blood)
    elif blood == 'AB' or blood == 'ab': ab.append(blood)
    elif blood == 'O' or blood == 'o': o.append(blood)
print(f'혈액형 수급 현황\n'
      f'A형 : {len(a)}\n'
      f'B형 : {len(b)}\n'
      f'AB형 : {len(ab)}\n'
      f'O형 : {len(o)}\n')

# 3
bloods = []
for i in range(10):
    blood = input('헌혈해주셔서 감사합니다.\n'
            '혈액형을 선택하세요 (A,B,AB,O) ')
    bloods.append(blood)

print('-'*30)
print(f'혈액형 수급 현황')
print('-'*30)
print(f'A형 : {bloods.count("A")}')
print(f'B형 : {bloods.count("B")}')
print(f'AB형 : {bloods.count("AB")}')
print(f'O형 : {bloods.count("O")}')
print('-'*30)