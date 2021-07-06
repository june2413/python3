# 한빛역에는 3개노선의 열차가 오전 9시부터 오후 6시까지 교차운행한다.
# 3대의 열차가 교차하는 시간을 구해 열차 충돌 사고를 막아 봅니다
train1 = 10
train2 = 25
train3 = 30

for i in range(1, 540+1):
    hour = (i // 60) + 9
    min = i % 60

    if i % train1 == 0 and i % train2 == 0:
        print(f'A열차와 B열차 충돌! {hour}시 {min}분')
    elif i % train2 == 0 and i % train3 == 0:
        print(f'B열차와 C열차 충돌! {hour}시 {min}분')
    elif i % train3 == 0 and i % train1 == 0:
        print(f'C열차와 A열차 충돌! {hour}시 {min}분')

