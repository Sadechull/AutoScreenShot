#import cap_time.py 
from tkinter import *   #引用Tk模块
from tkinter.filedialog import askdirectory
import datetime
import numpy as np 
from PIL import ImageGrab


# def selectPath():
# 	path_ = askdirectory()
# 	path.set(path_)

def gui_process():
	root = Tk()             #初始化Tk()
	root.title('自动截图')
	root.geometry("700x300+500+500")

	def selectPath():
		path_ = askdirectory()
		path.set(path_)

	path = StringVar()
	#path.set("/Users/sadechull/Documents/Job/Programming/Auto_Screencut/picload")
	#path = "/Users/sadechull/Documents/Job/Programming/Auto_Screencut/picload"

	#标签
	L_starttime = Label(root,text='开始时间',width=15)
	L_starttime.grid(row=0)
	L_starttime.config(font='Times -15 bold',fg='blue')

	L_starttime_month = Label(root,text='月')
	L_starttime_month.grid(row=0,column=2)
	L_starttime_day = Label(root,text='日')
	L_starttime_day.grid(row=0,column=4)
	L_starttime_hour = Label(root,text='时')
	L_starttime_hour.grid(row=0,column=6)
	L_starttime_minute = Label(root,text='分')
	L_starttime_minute.grid(row=0,column=8)
	L_starttime_second = Label(root,text='秒')
	L_starttime_second.grid(row=0,column=10)

	L_endtime = Label(root,text='结束时间')
	L_endtime.grid(row=1)
	L_endtime.config(font='Times -15 bold',fg='blue')

	L_endtime_month = Label(root,text='月')
	L_endtime_month.grid(row=1,column=2)
	L_endtime_day = Label(root,text='日')
	L_endtime_day.grid(row=1,column=4)
	L_endtime_hour = Label(root,text='时')
	L_endtime_hour.grid(row=1,column=6)
	L_endtime_minute = Label(root,text='分')
	L_endtime_minute.grid(row=1,column=8)
	L_endtime_second = Label(root,text='秒')
	L_endtime_second.grid(row=1,column=10)

	L_timeinterval = Label(root,text='截图间隔时间')
	L_timeinterval.grid(row=2)
	L_timeinterval.config(font='Times -15 bold',fg='blue')
	L_timeinterval_minute = Label(root,text='分')
	L_timeinterval_minute.grid(row=2,column=2)
	L_timeinterval_second = Label(root,text='秒')
	L_timeinterval_second.grid(row=2,column=4)

	L_path_select = Label(root,text='保存路径')
	L_path_select.grid(row=3)
	L_path_select.config(font='Times -15 bold',fg='blue')

	#文本框
	E_starttime_month = Entry(root,width=5)
	E_starttime_month.grid(row=0, column=1)
	E_starttime_month.insert(5,"00")
	E_starttime_day = Entry(root,width=5)
	E_starttime_day.grid(row=0, column=3)
	E_starttime_day.insert(5,"00")
	E_starttime_hour = Entry(root,width=5)
	E_starttime_hour.grid(row=0, column=5)
	E_starttime_hour.insert(5,"00")
	E_starttime_minute = Entry(root,width=5)
	E_starttime_minute.grid(row=0, column=7)
	E_starttime_minute.insert(5,"00")
	E_starttime_second = Entry(root,width=5)
	E_starttime_second.grid(row=0, column=9)
	E_starttime_second.insert(5,"00")

	E_endtime_month = Entry(root,width=5)
	E_endtime_month.grid(row=1, column=1)
	E_endtime_month.insert(5,"00")
	E_endtime_day = Entry(root,width=5)
	E_endtime_day.grid(row=1, column=3)
	E_endtime_day.insert(5,"00")
	E_endtime_hour = Entry(root,width=5)
	E_endtime_hour.grid(row=1, column=5)
	E_endtime_hour.insert(5,"00")
	E_endtime_minute = Entry(root,width=5)
	E_endtime_minute.grid(row=1, column=7)
	E_endtime_minute.insert(5,"00")
	E_endtime_second = Entry(root,width=5)
	E_endtime_second.grid(row=1, column=9)
	E_endtime_second.insert(5,"00")

	E_timeinterval_minute = Entry(root,width=5)
	E_timeinterval_minute.grid(row=2, column=1)
	E_timeinterval_minute.insert(5,"0")
	E_timeinterval_second = Entry(root,width=5)
	E_timeinterval_second.grid(row=2, column=3)
	E_timeinterval_second.insert(5,"0")

	E_path_select = Entry(root, textvariable = path, width=20)
	E_path_select.grid(row=3,column=1,columnspan=3)	

	B_path_select = Button(root, text="选择...", command = selectPath, fg = "blue")
	B_path_select.grid(row=3,column=4)

	stop_t = False

	def init_timer():
		#disable_button()
		year = datetime.datetime.now().strftime('%Y')
		st = datetime.datetime(int(year),int(E_starttime_month.get()),int(E_starttime_day.get()),int(E_starttime_hour.get()),\
			int(E_starttime_minute.get()),int(E_starttime_second.get()))
		et = datetime.datetime(int(year),int(E_endtime_month.get()),int(E_endtime_day.get()),int(E_endtime_hour.get()),\
			int(E_endtime_minute.get()),int(E_endtime_second.get()))
		ti = datetime.timedelta(minutes=int(E_timeinterval_minute.get()),seconds=int(E_timeinterval_second.get()))
		sp = str(path.get())
		print(sp)
		timer(st,et,ti,sp,stop_t)

	# def disable_button():
	# 	B_start_cut.config(state='disabled',text='截图中')

	# def enable_button():
	# 	B_start_cut.config(state='normal',text='开始截图')

	# def stop_timer():
	# 	stop_t = True
	# 	enable_button()

	#按钮

	B_start_cut = Button(root, text="开始自动截图", command = init_timer, fg = "blue", height = 3, width =15, font='Times -18 bold')
	B_start_cut.grid(row=4,column=3,columnspan=3)

	# B_stop_cut = Button(root, text="停止自动截图", command = stop_timer, fg = "blue", height = 3, width =15, font='Times -18 bold')
	# B_stop_cut.grid(row=5,column=3,columnspan=3)

	#菜单栏
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)	
	filemenu.add_command(label="开始截图", command=init_timer)
	# filemenu.add_command(label="停止截图", command=stop_timer)
	menubar.add_cascade(label="控制", menu=filemenu)
	root.config(menu=menubar)

	mainloop()

