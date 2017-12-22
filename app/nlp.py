from konlpy.tag import Twitter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime, time
from . import keyboards
from . import meal_crawl
from . import subway_crawl

def nlp(msg):
    call = {
            '식당 메뉴' : 0,
            '교통 정보' : 0,
            '학생 식당' : 0,
            '교직원 식당' : 0,
            '지하철 정보' : 0,
            '버스 정보' : 0,
            '상행선(건대행)' : 0,
            '하행선(대림행)' : 0,
            '정문 앞' : 0,
            '정문 건너편' : 0,
            '중문 앞' : 0,
            '중문 건너편' : 0,
            '기숙사 앞' : 0,
            '기숙사 건너편' : 0
            }

    t = Twitter()
    tag_ko = t.pos(msg)

    if t.nouns(msg).count('식당') or t.nouns(msg).count('메뉴'):
        call['식당 메뉴'] = 1
    if t.nouns(msg).count('교통'):
        call['교통 정보'] = 1
    if t.nouns(msg).count('교') or t.nouns(msg).count('교직원'):
        call['교직원 식당'] = 1
        meal_msg = '교직원 식당'
    if t.nouns(msg).count('학식') or t.nouns(msg).count('학생식당'):
        call['학생 식당'] = 1
        meal_msg = '학생 식당'
    if t.nouns(msg).count('버스'):
        call['버스 정보'] = 1
    if t.nouns(msg).count('지하철') or t.nouns(msg).count('막차')\
    or t.nouns(msg).count('첫차') :
        call['지하철 정보'] = 1

    if call['지하철 정보'] == 1:
        return JsonResponse({
            'message' :{
                'text' : '노선을 선택하세요.'
            },
            'keyboard' : keyboards.subway_keyboard()
        })
    elif call['버스 정보'] == 1:
        return JsonResponse({
            'message' :{
                'text' : '정류소를 선택하세요.'
            },
            'keyboard' : keyboards.bus_keyboard()
        })
    elif call['학생 식당'] == 1 or call['교직원 식당']:
        return JsonResponse({
            'message' :{
                'text' : meal_crawl.get(meal_msg)
            }
        })
    elif call['교통 정보'] == 1:
        return JsonResponse({
            'message' :{
                'text' : '버스, 지하철 중에서 선택하세요.'
            },
            'keyboard' : keyboards.transport_keyboard()
        })
    elif call['식당 메뉴'] == 1:
        return JsonResponse({
            'message' :{
                'text' : '식당을 선택하세요.'
            },
            'keyboard' : keyboards.meal_keyboard()
        })
    else:
        return JsonResponse({
            'message' :{
                'text' : '잘 모르겠습니다. 알고 싶은 내용이 아래에 있나요?'
            },
            'keyboard' : keyboards.default_keyboard()
        })

