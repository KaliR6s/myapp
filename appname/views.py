from django.shortcuts import render
from django.shortcuts import redirect
from .forms import PostForm
import random
from bs4 import BeautifulSoup
import urllib.request
import re

youtube_list_selectOne = ['https://www.youtube.com/watch?v=2-Am8llw87c&t=64s',
'https://www.youtube.com/watch?v=rVAsOQ4vrzk&t=168s',
'https://www.youtube.com/watch?v=JEOrxkcLo9k',
'https://www.youtube.com/watch?v=oit30URrODE'] #運勢悪い人向け
youtube_list_selectTwo = ['https://www.youtube.com/watch?v=0P6klz6BTek&index=20&list=PLIoouZjvzMWmz9y4G1n4MQ697zgEElW1x',
'https://www.youtube.com/watch?v=Vq4c9TpS1Cw&t=4s',
'https://www.youtube.com/watch?v=rVAsOQ4vrzk&t=168s',
'https://www.youtube.com/watch?v=L-UGLgRUtOs',
'https://www.youtube.com/watch?v=s_2a4mMR9BU'] #いい人向け

bgColorNum = {0:'white',1:'lightsteelblue',2:'lightyellow',3:'gainsboro',4:'pink',5:'lightgreen',6:'orange'}
bgColorList = {'white':'#ffffff','lightsteelblue':'#b0c4de','lightyellow':'#ffffe0','gainsboro':'#dcdcdc','pink':'#ffc0cb','lightgreen':'#90ee90','orange':'#FF8856'}
fortuneList = ['☆☆☆☆☆☆☆☆☆☆','★☆☆☆☆☆☆☆☆☆','★★☆☆☆☆☆☆☆☆','★★★☆☆☆☆☆☆☆','★★★★☆☆☆☆☆☆','★★★★★☆☆☆☆☆','★★★★★★☆☆☆☆','★★★★★★★☆☆☆','★★★★★★★★☆☆','★★★★★★★★★☆','★★★★★★★★★★']
zdNameDic = {'zodiac1':'おひつじ座','zodiac2':'おうし座','zodiac3':'ふたご座','zodiac4':'かに座','zodiac5':'しし座','zodiac6':'おとめ座',
'zodiac7':'てんびん座','zodiac8':'さそり座','zodiac9':'いて座','zodiac10':'やぎ座','zodiac11':'みずがめ座','zodiac12':'うお座'}

# Create your views here.
def appmain(request):
    youtubeUrl = random.choice(youtube_list_selectOne)
    zd = a = tdColor = character = luckyNum = zdName = ''
    t3='https://www.youtube.com/'
    bgColor = bgColorList[bgColorNum[0]]
    totalNum = 0
    if request.method == "GET":
        form = PostForm(request.GET)
        if form.is_valid():
            zd = form.cleaned_data["zodiac"]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]
        if zd == '':
            zdTotal = zdLove = zdMoney = zdWork = ''
        elif zd == 'zodiac1':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/aries_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/aries'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/ohitsuji/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]


        elif zd == 'zodiac2':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/taurus_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/taurus'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/oushi/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac3':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/gemini_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/gemini'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/hutago/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac4':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/cancer_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/cancer'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/kani/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac5':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/leo_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/leo'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/shishi/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac6':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/virgo_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/virgo'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/otome/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac7':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/libra_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/libra'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/tenbin/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac8':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/scorpio_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/scorpio'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/sasori/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac9':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/sagittarius_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/sagittarius'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/ite/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac10':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/capricorn_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/capricorn'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/yagi/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac11':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/aquarius_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/aquarius'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/mizugame/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]

        elif zd == 'zodiac12':
            character = 'https://www.vogue.co.jp/assets/commons/img/horoscope/daily/pisces_banner.jpg'
            zdName = zdNameDic[zd]
            url1 = 'https://fortune.yahoo.co.jp/12astro/pisces'
            req1 = urllib.request.Request(url1)
            response1 = urllib.request.urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1, "lxml")
            images = soup1.find_all('img')
            for img in images:
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_tot'):
                    zdTotalNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdTotal = fortuneList[int(zdTotalNum)]

                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_lov'):
                    zdLoveNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdLove = fortuneList[int(zdLoveNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_mny'):
                    zdMoneyNum = int(re.search(r'\d+',img['src']).group()) / 10
                    zdMoney =  fortuneList[int(zdMoneyNum)]
                if img['src'].startswith('https://s.yimg.jp/images/fortune/images/common/yftn_param_wrk'):
                    zdWorkNum =  int(re.search(r'\d+',img['src']).group()) / 10
                    zdWork = fortuneList[int(zdWorkNum)]

            url2 = 'https://uranai.nifty.com/f12seiza/uo/'
            req2 = urllib.request.Request(url2)
            response2 = urllib.request.urlopen(req2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "lxml")
            a = str(soup2.div(class_='hako'))     #今日の得点を取得
            totalNum = int(re.search(r'\d+',a).group())    #得点を抽出
            bgColor = bgColorList[bgColorNum[totalNum%6]]
            tdColor = bgColorNum[totalNum%6]
            luckyNum = totalNum%9 + 1
            if totalNum <50:
                youtubeUrl = youtube_list_selectOne[(luckyNum+123) % len(youtube_list_selectOne)]
            else:
                youtubeUrl = youtube_list_selectTwo[(luckyNum+123)%len(youtube_list_selectTwo)]
            t = youtubeUrl.split('watch?v=')
            t1 = t[0]+'embed/'
            t2 = t[1].split('&')
            t3 = t1+t2[0]
            
        return render(request, 'demo/appname.html', {'url': t3 , 'zdTotal':zdTotal,'zdLove':zdLove,'zdMoney':zdMoney,'zdWork':zdWork,'bgColor':bgColor,
        'tdColor':tdColor,'character':character,'luckyNum':luckyNum,'zdName':zdName})
