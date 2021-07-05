# 자동심장 충격기 생존율
msg = '최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요.'
time = int(input(msg))

# if time > 360:
#     print('생존율 : 25%미만')
# elif 300 >= time > 240:
#     print('생존율 : 47%')
# elif 240 >= time > 180:
#     print('생존율 : 57%')
# elif 180 >= time > 120:
#     print('생존율 : 66%')
# elif 120 >= time > 60:
#     print('생존율 : 76%')
# elif  time <= 60:
#     print('생존율 : 85%')

live = 25
if time > 360: live = 25
elif time > 300: live = 47
elif time > 240: live = 57
elif time > 180: live = 66
elif time > 120: live = 76
elif time > 60: live = 85
else: live = 90
print(f'생존율 : {live}%')
