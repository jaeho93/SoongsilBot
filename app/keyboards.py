#keyboard

def default_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['식당 메뉴','교통 정보']
        }

def meal_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['학생 식당','교직원 식당']
        }

def transport_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['지하철 정보','버스 정보']
        }

def subway_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['상행선(건대행)','하행선(대림행)']
        }

def bus_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['정문 앞','정문 건너편','중문 앞','중문 건너편','기숙사 앞','기숙사 건너편']
        }

