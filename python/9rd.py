## 함수 선언 부분 ##
def plus(v1, v2) :
    result = 0
    result = v1 + v2
    return result

## 전역 변수 선언 부분 ##
hap = 0

## 메인 코드 부분 ##
hap = plus(100, 200)
print("100과 200의 plus() 함수 결과는 %d" % hap)

## 함수 선언 부분 ##
def para_func (*para) :
    result = 0
    for num in para:
        result = result + num

    return result 

## 전역 변수 선언 부분 ##
hap = 0

## 메인 코드 부분 ## 
hap = para_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d"% hap)

hap = para_func(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(hap)

