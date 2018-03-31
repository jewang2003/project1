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


dictionary = {
	"name": "7D 건조망고",
	"type":"당절임",
	"ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
	"origin":"필리핀"
}

for key in dictionary:
        print(key,":",dictionary[key])

print(range(5), list(range(5)))
print(range(10), list(range(10)))
print()

print(range(0,5), list(range(0,5)))
print(range(5,10), list(range(5,10)))
print()

print(range(0,10,2), list(range(0,10,2)))
print(range(0,10,3), list(range(0,10,3)))
print()


for i in range(10):
        print(str(i) + "번째 반복입니다")
print()

for i in range(5):
        print(str(i) + " =반복 변수")
print()

for i in range(5, 10):
        print(str(i) + " =반복 변수")
print()

for i in range(0, 10, 3):
        print(str(i) + " =반복 변수")
print()

array = [273, 32, 103, 57, 52]

for i in range(len(array)):
        print("{}번째 반복: {}".format(i, array[i]))
print()

for i in reversed(range(10)):
        print("{}번째 반복".format(i))
print()


i = 0
while i<10:
        print("{}번째 반복입니다.".format(i))
        i += 1
print()

list_test = [1,2,1,2]
value = 2
while value in list_test:
        list_test.remove(value)

print(list_test)
print()

#import time
#output = 0
#target_tick = time.time() + 5
#while time.time() < target_tick:
#        output += 1
#print("5초 동안 반복한 횟수:", output)
#print()
i=0

# while True:
#        print("{}번째 반복문 입니다.".format(i))
#        i=i+1
#        input_text = input("> 종료하시겠습니까?(y): ")
#        if input_text in ["y", "x"]:
#                print("반복을종료합니다.")
#                break
#print()


numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
        if number < 10:
                continue
        print(number)
print()


string = "Hello Programing"

output = string.upper()
print("string.upper():", output)

output = string.lower()
print("string.lower():", output)

output = string.split(" ")
print("string.split():", output)
print()

list_a = [1,2,3,4]

list_a.append(1)
print("list_a.append(1)", list_a)

list_a.remove(2)
print("list_a.remove(2)", list_a)

list_a.pop()
print("list_a.pop()", list_a)
print()

test = (
        "이렇게 입력해도"
        "하나의 문자열로 연결되어"
        "생성된답니다."
)

print("test:", test)
print("type(test):", type(test))
print()

test = (
        "이렇게 입력해도",
        "하나의 문자열로 연결되어",
        "생성된답니다."
)

print("test:", test)
print("type(test):", type(test))
print()

print("::".join(["1","2","3","4","5"]))
print()

number = int(input("정수 입력> "))

if number % 2 == 0:
        print("\n".join(["입력한 문자열은 {}입니다.".format(number), "{}는 짝수입니다.".format(number)]))
              
else:
        print("\n".join(["입력한 문자열은 {}입니다.".format(number), "{}는 홀수입니다.".format(number)]))
              
