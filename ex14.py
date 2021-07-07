# 출석부 관리 시스템
students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우',
            '박찬호', '이승엽']
students.sort()                  # 가나다순 정리
students
students.remove('박찬호')         # 박찬호 삭제
print(students, len(students))   # 전체 값들과 값들의 갯수 출력
students[:3]                     # 앞에서 3개의값
students.insert(5, '이병규')      # 이병규 추가
students.sort(reverse=True)      # 역순 정리
students.reverse()
students.index('정우람')          # 정우람 인덱스값 확인
students[1] = '정잘남'            # 정우람을 정잘남으로 변경
