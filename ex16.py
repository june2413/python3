# 수학시험 프로그램
quiz = ('3+2', '5//2', '10-2', '(10**2)*2', '1-(10 % 4)', '2**4', '4/2')
answers = []
solution = ['5', '2', '8', '200', '-1', '16', '2']
right = []
wrong = []
for i in quiz:
    answer = input(f'문제 : {i}')
    answers.append(answer)


for i in range(7):
    if answers[i] == solution[i]:
        right.append('정답')
    else:
        wrong.append('오답')
print('정답 개수 : ', len(right))
print('오답 개수 : ', len(wrong))


# 2
quiz = ['3+2 = ','5÷2의 몫 = ', '10-2 = ', '10²x2 = ', '1-(10÷4의 나머지)']
answer
point