import random


class EvenOddGame:

    def __init__(self):

        # 크레딧
        self.credit = 0

        # 게임 결과를 저장할 리스트
        self.history = []

    # 1. 숫자 입력받는 함수

    def get_user_number(self):

        while True:

            try:

                num = int(input("1~100 사이의 숫자를 입력하세요: "))

                if 1 <= num <= 100:

                    return num

                print("1에서 100 사이의 숫자를 입력해주십시오.")

            except ValueError:

                print("숫자로만 입력해주십시오.")

    # 2. 홀 / 짝 예측 입력받는 함수

    def get_user_choice(self):

        while True:

            choice = input(
                "두 수의 합은 무엇일까요? ('홀' 또는 '짝' 입력): "
            ).strip()

            if choice in ["홀", "짝"]:

                return choice

            print("'홀' 또는 '짝' 중에서 정확히 입력해주십시오.")

    # 3. 홀짝 게임 진행 함수

    def play_game(self):

        print("\n==================================")

        print("홀짝 게임을 시작합니다.")

        computer_num = random.randint(1, 100)

        user_num = self.get_user_number()

        sigma = computer_num + user_num

        q = sigma % 2

        if q == 0:

            answer = "짝"

        else:

            answer = "홀"

        ans = self.get_user_choice()

        if answer == ans:

            result = "승리"

            # 승리하면 크레딧 50 추가
            self.credit += 50

        else:

            result = "패배"

        # 결과 출력

        print("\n[게임 결과]")

        print(
            f"컴퓨터의 숫자: {computer_num} / "
            f"내가 입력한 숫자: {user_num}"
        )

        print(f"두 수의 합: {sigma} ({answer})")

        print(f"당신은 {result}하셨습니다!")

        print(f"현재 크레딧 : {self.credit:,}")

        # 결과 저장
        record = f"{result},{self.credit}"

        self.history.append(record)

        # txt 파일에 결과 바로 추가

        with open("EO_history.txt", "a", encoding="utf-8") as file:

            file.write(record + "\n")

    # 4. 게임 메뉴 실행 함수

    def start(self):

        print("\n==================================")

        print("홀짝 게임에 오신 것을 환영합니다!")

        # 게임 메뉴를 반복

        while True:

            try:

                print("\n==================================")

                print("현재 크레딧 :", self.credit)

                print()

                print("1번 : 홀짝 게임 시작")

                print("2번 : 게임 종료")

                menu = int(input("번호를 입력하세요: "))

                if menu == 1:

                    self.play_game()

                elif menu == 2:

                    print("\n홀짝 게임을 종료합니다.")

                    print(f"최종 크레딧 : {self.credit:,}")

                    break

                else:

                    print("1, 2번 중에서 선택해주세요.")

            except ValueError:

                print("숫자로 입력해주십시오.")


# ==========================================
# 실행하는 부분
# ==========================================

game = EvenOddGame()

game.start()