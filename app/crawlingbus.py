from bs4 import BeautifulSoup
from urllib.request import urlopen

def get(stNm):
    if stNm == '정문 앞':
        num = 1
    elif stNm == '정문 건너편(올리브영 앞)':
        num = 2
    elif stNm == '정문 건너편':
        num = 3
    elif stNm == '중문 앞':
        num = 4
    elif stNm == '중문 건너편':
        num = 5
    elif stNm == '기숙사 앞':
        num = 6
    elif stNm == '기숙사 건너편':
        num = 7
        
    return arrival_bus(num)
 
def arrival_bus(num):
    try:
        if num == 1:
            html = urlopen('http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?ServiceKey=2ISgskYNUJKvIXsflwJL4PXaVlxKg9ykM7s3zxWSwivy7UJiocbKl9YYwaucREcnYXenFH6PD%2Bab0GeRGOpLgg%3D%3D&stId=119000073')
        elif num == 2:
            html = urlopen('http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?ServiceKey=2ISgskYNUJKvIXsflwJL4PXaVlxKg9ykM7s3zxWSwivy7UJiocbKl9YYwaucREcnYXenFH6PD%2Bab0GeRGOpLgg%3D%3D&stId=119000071')
        elif num == 3:
            html = urlopen('http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?ServiceKey=2ISgskYNUJKvIXsflwJL4PXaVlxKg9ykM7s3zxWSwivy7UJiocbKl9YYwaucREcnYXenFH6PD%2Bab0GeRGOpLgg%3D%3D&stId=119000072')
        elif num == 4:
            html = urlopen('http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?ServiceKey=2ISgskYNUJKvIXsflwJL4PXaVlxKg9ykM7s3zxWSwivy7UJiocbKl9YYwaucREcnYXenFH6PD%2Bab0GeRGOpLgg%3D%3D&stId=119000077')
        elif num == 5:
            html = urlopen('http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?ServiceKey=2ISgskYNUJKvIXsflwJL4PXaVlxKg9ykM7s3zxWSwivy7UJiocbKl9YYwaucREcnYXenFH6PD%2Bab0GeRGOpLgg%3D%3D&stId=119000076')
        elif num == 6:
            html = urlopen('http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?ServiceKey=2ISgskYNUJKvIXsflwJL4PXaVlxKg9ykM7s3zxWSwivy7UJiocbKl9YYwaucREcnYXenFH6PD%2Bab0GeRGOpLgg%3D%3D&stId=119000079')
        elif num == 7:
            html = urlopen('http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?ServiceKey=2ISgskYNUJKvIXsflwJL4PXaVlxKg9ykM7s3zxWSwivy7UJiocbKl9YYwaucREcnYXenFH6PD%2Bab0GeRGOpLgg%3D%3D&stId=119000078')

        source = html.read()

        html.close()
        
    except:
        return '일시적인 접속 오류입니다.\n잠시 후 다시 이용해 주세요.'

    soup = BeautifulSoup(source, "xml")

    tables1 = soup.find_all('itemList')

    st_tables2 = list()
        
    tables2 = [],[],[],[],[],[],[],[],[],[],[],[]

    st_tables3 = list()
        
    tables3 = [],[],[],[],[],[],[],[],[],[],[],[]

    busRouteId = list()

    st_busRouteNm = list()

    #st_busRouteNm = [],[],[],[],[],[],[],[],[],[],[],[]
    
    busRouteNm = [],[],[],[],[],[],[],[],[],[],[],[]
    
    stNm = str(tables1[0].find('stNm'))[6:-7]

    for i in range(len(tables1)):
        busRouteId.append(tables1[i].find_all('busRouteId'))

    
    
    for i in range(len(busRouteId)):
        html2 = urlopen('http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo?ServiceKey=2ISgskYNUJKvIXsflwJL4PXaVlxKg9ykM7s3zxWSwivy7UJiocbKl9YYwaucREcnYXenFH6PD%252Bab0GeRGOpLgg%253D%253D&busRouteId='+str(busRouteId[i]))
        source = html.read()
        html.close()
        soup = BeautifulSoup(source, "xml")
        st_busRouteNm.append(soup.find('busRouteNm'))

    print(st_busRouteNm)
    
    for i in range(len(st_busRouteNm)):
        busRouteNm[i].append(str(st_busRouteNm[i])[12:-12])
                   
    for i in range(len(tables1)):
        st_tables2.append(tables1[i].find_all('arrmsg1'))
    
    for i in range(len(tables1)):
        st_tables3.append(tables1[i].find_all('arrmsg2'))
    
    for i in range(len(st_tables2)):
        tables2[i].append(str(st_tables2[i])[10:-11])
    
    for i in range(len(st_tables3)):
        tables3[i].append(str(st_tables3[i])[10:-11])

    bus_info = '----'+stNm+'----\n'

    for i in range(len(tables1)):
        for j in busRouteNm[i]:
            bus_info += j+'\n'
        for j in tables2[i]:
            bus_info += j +'\n'
        for j in tables3[i]:
            bus_info += j +'\n\n'
            
    return bus_info
