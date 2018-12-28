# -*- coding: utf-8 -*-
import tushare as ts
import matplotlib.pyplot as plt
from matplotlib.pylab import datestr2num
from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# 程序图形化窗体类
class GraphicInterface(Frame):
    month1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yearList = []
    monthList = []
    dayList = []
    
    # 构造函数
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.InitList()
        self.CreateWidgets()
    
    # 初始化年月日列表函数
    def InitList(self):
        # 计算允许查询的时间段（允许查询当年年份和上一年份的数据）
        today = datetime.today();   # 获取今天的时间
        self.yearList = [today.year-1, today.year]  # 初始化年列表
        for i in range(1,13):
            self.monthList.append(str(i))   # 初始化月列表
        for i in range(1,32):
            self.dayList.append(str(i)) # 初始化日列表
    
    # 判断是否是闰年
    def IsLeapYear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False
    
    # 判断各项输入是否合法
    def CheckDateValidity(self, y, m, d):
        if self.IsLeapYear(y):
            if d > self.month1[m-1]:
                messagebox.showinfo('Message', '您输入的日期有误！')
                return False
            else:
                return True
        else:
            if d > self.month2[m-1]:
                messagebox.showinfo('Message', '您输入的日期有误！')
                return False
            else:
                return True
        
    # 创建窗体的函数
    def CreateWidgets(self):
        self.nb = ttk.Notebook()    # 使用ttk中的Notebook作为窗体的模板
        self.master.title('股票数据分析程序V1.0')   # 窗体标题
        self.master.geometry('1050x560')    # 设置窗体的几何大小
        self.master.resizable(0,0)    #不允许对窗口大小进行调整
        self.master.iconbitmap('stock.ico') # 设置窗体的左上角的图标
        
        # “单股分析”选项卡
        self.page1 = ttk.Frame(self.nb)
        # “单股分析”页图片
        self.image1 = Label(self.page1, image=img)
        self.image1.grid(row=0, column=0, sticky=W, rowspan=10, columnspan=3, padx=10, pady=10)
        # 标题
        self.label1 = Label(self.page1, font=('黑体',15), text="单只股票历史数据查询")
        self.label1.grid(row=0, column=4, rowspan=2, columnspan=2, padx=5, pady=5)
        # 提示文本
        self.label1 = Label(self.page1, text="请输入要查询的股票代码：")
        self.label1.grid(row=2, column=4, padx=5, pady=5)
        # 输入股票代码的文本框
        self.txt1 = Text(self.page1, height=1, width=12)
        self.txt1.grid(row=2, column=5, padx=5, pady=5)
        # 提示文本
        self.label2 = Label(self.page1, text="查询的时间区间为：")
        self.label2.grid(row=3, column=4, padx=5, pady=5)
        # 提示文本
        self.label3 = Label(self.page1, justify='right', text="\t\t从")
        self.label3.grid(row=4, column=4, padx=5, pady=5)
        # 年份下拉框
        self.yearbox1 = ttk.Combobox(self.page1, width=10, values=self.yearList)
        self.yearbox1.grid(row=4, column=5, padx=5, pady=5)
        # 提示文本“年”
        self.label4 = Label(self.page1, text="年")
        self.label4.grid(row=4, column=6, padx=5, pady=5)
        # 月份下拉框
        self.monthbox1 = ttk.Combobox(self.page1, width=5, values=self.monthList)
        self.monthbox1.grid(row=4, column=7, padx=5, pady=5)
        # 提示文本“月”
        self.label5 = Label(self.page1, text="月")
        self.label5.grid(row=4, column=8, padx=5, pady=5)
        # 日期下拉框
        self.daybox1 = ttk.Combobox(self.page1, width=5, values=self.dayList)
        self.daybox1.grid(row=4, column=9, padx=5, pady=5)
        # 提示文本“日”
        self.label6 = Label(self.page1, text="日")
        self.label6.grid(row=4, column=10, padx=5, pady=5)
        # 提示文本
        self.label7 = Label(self.page1, justify='right', text="\t\t到")
        self.label7.grid(row=5, column=4, padx=5, pady=5)
        # 年份下拉框
        self.yearbox2 = ttk.Combobox(self.page1, width=10, values=self.yearList)
        self.yearbox2.grid(row=5, column=5, padx=5, pady=5)
        # 提示文本“年”
        self.label8 = Label(self.page1, text="年")
        self.label8.grid(row=5, column=6, padx=5, pady=5)
        # 月份下拉框
        self.monthbox2 = ttk.Combobox(self.page1, width=5, values=self.monthList)
        self.monthbox2.grid(row=5, column=7, padx=5, pady=5)
        # 提示文本“月”
        self.label9 = Label(self.page1, text="月")
        self.label9.grid(row=5, column=8, padx=5, pady=5)
        # 日期下拉框
        self.daybox2 = ttk.Combobox(self.page1, width=5, values=self.dayList)
        self.daybox2.grid(row=5, column=9, padx=5, pady=5)
        # 提示文本“日”
        self.label10 = Label(self.page1, text="日")
        self.label10.grid(row=5, column=10, padx=5, pady=5)
        # 提示文本
        self.label11 = Label(self.page1, text="请选择绘图选项：")
        self.label11.grid(row=6, column=4, padx=5, pady=5)
        # “开盘价”复选框
        self.openVar = IntVar()
        self.button1 = Checkbutton(self.page1, text="开盘价", variable=self.openVar)
        self.button1.select()
        self.button1.grid(row=6, column=5, padx=5, pady=5)
        # “最高价”复选框
        self.highVar = IntVar()
        self.button2 = Checkbutton(self.page1, text="最高价", variable=self.highVar)
        self.button2.grid(row=6, column=7, padx=5, pady=5)
        # “收盘价”复选框
        self.closeVar = IntVar()
        self.button3 = Checkbutton(self.page1, text="收盘价", variable=self.closeVar)
        self.button3.grid(row=6, column=9, padx=5, pady=5)
        # “最低价”复选框
        self.lowVar = IntVar()
        self.button4 = Checkbutton(self.page1, text="最低价", variable=self.lowVar)
        self.button4.grid(row=7, column=5, padx=5, pady=5)
        # “成交量”复选框
        self.volVar = IntVar()
        self.button5 = Checkbutton(self.page1, text="成交量", variable=self.volVar)
        #self.button5.grid(row=5, column=7, padx=5, pady=5)
        # 开始分析按钮
        self.alertButton1 = Button(self.page1, text='开始分析', command=self.CheckInput1)
        self.alertButton1.grid(row=8, column=5, columnspan=2, padx=5, pady=10)
        
        # “对比分析”选项卡
        self.page2 = ttk.Frame(self.nb)
        # “对比分析”页图片
        self.image2 = Label(self.page2, image=img)
        self.image2.grid(row=0, column=0, sticky=W, rowspan=10, columnspan=3, padx=10, pady=10)
        # 标题
        self.label12 = Label(self.page2, font=('黑体',15), text="股票对比分析（柱状图绘制）")
        self.label12.grid(row=1, column=4, rowspan=2, columnspan=2, padx=5, pady=5)
        # 提示文本
        self.label13 = Label(self.page2, text="请输入要对比的股票代码1：")
        self.label13.grid(row=4, column=4, padx=5, pady=5)
        # 输入股票代码的文本框
        self.txt2 = Text(self.page2, height=1, width=12)
        self.txt2.grid(row=4, column=5, padx=5, pady=5)
        # 提示文本
        self.label14 = Label(self.page2, text="请输入要对比的股票代码2：")
        self.label14.grid(row=5, column=4, padx=5, pady=5)
        # 输入股票代码的文本框
        self.txt3 = Text(self.page2, height=1, width=12)
        self.txt3.grid(row=5, column=5, padx=5, pady=5)
        # 开始分析按钮
        self.alertButton2 = Button(self.page2, text='开始分析', command=self.CheckInput2)
        self.alertButton2.grid(row=6, column=5, columnspan=2, padx=5, pady=10)
        
        # 将两个选项卡页面加入窗体
        self.nb.add(self.page1, text='单股分析')
        self.nb.add(self.page2, text='对比分析')
        self.nb.pack(expand=1, fill="both")
    
    # 检查输入的合法性
    def CheckInput1(self):
        stockCode = self.txt1.get(1.0, END)[:-1]
        y1 = self.yearbox1.get()
        m1 = self.monthbox1.get()
        d1 = self.daybox1.get()
        y2 = self.yearbox2.get()
        m2 = self.monthbox2.get()
        d2 = self.daybox2.get()
        var1 = self.openVar.get()
        var2 = self.highVar.get()
        var3 = self.closeVar.get()
        var4 = self.lowVar.get()
        var5 = self.volVar.get()
        if stockCode == "":
            messagebox.showinfo('Message', '您还未输入股票代码！')
        elif y1 == "" or m1 == "" or d1 == "" or y2 == "" or m2 == "" or d2 == "":
            messagebox.showinfo('Message', '您还未选择日期！')
        elif not var1 and not var2 and not var3 and not var4 and not var5:
            messagebox.showinfo('Message', '您还未选择绘制选项！')
        elif self.CheckDateValidity(int(y1), int(m1), int(d1)) and self.CheckDateValidity(int(y2), int(m2), int(d2)):
            startDate = y1 + '-' + m1.zfill(2) + '-' + d1.zfill(2)
            endDate = y2 + '-' + m2.zfill(2) + '-' + d2.zfill(2)
            try:
                data = ts.get_hist_data(stockCode, start=startDate, end=endDate, ktype='D')    # 用tushare获取数据
            except Exception as e:
                print(e)
                messagebox.showinfo('Message', '获取数据失败，请检查您的网络连接！\n错误原因：'+str(e))
            try:
                DrawLine(stockCode, data, var1, var2, var3, var4, var5) # 调用绘制折线图的函数
            except Exception as e:
                print(e)
                messagebox.showinfo('Message', '数据分析失败，请检查您是否安装相关库！\n错误原因：'+str(e))
    
    # 检查输入的合法性
    def CheckInput2(self):
        stockCode1 = self.txt2.get(1.0, END)[:-1]
        stockCode2 = self.txt3.get(1.0, END)[:-1]
        if stockCode1 == "" or stockCode2 == "":
            messagebox.showinfo('Message', '您还未输入股票代码！')
        else:
            try:
                data = ts.get_realtime_quotes([stockCode1, stockCode2])    # 用tushare获取数据
            except Exception as e:
                print(e)
                messagebox.showinfo('Message', '获取数据失败，请检查您的网络连接！\n错误原因：'+str(e))
            try:
                DrawBar(stockCode1, stockCode2, data)    # 调用绘制折线图的函数
            except Exception as e:
                print(e)
                messagebox.showinfo('Message', '数据分析失败，请检查您是否安装相关库！\n错误原因：'+str(e))
    
