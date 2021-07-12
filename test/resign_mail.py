import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def closeWindow():
    messagebox.showinfo(title="不同意关不掉", message="关不掉吧，呵呵")
    return


def agree():
    win = tk.Toplevel(window)
    win.geometry("500x150+{}+{}".
                 format(int((screenwidth - width) / 2),
                        int((screenheight - height) / 2)))
    win.title("辞职")
    label = tk.Label(win, text="您耗子尾汁", font=("华文行楷", 20))
    label.pack()
    btn = tk.Button(win, text="滚出去", width=6, height=1, command=window.destroy)
    btn.pack()


def disagree():
    B2.place_forget()
    B2.place(x=random.randint(100, 500), y=random.randint(100, 500))


if __name__ == '__main__':
    window = tk.Tk()
    window.title('辞职信')
    width = 600
    height = 650
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width,
                                height, (screenwidth - width) / 2,
                                (screenheight - height) / 2)
    window.geometry(alignstr)
    # 设置窗口是否可变长、宽
    window.resizable(width=False, height=True)
    window.geometry('600x600')
    window.protocol("WM_DELETE_WINDOW", closeWindow)
    load = Image.open('resign.jpeg').resize((300, 310))
    render = ImageTk.PhotoImage(load)
    L2 = tk.Label(window, image=render)
    L2.place(x=150, y=100)
    B1 = tk.Button(window, text='同意', command=agree)
    B1.place(x=155, y=420)
    B2 = tk.Button(window, text='不同意', command=disagree)
    B2.place(x=400, y=420)
    window.mainloop()
