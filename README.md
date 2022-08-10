# 딥러닝 기반 Kubernetes Autoscaler 성능 개선 프로젝트

---

## 팀원
[(팀장)금나연](https://github.com/NayeonKeum)
[김상홍](https://github.com/bconfiden2)
[김지혜](https://github.com/asd3638)
[유지연](https://github.com/hellouz818)

<br>

---

## 프로젝트 주제: AI-HPA

<p align="center">

<h3>딥러닝 기반 모델 성능 비교를 통해 최적의 예측 모델 선정</h3>
<h3>사용자가 predictive scaling을 원하는 특정 서비스에만 적용 가능</h3>
<h3>Kubernetes의 standard pod의 형태로 실행 가능하게 제공</h3>

</p>

<br>

---

## 프로젝트 선정 배경

#### Kubernetes Default Autoscaler - HPA

Reactive 방식으로 특정 주기마다 metrics server로부터 자원 사용량을 확인하여 미리 지정해둔 threshold를 넘어가면 스케일링이 됨

- 한계점: HPA가 메트릭 서버로부터 폴링하는 주기, 메트릭 서버가 메트릭을 수집하는 주기로 인해 실제 스케일링해야할 값에 대한 대기 시간이 발생하여 적시에 스케일링할 수 없음

#### Proactive Autoscaler - PHPA

특정 구간의 사용량을 예측하여 미리 스케일링함으로써 HPA에서 발생하는 대기 시간 문제를 해결함

- 한계점: 단순한 통계 모델(Linear Regression, Holt-Winters Smoothing)을 사용하여 높은 예측 정확도를 기대하기 어려움

<br>

<img width="880" alt="HPA-반응시간" src="https://user-images.githubusercontent.com/68985625/183814343-87f6cd12-feb9-41bc-9e82-a08614ca0f3a.png">

<br>

### => 대기시간을 없애면서 예측 정확도를 높을 수 있는 새로운 Autoscaler의 도입 필요

<br>

---

## 아키텍처

### CPU 분석 기법

</br>

<img width="801" alt="CPU-분석기법" src="https://user-images.githubusercontent.com/68985625/183815378-49ec7226-f6ee-42e2-b948-72b64b2b568b.png">

</br>

|Collect|Update|Predict|
|------|------|------|
|애플리케이션 메트릭을 수집하여 중앙 집중식 시계열 데이터베이스로 보내 수집된 메트릭을 활용하고 분석 단계에서 사용|Collector에서 특정 구간의 데이터를 쿼리하여 학습시킨 모델에 적용. 예측된 다음 시점의 워크로드에 대하여 설정한 알고리즘을 바탕으로 다음 시점의 파드 수 예측|Kubernetes 엔진(kube-apiserver)은 예측 단계로부터 명령을 받아 Pod의 복제본 수를 변경|

<br>

### 아키텍처 구현

<img width="928" alt="AI-HPA-아키텍처" src="https://user-images.githubusercontent.com/68985625/183815374-d0498e75-35a4-4d64-8cf3-bbbbbcfcd094.png">


#### 1. 서비스별 메트릭 수집
Autoscaling하려는 deployment로부터 생성된 파드들의 CPU 사용량을 합산해 해당 서비스의 총 CPU 사용량을 수집

#### 2. 트래픽 예측
사용자가 정해둔 CPU limit을 기준으로 딥러닝 모델은 특정 시점의 Pod 개수를 예측

#### 3. Replicaset 업데이트
Kubernetes 엔진(kube-apiserver)은 Automatic Scaler의 명령을 통해 적절한 Pod 복제본 수 변경

<br>

---

## 딥러닝 모델

### Bi-LSTM(Bidirectional LSTM)

<br>

### [모델 레포지토리 링크](https://github.com/Scooter-2022/Model)

<br>

<img width="543" alt="Bi-LSTM-Arch" src="https://user-images.githubusercontent.com/68985625/183815974-05ab25b2-3849-4357-b707-3ae680ff7ec9.png">

<br>

표준 LSTM과 달리 입력이 양방향으로 흐르고, 양방향의 정보를 활용
시퀀스의 양방향에서 순차적 종속성을 모델링하는 도구
정보 흐름의 방향을 반대로 하는 LSTM 레이어를 추가

[출처](https://www.baeldung.com/cs/bidirectional-vs-unidirectional-lstm)

<br>

### Hyper-parameter info

최적의 파라미터 및 손실함수 결정

<img width="925" alt="Bi-LSTM-hyper-param" src="https://user-images.githubusercontent.com/68985625/183816142-60d6a840-5c28-483a-8991-d21990997178.png">


### 차별성 검증
#### HPA, PHPA 와의 차별성 검증
학습된 모델, Kubernetes에서 제공하는 기본 Autoscaler HPA, 오픈소스 Predictice HPA, 총 세 가지 모델에 랜덤으로 발생시킨 트래픽으로 성능 비교
예측 정확도를 바탕으로 개발한 모델의 스케일링 효과를 검증

<br>

#### 이미지

<img width="1303" alt="compare-hpa-ai-hpa" src="https://user-images.githubusercontent.com/68985625/183820991-7e80e101-617a-442c-af2a-1831749e1a73.png">

<br>

---

## 시연

https://user-images.githubusercontent.com/68985625/183821998-4d7a5194-cf08-4984-9dd0-bff6fed9972f.mp4

<br>

