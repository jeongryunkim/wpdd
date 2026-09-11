from login import Recommendation
from roulette import RouletteEvent
from quiz import EventQuiz
from credit_view import Credit_view
from 홀짝야바위 import EvenOddGame


class Main:

    def __init__(self):
        self.user_data = [0, 0]  # [0]: 크레딧, [1]: 퀴즈 참여 여부
        self.auth = Recommendation()
        self.roulette = RouletteEvent()
        self.quiz = EventQuiz(self.user_data)
        self.credit_viewer = Credit_view()
        self.even_odd = EvenOddGame()

    def main_page(self):
        print("====================================")
        print(" 키움증권 이벤트 시스템에 오신 것을 환영합니다.")
        print("====================================")

        # 1. 로그인 진행
        if not self.auth.login():
            return

        # 2. 메인 메뉴 UI
        while True:
            print("\n------------------------------------")
            print("키움증권 이벤트 참여하고 크레딧 받자!")
            print("1. 추천인 입력하기")
            print("2. 룰렛 게임하기")
            print("3. 퀴즈 참여하기")
            print("4. 홀짝 야바위 게임하기")
            print("5. 내 크레딧 조회하기")
            print("0. 종료")
            print("------------------------------------")

            choice = input("원하시는 메뉴 번호를 선택하세요: ")

            if choice == "1":
                earned = self.auth.input_code()
                if earned:
                    self.user_data[0] += earned

            elif choice == "2":
                earned = self.roulette.start()
                self.user_data[0] += earned

            elif choice == "3":
                self.user_data[0] = self.quiz.event_quiz()

            elif choice == "4":
                # 메뉴 선택 즉시 홀짝 게임 실행
                initial_credit = self.even_odd.credit
                self.even_odd.play_game()
                earned = self.even_odd.credit - initial_credit
                self.user_data[0] += earned

            elif choice == "5":
                self.credit_viewer.current_credit(self.user_data[0])

            elif choice == "0":
                print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
                break

            else:
                print("\n잘못 선택하셨습니다. 메뉴 번호를 다시 입력해 주세요.")