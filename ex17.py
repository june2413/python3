# 회원가입 프로그램

idpd = {}
join = input("'1.회원가입', '2.프로그램 종료'")
if join == '1':
    uid = input('아이디 : ')
    passwd = input('비밀번호 : ')
    idpd[uid] = passwd
else:
    print(idpd)
idpd

#2
members = {}
flag = True

menu = '-'*30
menu += '\n 회원가입 프로그램\n'
menu = '-'*30
menu += '\n 1.회원가입\n'
menu += '2. 회원가입 프로그램\n'
menu = '-'*30

while flag:
    print(menu)
    choice = input('작업을 선택하세요 : ')
    if choice == '1':       # 회원가입
        userid = input('아이디는?')
        passwd = input('비밀번호는?')
        members[userid] = passwd

    elif choice == '2':     # 가입한 회원들을 출력한후 종료
        print('프로그램종료')
        print('가입한 회원들은 다음과 같습니다')
        for u, p in members.items():
            print(f'{u} : {p}')
        flag = False
