# 근무시간에 필요한 컴퓨터 수량

# 1대로 총 24시간  해야할일
# 1대 가 1시간에 1/24
# x 시간동안 24를 채우기 위해서 몇대y가 필요한가
#
# 5 시간동안 24를 채우려면  5/24 * y = 1
# y= 24/5
# y = 24/x

# 3 * 8 = computer * hour
# computer = 3 * 8 / hour


# import math
# hour = int(input('근무시간을 입력하세요.'))
# com = math.ceil(24 / hour)
# print(f'필요한 컴퓨터 : {com}')

hour = int(input('근무시간을 입력하세요.'))
computer = 3 * 8 // hour
addCom = 1 if (3 * 8 % hour) > 0 else 0
print(f'필요한 컴퓨터수 : {computer + addCom}')

