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
