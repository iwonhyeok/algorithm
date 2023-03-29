#컴퓨터공학과, 20234007, 이원혁
print("컴퓨터공학과, 20234007, 이원혁")

import random

all_students = list(range(1, 31))
submitted = random.sample(all_students, 28)
not_submitted = list(set(all_students) - set(submitted))

print("제출하지 않은 학생의 출석번호는 다음과 같습니다:", not_submitted)