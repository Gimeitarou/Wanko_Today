from autogui-101_Wankov import autogui_101
import requests
import webbrowser
import datetime
import ctypes

#Wanko_URL = 'https://www.fujitv.co.jp/meza/wanko/index.html'
#webbrowser.open(Wanko_URL)

Pic_num = int(input('上から何番目の写真を壁紙にしたいか、半角数字で教えてください。'))

dt = datetime.datetime.today()
year_20xx = str(dt.year - 2000)
month = str(dt.month)
day = str(dt.day)
weekday = dt.weekday()

if int(month) < 10:
    month,day += '0','0'

if weekday == 5: #saturday
    day -= 1
elif weekday == 6: #sunday
    day -= 2

daytime_info_needed = year_20xx + month + day #Ex:250502_=_2025年5月2日

Pic_URL = f'https://www.fujitv.co.jp/meza/wanko/photo/w{daytime_info_needed}_0{Pic_num}.jpg'
Pic_name = f'w{daytime_info_needed}_0{Pic_num}.jpg'

autogui_101(Pic_URL,Pic_name)

#references
#https://atmarkit.itmedia.co.jp/ait/articles/2111/02/news019.html
#https://qiita.com/sastrum/items/518579bc00dfae3cd293
#https://techplay.jp/column/1617