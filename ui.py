import base64
import ctypes
import sys
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os
import webbrowser
from icon import img



def ui():
    #使用程序自身的dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)

    cpath = os.getcwd().replace('\\','/')
    
    root=Tk()
    root.tk.call('tk', 'scaling', ScaleFactor/68)
    root.title("解密工具")
    root.geometry('520x280')
    tmp = open("tmp.ico","wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    root.iconbitmap("tmp.ico")
    os.remove("tmp.ico")

    select_path = StringVar()
    def select_file():
        selected_file_path = filedialog.askdirectory(initialdir=cpath)
        select_path.set(selected_file_path)

    cal = Label(root, text = "选择目录，点击按钮加密")
    cal.place(relx=0.5,rely=0.15,anchor="center")
    tex = Entry(root, textvariable = select_path)
    tex.place(relx=0.1,rely=0.3, relwidth=0.6)
    sel = Button(root, text="选择", command=select_file)
    sel.place(relx=0.7,rely=0.3,relwidth=0.2)
    btnlink = Label(root, text='光辉ACG-ghacg.com',foreground='blue')
    btnlink.place(relx=0.5, rely=0.94,anchor="center")
    def open_url(event):
        webbrowser.open("https://ghacg.com", new=0)
    btnlink.bind("<Button-1>", open_url)

    def de():
        path = str(tex.get())
        try:
            os.system(cpath + '/tool/ali d "' + path + '"')
        except:
            return

    def en():
        path = str(tex.get())
        try:
            os.system(cpath + '/tool/ali e ' + path)
        except:
            return

    dec = Button(root, text="解密", command=de)
    dec.place(relx = 0.2, rely = 0.65, relwidth= 0.2)
    enc = Button(root, text="加密", command=en)
    enc.place(relx = 0.6, rely = 0.65, relwidth= 0.2)

    root.mainloop()

ui()
