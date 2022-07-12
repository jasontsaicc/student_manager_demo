class Student():
    def __init__(self, name, gender, tel):
        # 姓名, 性別,手機
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f"{self.name}, {self.gender}, {self.tel}"


# aa = Student('aa', "nv", 111)
# print(aa)
