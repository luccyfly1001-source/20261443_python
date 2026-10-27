from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("프로그래밍 언어 선택")
window.geometry("300x260")
window.resizable(width=False, height=False)

python_var = IntVar()
cpp_var = IntVar()
js_var = IntVar()

def show_selection():
    selected = []
    
    if python_var.get() == 1:
        selected.append("파이썬")
    if cpp_var.get() == 1:
        selected.append("C++")
    if js_var.get() == 1:
        selected.append("JavaScript")
    
    if selected:
        msg = ", ".join(selected) + " 선택되었습니다."
        messagebox.showinfo("선택 결과", msg)
    else:
        messagebox.showwarning("경고", "선택된 언어가 없습니다.")

cb_python = Checkbutton(window, text="파이썬", variable=python_var, font=("맑은 고딕", 11))
cb_cpp = Checkbutton(window, text="C++", variable=cpp_var, font=("맑은 고딕", 11))
cb_js = Checkbutton(window, text="JavaScript", variable=js_var, font=("맑은 고딕", 11))

cb_python.pack(anchor=W, padx=50, pady=10)
cb_cpp.pack(anchor=W, padx=50, pady=10)
cb_js.pack(anchor=W, padx=50, pady=10)

btn_submit = Button(window, text="선택 완료", command=show_selection, font=("맑은 고딕", 10), width=15)
btn_submit.pack(pady=10)

window.mainloop()