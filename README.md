# `홈쇼핑 짭모아` - 토이 프로젝트

이 프로젝트는 AngularJS와 Flask를 통해 홈쇼핑 모아의 클론을 만드는게 목표인 토이 프로젝트다.


## 시작하기

### 준비사항

시작하려면 먼저 `홈쇼핑 짭모아` 저장소를 복제해야한다.

```bash
git clone https://github.com
```

이 프로젝트는 서버와 클라이언트의 개발 언어가 다르므로 각자 설치를 진행하여야 한다. 


### 의존성

#### 서버

해당 프로젝트는 python3을 사용한다.

[파이선](https://www.python.org/downloads/)


#### 클라이언트

해당 프로젝트는 nodejs를 사용한다

[nodejs](https://nodejs.org/ko/)
 

### 설치 방법

#### 서버

```bash
pip install -r requirements.txt
```


#### 클라이언트


### 사용법

#### 서버

 * 아이템
```
URL:    GET http://localhost:5000/item/ft/date/time/asc
PARAM:  필터링, split tkn = :
        기본: all
        쇼핑몰 필터링: m:<얻을 쇼핑몰 이름(cjmall)>
        카테고리 필터링: ct:<얻을 카테고리 이름(유아·아동)>
        예:  cjmall, 모든 카테고리: m:cjmall
             cjmall, 유아·아동: m:cjmall:ct:유아·아동
return: application/json
```    
 * 카테고리
```
url:    GET http://localhost:5000/cate
param:  없음
return: application/json
```
 * 쇼핑몰
```
url:    GET http://localhost:5000/mall
param:  없음
return: application/json
```