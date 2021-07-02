# 수온 계산기

# 0 <= x <10 20
# 10<= x <20 19.3
# +i          -0.7*(i//10)


# depth = int(input('수심을 입력하세요.'))
# temp = 20-(0.7*(depth//10))
# print(f'수온 : {temp}')

depth = int(input('수심을 입력하세요.'))
temp = 20
temp = temp - (depth // 10 * 0.7)
print(f'수온 : {temp}')