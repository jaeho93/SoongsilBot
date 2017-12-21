from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
from datetime import timedelta
import requests
import json

'''
week : 1 평일/ 2 토요일 / 3 휴일,일요일
inout: 1 상행 내선 / 2 하행 외선
'''
def first_last_subway(week, inout):
    try:
        my_url = 'http://openapi.seoul.go.kr:8088/key/xml/SearchFirstAndLastTrainbyFRCodeService/1/5/7/'+str(week)+'/'+str(inout)+'/738/'
        html = urlopen(my_url)
        source = html.read()
        html.close()
    except:
        return '지하철API 접속 오류!'

    soup = BeautifulSoup(source, 'lxml')
    first_time = str(soup.find('first_time'))[12:-13]
    first_from = str(soup.find_all('f_subwaysname'))[16:-17]
    first_to = str(soup.find_all('f_subwayename'))[16:-17]
    last_time = str(soup.find('last_time'))[11:-12]
    last_from = str(soup.find_all('l_subwaysname'))[16:-17]
    last_to = str(soup.find_all('l_subwayename'))[16:-17]

    first_last_str = '----첫차 시간----\n'\
                    +first_time + '\n'\
                    +'----기점/종점----\n'\
                    +first_from+'->'+first_to+'\n'\
                    +'----막차 시간----\n'\
                    +last_time + '\n'\
                    +'----기점/종점----\n'\
                    +last_from+'->'+last_to+'\n'

    return first_last_str

def arrival_subway(week, inout):
    try:
        my_url = 'http://openapi.seoul.go.kr:8088/key/xml/SearchArrivalInfoByFRCodeService/1/5/738/'+str(inout)+'/'+str(week)
        html = urlopen(my_url)
        source = html.read()
        html.close()
    except:
        return '지하철API 접속 오류!'

    soup = BeautifulSoup(source, 'lxml')
    arrive_time = soup.find_all('arrivetime')
    subway_name = soup.find_all('subwayname')

    arrival_str = '----도착 정보-----\n'
    for i in range(5):
        arrival_str += str(subway_name[i])[12:-13] + '행 ' +\
         str(arrive_time[i])[12:-13]+'\n'

    return arrival_str

def get(inout_str):
    if inout_str == '상행선(건대행)':
        inout = 1
    elif inout_str == '하행선(대림행)':
        inout = 2
    today = datetime.today()
    if today.weekday() in [6]:
        return arrival_subway(3,inout)+first_last_subway(3,inout)

    header={'TDCProjectkey':'key'}
    year=str(today.year)
    month=str(today.month).zfill(2)
    day=str(today.day).zfill(2)
    url='https://apis.sktelecom.com/v1/eventday/days?type=h&year={0}&month={1}&day={2}'.format(year,month,day)
    result=requests.get(url,headers=header).json()
    if result['count']>0:
        return arrival_subway(3,inout)+first_last_subway(3,inout)
    elif today.weekday() in [5]:
        return arrival_subway(2,inout)+first_last_subway(2,inout)
    else:
        return arrival_subway(1,inout)+first_last_subway(1,inout)
