
####新增版本



"""
第一題
輸入美金轉換成台幣

"""
"""
import tkinter as tk              #匯入函式庫
def event1():
    global label1Str1
    global entry1String

    str1=entry1String.get()       #取得entry1的文字
    #方法一
    if str1.isdigit()==False:     #如果str1不是數字
        str1=0.0                  #則str1=0.0等於這個結果
    TWD = float(str1) * 29.876
    ##方法二
    # try:                          #嘗試處理
    #     TWD = float(str1)*29.876
    # except:
    #     TWD = 0.0                 #若處理失敗,則產生0.0
    TWD =round(TWD,2)             #處理位數到小數點第二位並四捨五入
    strTWD=str(TWD)
    label1Str1.set(strTWD)          #設定label1的文字

win=tk.Tk()                       #初始化


#輸入框Entry
entry1String=tk.StringVar()
entry1=tk.Entry(win,textvariable=entry1String)              #新增輸入框Entry
entry1.place(x=0,y=0)
entry1String.set("請輸入美金")

#按鈕Button
btn1=tk.Button(win,text="轉換",command=event1)
btn1.place(x=0,y=30)

#標籤Label
label1Str1=tk.StringVar()
label1=tk.Label(win,text="twd",textvariable=label1Str1)
label1Str1.set("twd")
label1.place(x=0,y=60)
win.mainloop()
"""
"""
第二題
計算出營業稅
"""

#解題邏輯:先把所有功能按鈕設定好,再一一賦予功能
import tkinter as tk              #匯入函式庫
def event1():
    global label1Str1,label2Str1,label3Str1,label4Str1,label5Str1,label6Str1,label7Str1,label8Str1
    global entry1String,entry2String,entry3String

    str2=entry2String.get()                       #取得entry2的文字
    str3 = entry3String.get()                     #取得entry3的文字
    strAll=int(str2)*int(str3)                    #計算金額
    label4Str1.set("金額:"+str(strAll))
    label5Str1.set("銷售額:"+str(strAll))
    strTax=strAll*0.05                            #計算營業稅
    strTax=round(strTax,0)                        #稅金取四捨五入
    label6Str1.set("營業稅:"+str(strTax))
    strTotal= int(strAll+ strTax)                 #計算總金額
    label7Str1.set("合計:"+str(strTotal))

    #將數字轉成中文
    list1 = ["元", "拾", "佰", "仟", "萬", "拾", "佰", "仟", "億"]
    list2 = ["零", "壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖"]
    strChinese = ""
    digit = 0
    while True:
        n1 = strTotal % 10  # 處理位數
        strTotal = strTotal // 10
        strChinese = list1[digit] + strChinese  # 數字轉國字
        strChinese = list2[n1] + strChinese

        if strTotal <= 0:
            break
        digit = digit + 1
    label8Str1.set("中文:"+str(strChinese))




win=tk.Tk()                       #初始化

#輸入框Entry
entry1String=tk.StringVar()
entry1=tk.Entry(win,width=10,textvariable=entry1String)              #新增輸入框Entry
entry1.place(x=0,y=35)
entry1String.set("")
entry2String=tk.StringVar()
entry2=tk.Entry(win,width=10,textvariable=entry2String)              #新增輸入框Entry
entry2.place(x=80,y=35)
entry2String.set("")
entry3String=tk.StringVar()
entry3=tk.Entry(win,width=10,textvariable=entry3String)              #新增輸入框Entry
entry3.place(x=160,y=35)
entry3String.set("")


#按鈕Button
btn1=tk.Button(win,text="計算",command=event1)
btn1.place(x=0,y=70)

#標題Label
label1Str1=tk.StringVar()
label1=tk.Label(win,text="品項",textvariable=label1Str1)
label1Str1.set("品項")
label1.place(x=0,y=10)
label2Str1=tk.StringVar()
label2=tk.Label(win,text="數量",textvariable=label2Str1)
label2Str1.set("數量")
label2.place(x=80,y=10)
label3Str1=tk.StringVar()
label3=tk.Label(win,text="單價",textvariable=label3Str1)
label3Str1.set("單價")
label3.place(x=160,y=10)


