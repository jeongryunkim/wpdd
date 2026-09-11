class recommendation:
    def __init__(self):
        self.user_id= 'admin'
        self.user_pw= '1234'
        self.r=['ohio5','kda05','kiwoom5','cheesecake96']
    
    def code(self):
        while True:
            p = input('추천인 코드를 입력해주세요>>> ')
    
            if p in self.r:
                print('크레딧 500이 지급되었습니다.')
                break  
            else:
                print('코드를 정확히 입력해주세요.')

    def login(self):
        correct_id = "admin"
        correct_pw = "1234"

        while True:
            user_id = input("ID를 입력하세요: ")
            user_pw = input("PASSWORD를 입력하세요: ")

            if user_id == correct_id and user_pw == correct_pw:
                print("로그인 되었습니다.")
                self.code()  
                break   
            else:
                print("ID 또는 PASSWORD가 일치하지 않습니다.")


system = recommendation()
system.login()
    