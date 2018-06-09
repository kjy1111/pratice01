# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

for num in range(1, 100):
    s = str(num)
    c = s.count('3') + s.count('6') + s.count('9')
    if c < 1:
        continue

    print("{} {}".format(s, '짝'*c))