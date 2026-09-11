import random


class EvenOddGame:

    def __init__(self):
        self.credit = 0
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
            choice = input("두 수의 합은 무엇일까요? ('홀' 또는 '짝' 입력): ").strip()
            if choice in ["홀", "짝"]:
                return choice
            print("'홀' 또는 '짝' 중에서 정확히 입력해주십시오.")

    # 3. 홀짝 게임 진행 함수 (바로 실행)
    def play_game(self):
        print("\n==================================")
        print("홀짝 게임을 시작합니다.")

        computer_num = random.randint(1, 100)
        user_num = self.get_user_number()
        sigma = computer_num + user_num

        if sigma % 2 == 0:
            answer = "짝"
        else:
            answer = "홀"

        ans = self.get_user_choice()

        if answer == ans:
            result = "승리"
            self.credit += 50
        else:
            result = "패배"

        # 결과 출력
        print("\n[게임 결과]")
        print(f"컴퓨터의 숫자: {computer_num} / 내가 입력한 숫자: {user_num}")
        print(f"두 수의 합: {sigma} ({answer})")
        print(f"당신은 {result}하셨습니다!")
        print(f"획득/현재 야바위 크레딧 : {self.credit:,}")

        # 결과 저장
        record = f"{result},{self.credit}"
        self.history.append(record)

        with open("EO_history.txt", "a", encoding="utf-8") as file:
            file.write(record + "\n")

        return self.credit


if __name__ == "__main__":
    game = EvenOddGame()
    game.play_game()