def capture(savepath ='C:/Desktop/'):
	img = ImageGrab.grab()
	bmp = img.convert('RGB')
	img.save(savepath+'/'+str(datetime.datetime.now())+'.bmp','bmp')

def timer(starttime, endtime, timeinterval,savepath,stop_t):
	capturetime = starttime
	while datetime.datetime.now()<starttime:
		while not stop_t :
			if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') == capturetime.strftime('%Y-%m-%d %H:%M:%S'):
				capture(savepath)
				capturetime = capturetime + timeinterval
				if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') > endtime.strftime('%Y-%m-%d %H:%M:%S'):
					break

def init_timer(root):
	year = datetime.datetime.now().strftime('%Y')
	st = datetime.datetime(year,E_starttime_month.get(),E_startime_day.get(),E_starttime_hour.get(),\
		E_starttime_minute.get(),E_starttime_second.get())
	et = datetime.datetime(year,E_endtime_month.get(),E_endtime_day.get(),E_endtime_hour.get(),\
		E_endtime_minute.get(),E_endtime_second.get())
	ti = datetime.timedelta(minutes=E_timeinterval_minute.get(),seconds=E_timeinterval_second.get())
	sp = path

if __name__ == "__main__":
    gui_process()

# root1=Tk()
# root1.mainloop()