# 画折线图的函数
def DrawLine(code, data, openVar, highVar, closeVar, lowVar, volVar):
    # 使中文字符显示正常
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 使正负号显示正常
    plt.rcParams['axes.unicode_minus'] = False
    x = [datestr2num(i) for i in data.index]    # 将x轴转换为日期
    plt.style.use('ggplot') # 设置背景样式
    #plt.figure(figsize=(10,6))  # 设置图表格式
    plt.xlabel("日期")    # 设置X轴的文字
    plt.ylabel("指数")    # 设置Y轴的文字
    plt.title("股票 "+code+" 走势折线图")  # 设置图的标题
    # 根据传入的参数来确定要绘制的折线
    if openVar == True:
        plt.plot_date(x, data['open'], '-', label="开盘价")
    if highVar:
        plt.plot_date(x, data['high'], '-', label="最高价")
    if closeVar:
        plt.plot_date(x, data['close'], '-', label="收盘价")
    if lowVar:
        plt.plot_date(x, data['low'], '-', label="最低价")
    if volVar:
        plt.plot_date(x, data['volumn'], '-', label="成交量")
    plt.grid()  # 显示网格
    plt.legend()    # 显示图例
    plt.show()
    
# 画柱状图的函数
def DrawBar(code1, code2, data):
    # 使中文字符显示正常
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 使正负号显示正常
    plt.rcParams['axes.unicode_minus'] = False
    item = ['今日开盘价', '昨日收盘价', '当前价格', '今日最高价', '今日最低价', '竞买价', '竞卖价']
    x = list(range(len(item)))
    y1 = data.iloc[0, [1,2,3,4,5,6,7]]  # 选取第一支股票对应的数据
    y2 = data.iloc[1, [1,2,3,4,5,6,7]]  # 选取第二支股票对应的数据
    plt.xlabel("数据项目")    # 设置X轴的文字
    plt.ylabel("指数")    # 设置Y轴的文字
    plt.title("股票 "+code1+" 与股票 "+code2+" 数据对比图")  # 设置图的标题
    plt.bar(x, y1, width=0.4, label=code1)  # 绘制柱状图
    for i in range(len(x)): # 计算第二个柱状图的偏移量
        x[i] = x[i] + 0.4
    plt.bar(x, y2, width=0.4, label=code2, tick_label=item) # 绘制第二个柱状图
    plt.grid()  # 显示网格
    plt.legend()    # 显示图例
    plt.show()


# 打开窗口中要插入的图片文件
tmp = Tk()
img = PhotoImage(file='stock.png')
# 实例化窗体类
gui = GraphicInterface()
# 主消息循环:
gui.mainloop()