# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s='*'
#【我的】
#直角三角形，星星數目正確(可是太多)，位置不對
#run i=1~8
for i in range(1,8):
    print((s*i))

#直角三角形，星星數目正確，位置不對
#run i=1,(1+2),(3+2),(5+2)
for i in range(1,8,2):
    print((s*i))
    
#直角三角形，星星數目正確，位置正確
for i in range(1,8,2):
    print((s*i).center(7))

#【你的】
#非角三角形，星星數目錯誤，位置不對
#[錯誤原因]1,4,plot;8 stop;間格取錯，第三個參數請改成 2 
#run i=1,(1+4)
for i in range(1,8,4):
    print((s*i))

#三角形，星星數目錯誤，位置對
#[錯誤原因]
""" 純粹運氣號，位置夠寬，所以可以畫在中間。
    其實參數改成7，一樣畫的出來，且沒有邊界空白問題。 """

#[驗證範例]
""" for i in range(1,8,4):
        print((s*i).center(11,'+')) """

for i in range(1,8,4):
    print((s*i).center(11))

#【修正結論與建議】
""" 把你的迴圈間格修正，字串center()裡面的參數調好，答案就對了! """

s='*'

#【我的】
for i in range(1,8,2):
    if(i < (8-1)):
            print((s*i).center(7))
for i in reversed(range(1,8,2)):
    print((s*i).center(7))

#【你的】
for i in range(1,8,4):
    if(i < (4-1)):
            print((s*i).center(11)) 
for i in reversed(range(1,8,4)):
    print((s*i).center(11))

#【我的最後版本】
printL = 8
for i in range(1,printL,2):
    if(i < (printL-1)):
        print((s*i).center((printL-1)))
for i in reversed(range(1,8,2)):
    print((s*i).center(printL-1))
