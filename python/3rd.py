import turtle ## 거북이 그래픽 라이브러리를 불러옵니다.
import random ## 랜덤 값 생성을 위한 라이브러리

## 함수 선언 부분 ##
def screenLeftClick(x,y) :
    tSize = random.ranrange(1,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))

    turtle.pendown()
    turtle.goto(x, y)

def ScreenMidClick(x,y) :
    global r, g, b
    tSize = random.raddrange(1,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
