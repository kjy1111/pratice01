# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

l = []
s = 0

while len(l) != 5:
    n = input('>')
    if n.isalpha():
        print('정수를 입력해 주세요.')
        continue
    elif n.isdigit():
        n = int(n)
        s += n
        l.append(n)

print('평균: {}'.format(s/len(l)))