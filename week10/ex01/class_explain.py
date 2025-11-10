# 1. 클래스(Class) 정의: '자동차 설계도'
class Car:
    
    # 2. 초기화 메서드 (__init__): 객체가 생성될 때 호출됨
    # 'self'는 방금 생성된 객체 자신을 가리킵니다.
    def __init__(self, input_color, input_speed):
        print(f"--- __init__ 호출됨 ---")
        print(f"이 객체(self)의 메모리 주소: {id(self)}")
        
        # 3. 속성(Attribute) 설정: 'self'에 데이터를 저장합니다.
        self.color = input_color
        self.speed = input_speed
        print(f"객체 초기화 완료: 색상={self.color}, 속도={self.speed}")
        print("----------------------")

    # 4. 메서드(Method): 객체가 수행할 수 있는 동작
    def drive(self):
        print(f"{self.color}색 차가 {self.speed}km/h로 달립니다.")

# --- 코드 실행 ---

print("프로그램 시작: 첫 번째 차를 만듭니다.")

# 5. 객체 생성 (인스턴스화):
# (1) Car()가 호출되어 메모리에 객체가 생성됩니다.
# (2) __init__(생성된객체주소, "파란색", 60)이 자동으로 호출됩니다.
# (3) __init__이 완료되면, 객체의 주소(참조)가 'my_car1' 변수에 저장됩니다.
my_car1 = Car("파란색", 60)

print(f"\n'my_car1' 변수가 가리키는 주소: {id(my_car1)}")
print("'my_car1'은 Car 클래스의 '인스턴스'입니다.")


print("\n프로그램 시작: 두 번째 차를 만듭니다.")
my_car2 = Car("빨간색", 80)
print(f"\n'my_car2' 변수가 가리키는 주소: {id(my_car2)}")
print("'my_car2' 역시 Car 클래스의 '인스턴스'입니다.")

# 6. 인스턴스 사용:
print("\n--- 메서드 호출 ---")
my_car1.drive() # my_car1이 가리키는 객체의 drive() 메서드 호출
my_car2.drive() # my_car2가 가리키는 객체의 drive() 메서드 호출
