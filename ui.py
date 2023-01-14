import base64
import ctypes
import sys
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os
from icon import img



def ui():
    #使用程序自身的dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
    
    root=Tk()
    root.tk.call('tk', 'scaling', ScaleFactor/68)
    root.title("加密工具")
    root.geometry('960x540')
    tmp = open("tmp.ico","wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    root.iconbitmap("tmp.ico")
    os.remove("tmp.ico")

    select_path = StringVar()
    def select_file():
        selected_file_path = filedialog.askopenfilename(initialdir=sys.path[0])
        select_path.set(selected_file_path)

    lab = Label(root, text="选择文件：")
    lab.place(relx=0.1, rely=0.3)
    tex = Entry(root, textvariable = select_path)
    tex.place(relx=0.2,rely=0.3, relwidth=0.5)
    sel = Button(root, text="选择文件", command=select_file)
    sel.place(relx=0.81,rely=0.3,relwidth=0.16)

    def de():
        path = str(tex.get())
        try:
            os.system(sys.path[0] + '/tool/ali d "' + path + '"')
        except:
            return

    dec = Button(root, text="解密", command=de)
    dec.place(relx = 0.4, rely = 0.5, relwidth= 0.2)

    root.mainloop()

ui()
