# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요

num = input("수를 입력하세요:")

if int(num) == 0 or int(num) == 1:
    print('3의 배수가 아닙니다')

elif num.isalpha():
    print('정수가 아닙니다.')

elif num.isdigit():
    print('3의 배수 입니다.' if int(num) % 3 == 0 else '3의 배수가 아닙니다.')