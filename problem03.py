# 문제3. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'

s1 = s
s1 = s1.strip('/')
s1 = s1.split('/')
print(s1)

s = s.rsplit('/', 1)
print(s)