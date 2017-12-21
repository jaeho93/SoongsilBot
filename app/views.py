from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime, time
from . import keyboards
from . import meal_crawl
from . import subway_crawl

def keyboard(request):
    return JsonResponse(keyboards.default_keyboard())

@csrf_exempt
def message(request):
    json_str = (request.body).decode('utf-8')
    received_json_data = json.loads(json_str)
    content_text = received_json_data['content']

####식당 정보
    if content_text == '식당 메뉴':
        return JsonResponse({
            'message' :{
                'text' : '식당을 선택해주세요.'
            },
            'keyboard' : keyboards.meal_keyboard()
        })

####식당 정보 보기
    elif content_text == '학생 식당' or content_text == '교직원 식당':
        return JsonResponse({
            'message' :{
                'text' : meal_crawl.get(content_text)
            },
            'keyboard' : keyboards.default_keyboard()
        })

####교통 정보
    elif content_text == '교통 정보':
        return JsonResponse({
            'message' :{
                'text' : '버스, 지하철 중에서 선택하세요.'
            },
            'keyboard' : keyboards.transport_keyboard()
        })

####지하철 정보
    elif content_text == '지하철 정보':
        return JsonResponse({
            'message' :{
                'text' : '노선을 선택하세요.'
            },
            'keyboard' : keyboards.subway_keyboard()
        })

####버스 정보
    elif content_text == '버스 정보':
        return JsonResponse({
            'message' :{
                'text' : '정류소를 선택하세요.'
            },
            'keyboard' : keyboards.bus_keyboard()
        })

####지하철 상행선/하행선
    elif content_text == '상행선(건대행)' or content_text == '하행선(대림행)' :
        return JsonResponse({
            'message' :{
                'text' : subway_crawl.get(content_text)
            },
            'keyboard' : keyboards.default_keyboard()
        })

####버스 정류소별 정보
    elif content_text == '정문 앞' or content_text == '정문 건너편'\
    or content_text == '중문 앞' or content_text == '중문 건너편'\
    or content_text == '기숙사 앞' or content_text == '기숙사 건너편':
        return JsonResponse({
            'message' :{
                'text' : '미구현'
            },
            'keyboard' : keyboards.default_keyboard()
        })
