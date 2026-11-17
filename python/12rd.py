from tkinter import *
from tkinter.filedialog import askopenfilename


def fun_open():
    filepath = askopenfilename(
        title="gif 이미지 로드", filetypes=[("gif이미지", "*.gif")]
    )
    if not filepath:
        return

    tk_img = PhotoImage(file=filepath)
    image_label.config(image=tk_img)
    image_label.image = tk_img


window = Tk()
window.title("GIF 뷰어")

image_label = Label(window)
image_label.pack()

btn = Button(window, text="열기", command=fun_open)
btn.pack()

window.mainloop()