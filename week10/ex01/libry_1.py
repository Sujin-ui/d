class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.is_borrowed = False   
        # 처음엔 대출되지 않은 상태

    def borrow(self):
        if  self.borrow:
            print("대출가능합니다")
        else :
            print("배출중입니다")

