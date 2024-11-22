# 사용자로부터 이름을 입력받고, 인사하는 프로그램

def greet_user():
    name = input("이름을 입력하세요: ")  # 사용자로부터 이름을 입력받음
    print(f"안녕하세요, {name}님! 반갑습니다.")  # 입력받은 이름을 포함해 인사 출력

if __name__ == "__main__":
    greet_user()  # 함수 실행
