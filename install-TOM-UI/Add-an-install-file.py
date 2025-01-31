#这个程序是负责UI的
#OK Let's go
#这个程序是负责UI的
import tkinter as tk
#AI告诉我要添加这个库
root = tk.Tk()
#AI告诉我要这个代码来创建窗口
root.title("安装程序")
# AI告诉我要用这行代码设置窗口标题
root.geometry("400x300")
# AI告诉我要用这行代码设置窗口大小
root.resizable(False, False)
# AI告诉我这行代码可以锁定窗口大小
button = tk.Button(root, text="下一步", width=10, height=2,font=("华康翩翩体W5-A", 22))
button.pack(pady=20)
button.place(x=120, y=150)
#AI告诉我这行代码可以创建一个按钮
root.mainloop()
#AI告诉我这行代码可以运行主循环