from bs4 import BeautifulSoup
from urllib.request import urlopen

def get(place):
    if place == '학생 식당':
        return haksik()
    elif place == '교직원 식당':
        return gyosik()

def haksik():
    try:
        html = urlopen('http://www.soongguri.com/main.php?mkey=2&w=3&l=2')
        source = html.read()
        html.close()
    except:
        return '일시적인 접속 오류입니다.\n잠시 후 다시 이용해 주세요.'

    soup = BeautifulSoup(source,'lxml')
    tables = soup.find_all('td', attrs={'class':'menu-list-t1'})
    bs_haksik_today = list()
    haksik_today = [[],[],[],[]]
    for i in range(4):
        bs_haksik_today.append(tables[i].find_all('div', attrs={'style':''}))
    for i in range(4):
        for j in range(len(bs_haksik_today[i])):
            haksik_today[i].append(str(bs_haksik_today[i][j])[5:-6])

    haksik_today_str = '----중식1----\n'
    for menu in haksik_today[0]:
        haksik_today_str += menu+'\n'
    haksik_today_str += '----중식2----\n'
    for menu in haksik_today[1]:
        haksik_today_str += menu+'\n'
    haksik_today_str += '----중식3----\n'
    for menu in haksik_today[2]:
        haksik_today_str += menu+'\n'
    haksik_today_str += '----석 식----\n'
    for menu in haksik_today[3]:
        haksik_today_str += menu+'\n'
    return haksik_today_str

def gyosik():
    try:
        html = urlopen('http://www.soongguri.com/main.php?mkey=2&w=3&l=2')
        source = html.read()
        html.close()
    except:
        return '일시적인 접속 오류입니다.\n잠시 후 다시 이용해 주세요.'

    soup = BeautifulSoup(source,'lxml')
    tables1 = soup.find_all('td', attrs={'class':'menu-list-t1'})
    bs_tables2 = list()
    tables2 = [[],[],[],[]]

    bs_tables2.append(tables1[4].find_all('div', attrs={'style':''}))

    for j in range(len(bs_tables2[0])):
        tables2[0].append(str(bs_tables2[0][j])[5:-6])

    bs_tables2.append(tables1[5].find_all('p'))

    for j in range(len(bs_tables2[1])):
        tables2[1].append(bs_tables2[1][j].text)

    for i in range(2):
        bs_tables2.append(tables1[i+6].find_all('div', attrs={'style':''}))
    for i in range(2):
        for j in range(len(bs_tables2[i+2])):
            tables2[i+2].append(str(bs_tables2[i+2][j])[5:-6])

    gyosik_today_str = '----조 식----\n'
    for menu in tables2[0]:
        gyosik_today_str += menu+'\n'
    gyosik_today_str += '----중식1----\n'
    for menu in tables2[1]:
        gyosik_today_str += menu+'\n'
    gyosik_today_str += '----중식2----\n'
    for menu in tables2[2]:
        gyosik_today_str += menu+'\n'
    gyosik_today_str += '----석 식----\n'
    for menu in tables2[3]:
        gyosik_today_str += menu+'\n'
    return gyosik_today_str


print(get('학생 식당'))
print(get('교직원 식당'))
