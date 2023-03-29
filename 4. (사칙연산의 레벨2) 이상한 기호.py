#컴퓨터공학과, 20234007, 이원혁
print("컴퓨터공학과, 20234007, 이원혁")

A = 0
B = 0
def formula(A,B):
    result = (A+B)*(A-B)
    return result

guess_A = input("A의 수를 입력하세요: ")
guess_B = input("B의 수를 입력하세요: ")

A = int(guess_A)
B = int(guess_B)

while not (0 < A <= 1000 and 0 < B <= 1000):
    print("ERROR! A와 B가 1000을 넘지 않게 작성해주세요.")
    guess_A = int(input("A의 수를 입력하세요: "))
    guess_B = int(input("B의 수를 입력하세요: "))

print(formula(A,B))