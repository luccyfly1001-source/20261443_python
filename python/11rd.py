from tkinter import *
from PIL import Image, ImageTk, ImageOps

## 전역 변수 선언 부분 ##
btnList = [None] * 4
fnameList = ["1.gif", "2.gif", "3.gif", "4.gif"]
photoList = [None] * 4
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.title("GIF 이미지 불러오기")
window.geometry("140x140")

# 1. GIF 이미지 경로 설정(확장자가 .jpg 또는 .jpeg인지 확인하세요)
image_path =r"C:\Users\Admin\Documents\20261443_JS_python\python\image.gif"

# 2. GIF 이미지 열기
img = Image. open(image_path)
img_resized = ImageOps.contain(img, (140, 140))
tk_img = ImageTk.PhotoImage(img_resized)
label = Label(window, image=tk_img)
label.image = tk_img  # 이미지 깜빡임/ 사라짐 방지용 참조 유지

window.mainloop()

label.image
for i in range(0, 4) :
    photoList[i] = PhotoImage(file = "image/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0, 2) :
    for k in range(0, 2) :
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()

