from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("프로그래밍 언어 선택")
window.geometry("300x220")
window.resizable(width=False, height=False)

python_var = IntVar()
cpp_var = IntVar()
js_var = IntVar()

def python_click():
    if python_var.get() == 1:
        messagebox.showinfo("선택", "파이썬 선택되었습니다.")

def cpp_click():
    if cpp_var.get() == 1:
        messagebox.showinfo("선택", "C++ 선택되었습니다.")

def js_click():
    if js_var.get() == 1:
        messagebox.showinfo("선택", "JavaScript 선택되었습니다.")

cb_python = Checkbutton(window, text="파이썬", variable=python_var, command=python_click, font=("맑은 고딕", 11))
cb_cpp = Checkbutton(window, text="C++", variable=cpp_var, command=cpp_click, font=("맑은 고딕", 11))
cb_js = Checkbutton(window, text="JavaScript", variable=js_var, command=js_click, font=("맑은 고딕", 11))

cb_python.pack(anchor=W, padx=50, pady=15)
cb_cpp.pack(anchor=W, padx=50, pady=15)
cb_js.pack(anchor=W, padx=50, pady=15)

window.mainloop()