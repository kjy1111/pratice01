# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.

# a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
# - 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )

# b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
# - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )

num = input('숫자를 입력하세요: ')

if num.isalpha():
    print('숫자를 입력하세요!!!!')

elif num.isdigit():

    num = int(num)
    # sum = 0
    odd = 0
    even = 0

    for n in range(num + 1):
        if n % 2 != 0:
            odd += n

        elif n % 2 == 0:
            even += n

    print('결과 값: {}'.format(odd) if n % 2 != 0 else '결과 값: {}'.format(even))


    # if num % 2 != 0:
    #     for n in range(num + 1):
    #         if n % 2 != 0:
    #             sum += n
    #     print('결과 값: {}'.format(sum))
    #
    # if num % 2 == 0:
    #     for n in range(num + 1):
    #         if n % 2 == 0:
    #             sum += n
    #     print('결과 값: {}'.format(sum))