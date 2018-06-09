# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def sum(*args):
    s = 0
    for x in args:
        s += x
    return s

print(sum())
print(sum(1, 2))
print(sum(4, 1, 7, 3, 9, 2))
