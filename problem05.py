# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
#   없이 각 단어를 순서대로 출력하세요.

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.upper()
s = s.replace(',', '')
s = s.replace('.', '')
s = s.replace('\n', '')
s = s.split(' ')

s1 = s
s1 = set((s))
lst = list(s1)
lst.sort()

for lis in lst:
    print(lis, end = '\n')


# 2)각 단어의 빈도수도 함께 출력해 보세요
print('-----------------------------------')

s2 = s
lst1 = list(s2)
lst1.sort()

count = {}

for lis1 in lst1:
    if lis1 in count.keys():
        count[lis1] += 1
    else:
        count[lis1] = 1

for key, value in count.items():
    print("{}: {}".format(key, value))