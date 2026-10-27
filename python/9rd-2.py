from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("윈도창 연습")
window.geometry("400x400")
window.resizable(width=False, height=False)

photo = PhotoImage(file="image/11.gif")

label1 = Label(window, image=photo) 
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부 중입니다.", bg="magenta", width=20, height=5, anchor=SE)

def myFunc():
    messagebox.showinfo("고양이 버튼", "고양이가 귀엽죠? ^^")
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요.") 

chk = IntVar()
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)
button1 = Button(window, image=photo, command=myFunc)

cb1.pack()
button1.pack()
label1.pack()
label2.pack()
label3.pack()

window.mainloop()