import requests
import webbrowser
import datetime
import ctypes

Wanko_URL = 'https://www.fujitv.co.jp/meza/wanko/index.html'
webbrowser.open(Wanko_URL)

Pic_num = int(input('上から何番目の写真を壁紙にしたいか、半角数字で教えてください。'))

dt = datetime.datetime.today()
year_20xx = str(dt.year - 2000)
month = str(dt.month)
day = str(dt.day)

daytime_info_needed = year_20xx + month + day #Ex:250502_=_2025年5月4日

Pic_URL = f'https://www.fujitv.co.jp/meza/wanko/photo/w{daytime_info_needed}_0{Pic_num}jpg'

def Download_Setit(URL):
        requests.get(URL)
        Pic_path = f'Downloads/w{daytime_info_needed}_0{Pic_num}.jpg'
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Pic_path, 0)
        return 0

#references
#https://atmarkit.itmedia.co.jp/ait/articles/2111/02/news019.html
#https://qiita.com/sastrum/items/518579bc00dfae3cd293
#https://techplay.jp/column/1617