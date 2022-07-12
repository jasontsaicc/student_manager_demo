# 定義類
class A:
    a = 0
    def __init__(self, name):
        self.b = 1
        self.c = 2
        self.name = name
# 創建對象
aa = A("jason")
# 調用__dict__
print(A.__dict__)
print(aa.__dict__)