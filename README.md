# 안암어스 백엔드

2022 KU 스마트 캠퍼스 데이터톤 5조 안암어스 백엔드 저장소

안암 지역 배리어프리 수준 시각화 및 경로 추천 웹사이트의 API 개발 및 서버 배포

## 주요 기능

- 경사로, 도로포장도, 계단 여부 등 사회적 약자 이동권과 관련된 요소를 고려하여 안암동 내 다양한 경로에 따른 배리어프리 수준을 확인할 수 있는 **배리어프리 지도**를 제공
- 나아가 이러한 배리어프리 수준을 고려하여 최적 경로를 추천하는 **배리어프리 경로 찾기** 기능을 제공
- 마지막으로 웹사이트 사용자들의 건의사항을 수렴할 수 있는 **게시판**도 제공

배포된 서비스는 [링크](http://anam-earth.jseoplim.com)로 접속 가능하다.

## 배포 및 인프라

### 아키텍처

![아키텍처](https://user-images.githubusercontent.com/86508420/187080789-1ebf33de-44a9-4c00-8a89-e4bd70dfb593.png)


### CI/CD

![CI-CD](https://user-images.githubusercontent.com/86508420/187080686-06ca208d-7308-4ef4-a333-8d1f392ed688.png)



## 설치 및 실행

git, docker, docker compose가 설치된 Linux 환경을 전제한다.

```bash
# GitHub에서 프로젝트 파일 내려받기
git clone https://github.com/jseop-lim/anam-earth-be.git
cd anam-earth-be/backend

# Docker 컨테이너 빌드 및 실행
docker compose -f docker-compose.local.yml up -d

# 백엔드 컨테이너에서 bash shell 실행
docker exec -it anam-earth-backend bash

# 백엔드 컨테이너 로그 확인
docker logs -f anam-earth-backend
```

## 디렉토리 구조

*앱 설명*

*데이터 설명*

*데이터 삽입 자동화*

## 기술스택

### API

* 언어: 파이썬

* 프레임워크: 장고, DRF

* 데이터베이스: MySQL

* 기타:

  * networkx - 최단 경로 계산 위한 그래프 라이브러리
  * Swagger - API 명세

  * GeoJson - 지리정보 저장 양식. 프론트와의 통신에 사용

### 배포

Docker, S3

EC2, Nginx, Gunicorn, MySQL

GitHub Actions, AWS CodeDeploy
