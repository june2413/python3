# 날씨 예보 프로그램
print('날씨 정보를 입력하세요')
day = input('요일을 입력하세요')
date = input('날짜를 입력하세요 (월일)')
mintemp = int(input('아침 최저기온을 입력하세요'))
maxtemp = int(input('낮 최고기온을 입력하세요'))
rainprop = int(input('비올확율을 입력하세요'))
airrate = input('미세먼지 수치를 입력하세요')
sunrise = input('일출 시간을 입력하세요')
sunset = input('일몰 시간을 입력하세요')
southwave = float(input('남해 앞바다 물결을 입력하세요'))
eastwave = float(input('동해 앞바다 물결을 입력하세요'))
westwave = float(input('서해 앞바다 물결을 입력하세요'))

print('내일 날씨 예보입니다.')
print(day + '요일인' + date +
      '의 아침 최저 기온은'+ str(mintemp) + '도, 낮 최고 기온은' +
      str(maxtemp) + '도로 예보됐습니다.')
print('비올 확률은 ' + str(rainprop) + '%이고, 미세먼지는' +
    airrate + ' 수준일 것으로 예상됩니다')
print('일출시간은 ' + sunrise + '이고, 일몰시간은 ' + sunset + '입니다')
print('바다의 물결은 남해 앞바다 ' + str(southwave) +
      'm, 동해 앞바다' + str(eastwave) + 'm, 서해앞바다 ' +
      str(westwave) + 'm, 높이로 일겠습니다.')
print('지금까지 ' + date +' ' + day + '요일 날씨 예보였습니다.')

print('------------------------------')
print('내일 날씨 예보입니다.')
print('{0}요일인 {1}의 아침 최저 기온은 {2}도, 낮 최고 기온은 {3}도로 예보됐습니다.'
      .format(day, date, mintemp, maxtemp))
print('비올 확률은 {0}%이고, 미세먼지는 {1}수준일 것으로 예상됩니다'
      .format(rainprop, airrate))
print('일출시간은{0} 이고, 일몰시간은 {1}입니다'
      .format(sunrise, sunset))
print('바다의 물결은 남해 앞바다 {0}m, 동해 앞바다{1}m, 서해앞바다 {2}m, 높이로 일겠습니다.'
      .format(southwave, eastwave, westwave))
print('지금까지 {0} {1}요일 날씨 예보였습니다.'
      .format(date, day))

print('------------------------------')
print('내일 날씨 예보입니다.')
print('%s요일인 %s의 아침 최저 기온은 %d도, 낮 최고 기온은 %d도로 예보됐습니다.'
      % (day, date, mintemp, maxtemp))
print('비올 확률은 %d이고, 미세먼지는 %s수준일 것으로 예상됩니다'
      % (rainprop, airrate))
print('일출시간은 %d 이고, 일몰시간은 %s입니다'
      % (sunrise, sunset))
print('바다의 물결은 남해 앞바다 %fm, 동해 앞바다 %fm, 서해앞바다 %fm, 높이로 일겠습니다.'
      % (southwave, eastwave, westwave))
print('지금까지 %s %s 요일 날씨 예보였습니다.'
      % (date, day))