#計算後Label
label4Str1=tk.StringVar()
label4=tk.Label(win,text="金額:",textvariable=label4Str1)
label4Str1.set("金額:")
label4.place(x=0,y=100)
label5Str1=tk.StringVar()
label5=tk.Label(win,text="銷售額:",textvariable=label5Str1)
label5Str1.set("銷售額:")
label5.place(x=0,y=120)
label6Str1=tk.StringVar()
label6=tk.Label(win,text="營業稅:",textvariable=label6Str1)
label6Str1.set("營業稅:")
label6.place(x=0,y=140)
label7Str1=tk.StringVar()
label7=tk.Label(win,text="合計:",textvariable=label7Str1)
label7Str1.set("合計:")
label7.place(x=0,y=160)
label8Str1=tk.StringVar()
label8=tk.Label(win,text="中文:",textvariable=label8Str1)
label8Str1.set("中文:")
label8.place(x=0,y=180)

win.mainloop()

"""
第三題
計算機做加減(未完成)
"""
"""

# 第三題： 計算機

import tkinter as tk # 匯入tkinter 函式庫

def event1():
    math(1)
def event2():
    math(2)
def event3():
    math(3)
def event4():
    math(4)
def event5():
    math(5)
def event6():
    math(6)
def event7():
    math(7)
def event8():
    math(8)
def event9():
    math(9)
def event0():
    math(0)

def math(num1):
    global label1Str1
    str1=label1Str1.get()
    str1=str1+str(num1)
    label1Str1.set(str1) # 設定 label1 的文字


subNumber =0
lastNumber=0
def eventAdd():
    global label1Str1
    global lastNumber
    str1=label1Str1.get()
    lastNumber=int(str1)
    label1Str1.set("")

def eventSub():
    global subNumber
    global lastNumber
    global label1Str1
    str1=label1Str1.get()
    lastNumber = int(str1)
    subNumber = -1
    label1Str1.set("")


def eventAns():
    global subNumber
    global lastNumber
    global label1Str1
    str1=label1Str1.get()
    if subNumber<0:
        subNumber = -int(str1)
        subNumber = subNumber +lastNumber
        label1Str1.set(str(subNumber))
        lastNumber = 0
        subNumber =0
    else:
        int1=int(str1)
        int1=int1+lastNumber
        label1Str1.set(str(int1))
        lastNumber=0

def eventAc():
    global label1Str1
    global lastNumber
    global subNumber
    label1Str1.set("")
    lastNumber = 0
    subNumber = 0


win = tk.Tk() # 建立GUI 應用程式的主視窗




# 標籤Label
label1Str1 = tk.StringVar() # 建立StringVar 變數
label1 =tk.Label(win,text="用戶輸入的資料", textvariable=label1Str1) # 建立Label物件, 綁定這個變數
label1Str1.set("")
label1.place(x=0, y=0)


# 按鈕Button
btn1 =tk.Button(win,text="1",command=event1) # 建立Button物件 按下後會出叫event1函式
btn1.place(x=0, y=90)# 按鈕Button
btn2 =tk.Button(win,text="2",command=event2) # 建立Button物件 按下後會出叫event1函式
btn2.place(x=30, y=90)# 按鈕Button
btn3 =tk.Button(win,text="3",command=event3) # 建立Button物件 按下後會出叫event1函式
btn3.place(x=60, y=90)

btnAdd =tk.Button(win,text="+",command=eventAdd) # 建立Button物件 按下後會出叫event1函式
btnAdd.place(x=90, y=60)

btn4 =tk.Button(win,text="4",command=event4) # 建立Button物件 按下後會出叫event1函式
btn4.place(x=0, y=60)
btn5 =tk.Button(win,text="5",command=event5) # 建立Button物件 按下後會出叫event1函式
btn5.place(x=30, y=60)
btn6 =tk.Button(win,text="6",command=event6) # 建立Button物件 按下後會出叫event1函式
btn6.place(x=60, y=60)
btn7 =tk.Button(win,text="7",command=event7) # 建立Button物件 按下後會出叫event1函式
btn7.place(x=0, y=30)
btn8 =tk.Button(win,text="8",command=event8) # 建立Button物件 按下後會出叫event1函式
btn8.place(x=30, y=30)
btn9 =tk.Button(win,text="9",command=event9) # 建立Button物件 按下後會出叫event1函式
btn9.place(x=60, y=30)
btnAns =tk.Button(win,text="=",command=eventAns) # 建立Button物件 按下後會出叫event1函式
btnAns.place(x=90, y=120)
btn10 =tk.Button(win,text="0",command=event0) # 建立Button物件 按下後會出叫event1函式
btn10.place(x=90, y=30)
btn11 =tk.Button(win,text="-",command=eventSub) # 建立Button物件 按下後會出叫event1函式
btn11.place(x=90, y=90)

btn11 =tk.Button(win,text="AC",command=eventAc) # 建立Button物件 按下後會出叫event1函式
btn11.place(x=0, y=120)

win.mainloop() # 最後步驟：程式做無限循環
"""
