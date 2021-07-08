# 다국어 인사말 프로그램

def sayHello(country):

    if country == '1':
        print('안녕')
    elif country == '2':
        print('Hello')
    elif country == '3':
        print('こんにちは')
    elif country == '4':
        print('你好')

country = input('where are you from? 1.한국 2.USA 3.Japan 4.China')

sayHello(country)



