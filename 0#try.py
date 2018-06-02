import tkinter as tk

window = tk.Tk()
window.title('Simulation: omni_test')
window.geometry('800x600')

canvas = tk.Canvas(window,bg='yellow',height=450,width=500)
x0,y0,x1,y1=50,50,80,80
oval=canvas.create_oval(x0,y0,x1,y1,fill='blue')
canvas.place(x=150,y=40)

#Button,如何做到图片的Button？
active = False
def doStep():
	"""前行一小步"""
	canvas.move(oval,0,1)
def doRun():
	canvas.move(oval,0,1)
def doPause():
	active == False


button_img_next_green_gif = tk.PhotoImage(file = 'next_green.gif')#按钮图片载入
button_img_play_green_gif = tk.PhotoImage(file = 'play_green.gif') 
button_img_pause_green_gif = tk.PhotoImage(file = 'pause_green.gif')
button_img_video_gif = tk.PhotoImage(file = 'video.gif')
button_img_showhide_gif = tk.PhotoImage(file = 'showhide.gif')
button_img_prev_green_gif = tk.PhotoImage(file = 'prev_green.gif')
button_img_repeat_blue_gif = tk.PhotoImage(file = 'repeat_blue.gif')


button_doStepBack = tk.Button(window,image=button_img_prev_green_gif,command=doStep).place(x=10,y=40)#带图按钮
button_doStep = tk.Button(window,image=button_img_next_green_gif,command=doStep).place(x=10,y=10)#带图按钮
button_doRun = tk.Button(window,image=button_img_play_green_gif,command=doRun).place(x=40,y=10)
button_doPause = tk.Button(window,image=button_img_pause_green_gif).place(x=70,y=10)
button_showhide = tk.Button(window,image=button_img_showhide_gif).place(x=100,y=10)
button_Record = tk.Button(window,image=button_img_video_gif).place(x=130,y=10)
button_setReplay = tk.Button(window,image=button_img_repeat_blue_gif,command=doStep).place(x=40,y=40)#带图按钮



# b1 = tk.Button(window,text='Step forward',command=doStep).pack()#无图按钮
# b2 = tk.Button(window,text='Run Simulation',command=doRun).pack() 
# b3 = tk.Button(window,text='Pause Simulation',command=doPause).pack()
# b4 = tk.Button(window,text='Record').pack(side='left')


#读条
s = tk.Scale(window,label='try me',from_=5,to=10,orient=tk.HORIZONTAL,
	length=500,showvalue=1,tickinterval=5,resolution=0.01)
s.place(x=150,y=500)

#只是为了显示menubar中的操作
l = tk.Label(window,width=10,text='',bg='green')#直接加.pack(),只pack了等式后面部分
l.place(x=20,y=100) #必须进行这一步，否则l没有被pack上去，


#下面都是menubar
counter = 0
def do_job():
	global counter #定义为全局变量
	l.config(text='do'+str(counter)) #label config 改变label一个参数。字符串
	counter += 1
#该函数只是用来试一试


#下面都是menubar
menubar = tk.Menu(window) #创建了一个空的menubar，建立在window上的，所以master是window

filemenu = tk.Menu(menubar,tearoff=0)#创建filemenu，master是menurbar，tearoff是否虚线分开
menubar.add_cascade(label='File',menu=filemenu)#menubar上加了filemenu，以File命名
filemenu.add_command(label='New',command=do_job)#在filemenu上加
filemenu.add_command(label="Open",command=do_job)
filemenu.add_command(label="Save",command=do_job)
filemenu.add_separator() #加了一条分割线
filemenu.add_command(label="Exit",command=window.quit) 

editmenu = tk.Menu(menubar,tearoff=0)#editmenu是menubar上的一个menu
menubar.add_cascade(label='Edit',menu=editmenu)#把它显示在menubar上
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label="Copy",command=do_job)
editmenu.add_command(label="Paste",command=do_job)

simulatemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(labe='Simulation',menu=simulatemenu)
simulatemenu.add_command(label='Step back')
simulatemenu.add_command(label='Pause')
simulatemenu.add_command(label='Run')
simulatemenu.add_command(label='Step forward')
# simulatemenu.add_command(label='Select step size')
submenu=tk.Menu(simulatemenu)#在simulatemenu中建立submenu
simulatemenu.add_cascade(label='Select step size',menu=submenu,underline=0)
submenu.add_command(label="Automaic")
submenu.add_command(label="Fixed interbal(0.100s)..")
submenu.add_separator() #加了一条分割线
submenu.add_command(label="step from robot/plantform")
submenu.add_command(label="step from robot/sink")
submenu.add_command(label="step from robot/controller")
simulatemenu.add_separator() #加了一条分割线
simulatemenu.add_command(label="Recomputer from here")
simulatemenu.add_separator() #加了一条分割线
simulatemenu.add_command(label="Record Video..")
simulatemenu.add_command(label="Shou/Hide")

window.config(menu=menubar)#把所有menubar放在window上。config改变window的一个参数


window.mainloop()









