#class Car 정의함
class Car: 
    #생성자 메소드인  __init__를 생성
    #self는 자기 자신을 가르키는 객체에 해당함
    def __init__(self, brand, model, year): #나머지 brand, model, year는 외부에서 전달 받은 값
        self.brand = brand  #self.~~면 객체 내부에 저장
        self.model = model
        self.year = year
        self.speed = 0   #speed는 속도를 초기화 시킴

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} {self.model} 가속! 현재 속도: {self.speed} km/h")

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"{self.brand} {self.model} 감속! 현재 속도: {self.speed} km/h")

    def honk(self):
        print("빵빵! 🚙")

# 객체 생성
my_car = Car("Hyundai", "Sonata", 2022)

# 메서드 사용
my_car.accelerate(30)   # 속도 30 증가
my_car.brake(10)        # 속도 10 감소
my_car.honk()           # 경적 울림