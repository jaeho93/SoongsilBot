# SoongsilBot

1. [프로젝트_개요](#프로젝트_개요)
2. [개발_환경](#개발_환경)
3. [라이선스](#라이선스)
4. [사용_라이브러리](#사용_라이브러리)

## 프로젝트_개요

### 개발 배경

> 학생들이 원하는 정보를 학교 홈페이지에서 찾는 것이 가능하긴 하지만 스마트폰에서 작은 글씨를 읽어가면서 원하는 정보를 빠르게 얻기 어렵다. 카카오톡 메신저에서 원하는 정보를 알려주는 챗봇을 개발하여 학생들이 알고 싶은 정보를 채팅으로 알려주는 서비스를 제공한다.

## 개발_환경
* Python 3
* Amazon AWS EC2
* Ubuntu Linux t2.micro
* Apache HTTP Server

## 라이선스
* [MIT License](LICENSE)

MIT License로 사용가능합니다.

## 사용_라이브러리

### [Django](https://www.djangoproject.com/)
> Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

* **용도 :** 웹 프레임워크
* **라이선스 :** The 3-Clause BSD License
* **라이선스 전문 :** [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)

### [플러스친구 자동응답 API](https://github.com/plusfriend/auto_reply)
> "플러스친구"는 회원이 작성한 콘텐츠를 이용자가 메시지나 포스트를 통하여 받아볼 수 있도록 제공하는 카카오톡 기반의 모바일 비즈니스 플랫폼 서비스를 말합니다. 회사는 회원에게 API 플랫폼 서비스(이용자에게 특정 답변 등을 요구하는 형태의 질문을 설계할 수 있는 채팅 플랫폼, 이하 “API 서비스”라 합니다)를 제공합니다.

* **용도 :**  카카오톡과 챗봇 
* **라이선스 :**
* **라이선스 전문 :** [플러스친구 이용약관](https://center-pf.kakao.com/terms)

### [EventDay](https://developers.sktelecom.com/content/sktApi/view/?svcId=10072)
> 다양한 출처 등으로 흩어져 있는 기념일 정보를 통합하고 사회/문화적으로 통용되는 기념일과 비주기 행사를 통합된 Event Data로 구성합니다. 구성된 정보는 손쉽게 호출하여 확인할 수 있으며, 이를 활용하여 서비스를 제공할 수 있도록 지원합니다.

* **용도 :**  서비스 날짜의 공휴일 여부 판별
* **라이선스 :** 
* **라이선스 전문 :** [이용약관](https://developers.sktelecom.com/policy/accessTerms/)

### [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
> Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

* **용도 :** 웹 크롤링 및 파싱
* **라이선스 :** Python Software Foundation License
* **라이선스 전문 :** [PSF Doc](https://docs.python.org/3/license.html)

### [KoNLPy](http://konlpy.org/ko/latest/#)
> KoNLPy is a Python package for Korean natural language processing.

* **용도 :**  한글 형태소 분석
* **라이선스 :** GNU General Public License V3
* **라이선스 전문 :** [GPLv3](http://www.gnu.org/licenses/gpl.html)

### [Natural Language Toolkit](http://www.nltk.org/)
> LTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.

* **용도 :**  한글 형태소 분석 트리 비주얼라이징
* **라이선스 :** Apache License 2.0
* **라이선스 전문 :** [LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

### [SearchFirstAndLastTrainbyFRCodeService](http://data.seoul.go.kr/openinf/openapiview.jsp?infId=OA-1191&tMenu=11)
> 역외부코드로 지하철역별 첫차, 막차 시간 정보를 검색할 수 있도록 하는 API입니다.

* **용도 :** 지하철 첫차와 막차 정보 검색
* **라이선스 :** 저작자표시(BY)
* **라이선스 전문 :** [저작자표시 2.0 대한민국 (CC BY 2.0 KR)](https://creativecommons.org/licenses/by/2.0/kr/)

### [SearchArrivalInfoByFRCodeService](http://data.seoul.go.kr/openinf/openapiview.jsp?infId=OA-102&tMenu=11)
> 역외부코드로 지하철역별 열차 도착 정보를 검색할 수 있도록 하는 API입니다.

* **용도 :** 열차 도착 정보 검색
* **라이선스 :** 저작자표시(BY)
* **라이선스 전문 :** [저작자표시 2.0 대한민국 (CC BY 2.0 KR)](https://creativecommons.org/licenses/by/2.0/kr/)
