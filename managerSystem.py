from student import *


class StudentManager:
    def __init__(self):
        # 儲存學員數據  list
        self.student_list = []

    # 1.程式入口函數
    def run(self):
        # 1.加載文件裡的學員數據
        self.load_student()

        while True:
            # 2.顯示功能菜單
            self.show_menu()

            # 3.用戶輸入功能序號
            menu_num = int(input("請輸入需要的功能序號: "))

            # 4.根據用戶輸入的序號執行不同的功能 如果輸入1.執行添加
            if menu_num == 1:
                # 添加學員
                self.add_student()
            elif menu_num == 2:
                # 刪除學員
                self.del_student()
            elif menu_num == 3:
                # 修改學員信息
                self.modify_student()
            elif menu_num == 4:
                # 查詢學員信息
                self.search_student()
            elif menu_num == 5:
                # 顯示所有學員信息
                self.show_student()
            elif menu_num == 6:
                # 保存學員信息
                self.save_student()
            elif menu_num == 7:
                break

    # 2.系統功能函數
    # 2.1顯示功能菜單 - 打印序號的功能對應關係 -- 靜態方法 (不涉及對象或對象數據的取用)
    @staticmethod
    def show_menu():
        print("請選擇如下功能")
        print("1.添加學員")
        print("2.刪除學員")
        print("3.修改學員信息")
        print("4.查詢學員信息")
        print("5.顯示所有學員信息")
        print("6.保存學員信息")
        print("7.離開系統")

    # 2.2添加學員
    def add_student(self):
        # 1.用戶輸入姓名, 性別, 手機
        name = input("請輸入你的姓名: ")
        gender = input("請輸入你的性別: ")
        tel = input("請輸入你的手機號碼: ")

        # 2.創建學員對象 -- 類創建 在student文件裡 所以先導入
        student = Student(name, gender, tel)

        # 3.將對象添加到學員列表
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    # 2.3刪除學員
    def del_student(self):
        # 1. 用戶輸入目標學員姓名
        del_name = input("請輸入要刪除的學員姓名")
        # 2.遍歷學員列表，如果使用者輸入的學員存在則刪除學員物件，否則提示學員不存在
        for i in self.student_list:
            if del_name == i.name:
                # 刪除學員對象
                self.student_list.remove(i)
                break
            else:
                # 正常結束執行的代碼 目標不存在
                print("查無此人!!!")
            print(self.student_list)

    # 2.4修改學員信息
    def modify_student(self):
        # 1.用戶輸入目標學員姓名
        modify_name = input("請輸入要修改的學員姓名: ")
        # 2.遍歷列表資料，如果學員存在修改姓名性別手機號，否則提示學員不存在
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input("姓名: ")
                i.gender = input("性別: ")
                i.tel = input("手機號")
                print(f'修改學員信息成功, 姓名{i.name}, 性別{i.gender}, 手機{i.tel}')
                break
        else:
            print("查無此人")

    # 2.5查詢學員信息
    def search_student(self):
        print("查詢學員信息")
        search_name = input("請輸入要查詢的學員姓名: ")
        for i in self.student_list:
            if search_name == i.name:
                print(f"姓名{i.name}, 性別{i.gender}, 手機號{i.tel}")
                break
            else:
                print("查無此人!!!")

    # 2.6顯示所有學員信息
    def show_student(self):
        # 1.列印表頭
        print("姓名\t性別\t手機號")
        # 2.列印學員數據
        for i in self.student_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    # 2.7保存學員信息
    def save_student(self):
        # 1.打開文件
        f = open("student.data", "w")
        # 2.文件寫入數據
        # 2.1 [學員對象] 轉成dict
        new_list = [i.__dict__ for i in self.student_list]
        # 2.2 文件寫入 字符串數據
        f.write(str(new_list))
        # 3.關閉文件
        f.close()

    # 2.8 加載學員信息
    def load_student(self):
        # 1.打開文件 嘗試r開啟，如果有異常w
        try:
            f = open("student.data", "r")
        except:
            f = open("student.data", "w")
        else:
            # 2.讀取數據 檔案讀取出的資料是字元串還原列表類型；[{}] 轉換 [學員物件]
            data = f.read()  # str
            new_list = eval(data)
            self.student_list = [Student(i["name"], i["gender"], i["tel"]) for i in new_list]
        finally:
            # 3.關閉文件
            f.close
