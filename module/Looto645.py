#
# import random
# a = []
# b = []
# for i in range(6):
#     num = input('1부터 45까지의 정수 6개를 입력하세요.')
#     a.append(num)
#     bnum = random.randint(1, 45)
#     b.append(bnum)
#
# li = []
# for i in range(6):
#     for j in range(6):
#         if a[i] == b[j]:
#             li.append(a[i])
#
#
# print('이번주 로또번호', b)
# print(li())

import random as r
# def readLotto():    # 입력받는 번호
#     magic = []
#     for i in range(6):
#         val = input(f'1부터 45까지의 정수를 하나 입력하세요 ({i+1}/6) :')
#         magic.append(int(val))
#     return magic

# def makeLotto():    # 랜덤 생성 번호
#     magic = []
#     for i in range(6):
#         magic.append(r.randint(1,45))
#     return magic

def readLotto():    # 입력받는 번호
    magic = []
    i = 0
    while len(magic) < 6:
        val = int(input(f'1부터 45까지의 정수를 하나 입력하세요 ({i+1}/6) :'))
        if magic.count(val) == 0:   # 입력한 정수가 magic 리스트에 존재하는지 검사
            magic.append(val)
            i += 1
    return magic

def makeLotto():    # 랜덤 생성 번호
    magic = []
    while len(magic) < 6:
        val = r.randint(1,45)
        if magic.count(val) == 0:
            magic.append(val)
    return magic

def Lotto645():
    magic = readLotto()
    lotto = makeLotto()
    wins = []
    for v in magic:
        if lotto.count(v) != 0:
            wins.append(v)

    print('나의 로또번호', lotto)
    print(f'이번 로또번호', magic)
    print(f'일치하는 숫자', wins)


