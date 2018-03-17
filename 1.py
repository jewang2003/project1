# 출력합니다.
print("# 문자 선택 연산자")
print('안녕하세요'[0])
print('안녕하세요'[1])
print('안녕하세요'[2])
print('안녕하세요'[3])
print('안녕하세요'[4])

# 출력합니다.
print("# 문자 선택 연산자 : 뒤에서부터 선택")
print('안녕하세요'[-1])
print('안녕하세요'[-2])
print('안녕하세요'[-3])
print('안녕하세요'[-4])
print('안녕하세요'[-5])

# 출력합니다.
print("# 문자 범위 선택 연산자")
print('"안녕하세요"[0:2]:', "안녕하세요"[0:2])
print('"안녕하세요"[1:3]:', "안녕하세요"[1:3])
print('"안녕하세요"[2:4]:', "안녕하세요"[2:4])
print()
print("#문자 범위 선택 연산자 : 한쪽 숫자 생략")
print('"안녕하세요"[3:]:', "안녕하세요"[3:])
print('"안녕하세요"[:3]:', "안녕하세요"[:3])

# 출력합니다.
print("# IndexError 예외")
print("안녕하세요"[10])


print(len("hello world!"))

print(type(len("hello world!")))
print(type("hello world!"))

print(273)
print(52.273)

print(type(273))
print(type(52.273))

print(0)
print(0.0)

print(type(0))
print(type(0.0))

print(5 + 7)
print(5 - 7)
print(5 * 7)
print(5 / 7)
print(3 // 2)
print(5 % 2)

# 출력합니다.
print("# 제곱 연산자")
print("2 ** 1=", 2**1)
print("2 ** 2=", 2**2)
print("2 ** 3=", 2**3)
print("2 ** 4=", 2**4)

print("2 + 2 - 2 * 2 / 2 * 2 =", 2 + 2 - 2 * 2 / 2 * 2)
print("2 - 2 + 2 / 2 * 2 + 2 =", 2 - 2 + 2 / 2 * 2 + 2)

print("안녕" + "하세요" * 3)

pi = 3.141592653589793238
print(pi)

# 숫자열 복합 대입 연산자
number = 100
number += 10
number += 20
number += 30
print("number:", number)

# 문자열 복합 대입 연산자
string = "안녕하세요"
string += "!"
string += "!"
print("string:", string)

# 입력을 받습니다.
string = input("입력> ")

# 출력합니다.
print(string)

# 출력합니다.
print("입력:", string)
print("자료형:", type(string))

# 입력을 받습니다.
string = input("입력> ")

# 출력합니다.
print("입력 + 100:", string +100)

input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))
print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)

# 숫자가 아닌 것을 숫자로 변형하려고 할 때
int("안녕하세요")

# format() 함수로 숫자를 문자열로 변환하기
format_output = "{}".format(52273)

# 출력하기
print(type(format_output), format_output)

# format() 함수로 숫자를 문자열로 변환하기
format_output_a = "{}원".format(3000)
format_output_b = "{} {} {}".format(1, 2, 3)
format_output_c = "{} {} {}".format(1, "문자열", True)

# 출력하기
print(format_output_a)
print(format_output_b)
print(format_output_c)

# "{} {}".format(1, 2, 3, 4, 5)
# "{} {} {}".format(1, 2) #오류 발생 

# 정수
output_a = "{:d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52) #5칸
output_c = "{:10d}".format(52) #10칸

# 빈 칸을 0으로 채우기
output_d = "{:05d}".format(52) #양수
output_e = "{:05d}".format(-52) #음수
print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈 칸을 0으로 채우기")
print(output_d)
print(output_e)

# 기호와 함께 출력하기
output_f = "{:+d}".format(52) # 양수
output_g = "{:+d}".format(-52) # 음수
output_h = "{: d}".format(52) # 양수: 기호 부분 공백
output_i= "{: d}".format(-52) # 음수: 기호 부분 공백

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

# 조합하기
output_h = "{:+5d}".format(52) # 기호를 뒤로 밀기: 양수
output_i = "{:+5d}".format(-52) # 기호를 뒤로 밀기: 음수
output_j = "{:=+5d}".format(52) # 기호를 앞으로 밀기: 양수
output_k = "{:=+5d}".format(-52) # 기호를 앞으로 밀기: 음수
output_l = "{:+05d}".format(52) # 0으로 채우기: 양수
output_m = "{:+05d}".format(-52) # 0으로 채우기: 음수

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273) # 15칸 만들기
output_c = "{:+15f}".format(52.273) # 15칸에 부호 추가하기
output_d = "{:+015f}".format(52.273) # 15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)

output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)

# 변수를 선언합니다
str_a = "Hello Python Programming...!"
# str_upper = str_a.upper()
# str_lower = str_a.lower()

# upper() 함수와 lower() 함수를 사용합니다.
# print("str.upper():", str_upper)
# print("str.lower():", str_lower)

str_a.upper()
print(str_a)
str_a.lower()
print(str_a)

input_a = """
    안녕하세요
문자열의 함수를 알아봅니다
"""


# 문자열의 함수를 사용해봅니다.
print("# 공백 제거 이전")
print(input_a)
print()

print("# 공백 제거 이후")
print(input_a.strip())

# find() 함수와 rfind() 함수 사용하기
output_a = "안녕안녕하세요".find("안녕")
output_b = "안녕안녕하세요".rfind("안녕")

# 출력하기
print("find():", output_a)
print("rfind():", output_b)
