# 지금 현재 수지의 통장잔액이 25,000원이다. 은행이자가 연 6%라 가정할 때,
# 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지 알아보는 프로그램을 작성하세요

# 25000*(1.06 ** y) > 50000
# (1.06 ** y) > 2

n = 1
while (1.06 ** n) < 2:
    n += 1

