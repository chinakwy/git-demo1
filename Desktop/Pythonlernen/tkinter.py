import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100') #大小


var = tk.StringVar() #tk里面的一个字符串的变量
l = tk.Label(window,textvariable = var,bg='red',font = ('Arial',12),
    width=15,height=2) 
#windouw 上面的一个Label,bg=backgroun ,font 字体
#textvariable = var,字符串变量，一开始他是空的

l.pack()
#放在左右上下，最后在上面中间位置
 
on_hit = False #全局变量 还要标出global on_hit
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('You hit me') #点击一下文本变量就出现 You hit me
    else:
        on_hit = False
        var.set('') #再点击一下文本就为空

b = tk.Button(window,text='hit me', width=15, height=2,command=hit_me)
# 这了设置了一个按钮。点击后执行的就是command里这个函数，前面定义好hit_me
b.pack()

window.mainloop() 
#while 循环.这样就出来出来一个窗口了。所有的窗口都有这样一个mainloop
