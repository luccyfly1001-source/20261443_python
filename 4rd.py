print("100")
print("%d" % 100)
print("100 + 100")
print("%d" % (100 + 100))
print("%d %d" % (100, 200))
print("%d %d" % (100, 200))
print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)

print("%f" % 123.45)
print("%.1f" % 123.45)
print("%.3f" % 123.45)

print("%s" % "Python")
print("%10s" % "Python")
print("{2:d} {1:d} {0:d}".format(100, 200, 300))

print("한 행입니다. 또 한 행입니다.")
print("한 행입니다.\n또 한 행입니다.")
print("      *\n     ***\n    *****\n   *******\n  *********\n   *******\n    *****\n     ***\n      *")

a = 9
b = 2

result = a//b
print(a,'//',b,'=',result)
result = a**b
print(a,'**',b,'=',result)
result = a%b
print(a,'%',b,'=',result)

a += 3; print("a += 3 :", a)
a = 9 
a -= 3; print("a -= 3 ;", a)
a = 9
a *= 3; print("a *= 3 :", a)
a = 9
a /= 3; print("a /= 3:", a)

print(" a == b :", a == b)
print(" a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)

s1, s2, s3 = "100", "100.123", "999999999999999999999999999"
print(int(s1)+1,"\n", float(s2)+1, int(s3)+1)


money = c500 = c100 = c50= c10 = 0

money = int(input("교환할 돈은 얼마?"))

c500 = money // 500 
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %=50

c10 = money // 10
money %= 10

print("\n 500원짜리 => %d개"%c500)
print("\n 100원짜리 => %d개"%c100)
print("\n 50원짜리 => %d개"%c50)
print("\n 10원짜리 => %d개"%c10)
print("바꾸지 못한 잔돈 => %d원 \n"%money)



money2 = c10000 = c5000 = c1000 = 0

money2 = int(input("교환할 돈은 얼마?"))

c10000 = money2 // 10000
money2 %= 10000

c5000 = money2 // 5000
money2 %= 5000

c1000 = money2 // 1000
money2 %=1000

print("\n 10000원짜리 => %d개"%c10000)
print("\n 5000원짜리 => %d개"%c5000)
print("\n 1000원짜리 => %d개"%c1000)
print("바꾸지 못한 잔돈 => %d원 \n"%money2) 


a = 99

if a < 100 :
    print("100보다 작군요.")
    print("거짓이므로 이 문장은 안 보이겠죠?")

print("프로그램 끝")

a = int(input("정수를 입력하세요 : "))

if a % 2 == 0 :
    print("짝수를 입력했균요.")
else :
     print("홀수를 입력했군요.")

a = 75

if a > 50 :
    if a < 100 :
        print("50보다 크고 100보다 작군요.")
    else :
        print("와~~ 100보다 크군요.")
else :
    print("에고~50보다 작군요.")

score = int(input("점수를 입력하세요 : "))

if score >=90 :
    print("A")
else :
      if score >=80 :
          print("B")
      else :
           if score >=60 :
               print("D")
           else :
                  print("F")

print("학점입니다. ^^")



score = int(input("점수를 입력하세요 : "))

if score >=95 :
    print("A+")
else :
      if score >=90 :
          print("A0")
      else :
           if score >=85 :
               print("B+")
           else :
                if score >=80 :
                  print("B0")
                else :
                      if score >= 75 :
                           print("C+")
                      else :
                           if score >= 70 :
                                print("C0")
                           else :
                                if score >= 65 :
                                     print("D+")
                                else :
                                     if score >= 60 :
                                          print("D0")
                                     else :
                                          if score < 60 :
                                               print("F")

print("학점입니다. ^^")