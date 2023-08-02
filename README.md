<div align="center">
  <h1>흡연자 검출 모델을 활용한
  
  "단속반 &amp; 미화원" 경로 추천 서비스</h1>
<p align="center">
  <img src="https://user-images.githubusercontent.com/90829718/241697029-2119575e-890a-4ede-b4b6-3a507f9f256c.png" width="150" />
</p>
</div>

<div align="center">
    <h2>🚬 바른흡연 🔎</h2>
 </div>

<br />

## 목차
1. [**바른흡연 프로젝트란**](#barunsmoke)
1. [**기대 효과**](#effect)
1. [**수상 기록**](#awards)
1. [**구성 요소**](#Component)
1. [**데모영상**](#DeepLearning)
1. [**기술 스택**](#tech-stack)
1. [**구조도**](#structure)
1. [**검출과정**](#detection-process)
1. [**UX**](#UX)
<br />

<a name="barunsmoke"></a>

## 📚 바른흡연 프로젝트란
>프로젝트 "바른흡연"은, 흡연자의 행위패턴을 분석하여 만들어낸 흡연자 검출 모델을 활용한 경로추천 서비스입니다.  <br/>
>흡연 관련 업무를 수행하는 단속반 및 미화원 분들에게 최적의 업무 경로를 제공하는 것을 목표로 합니다
<br/>

<a name="effect"></a>

## 💡 기대 효과
>1. 흡연자 검출수 기반 히트맵을 통해 효율적인 구역관리 지원.  <br/>
>2. 사용자 맞춤형 경로 추천으로 업무 효율 향상.  
>2-1. 최소 검출수 조정으로 선택적 경유지 설정  
>2-2. '최단거리' 경로 추천 지원  
>2-3. '검출수 우선' 경로 추천 지원  
>3. 검출수 데이터 통계로 더 정확한 단속 계획 수립 지원.
>4. 구역별 검출수 초기화 기능으로 미화원간 업무 혼선 방지.
<br/>

<a name="awards"></a>

## 🏆 수상
>2023 한성대학교 컴퓨터공학부 캡스톤디자인 우수상
<br/>
<br/>
<br/>


<a name="Component"></a>
## 📌 구성 요소
| <div align="center"/>기능                      | <div align="center"/>내용                                                  |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------- |
| <div align="center"/>🔗[**딥러닝 서버(detect_server)**](https://github.com/DaMoim-Team/DaMoim_detect_server)|- SORT & CROP<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 프레임 속 사람객체 id 부여<br/>&nbsp;&nbsp;&nbsp;&nbsp;- id별 bounding box기준 Crop<br/>- Custom Yolov8<br/>&nbsp;&nbsp;&nbsp;&nbsp;- AI hub, Kaggle에서 Dataset 확보<br/>&nbsp;&nbsp;&nbsp;&nbsp;- smoking_head(담배를 입에 무는 지점) Roboflow에서 Labeling<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 검출 빈도 알고리즘<br/>- OpenPose<br/>&nbsp;&nbsp;&nbsp;&nbsp;- pose estimation 팔 각도 계산<br/>&nbsp;&nbsp;&nbsp;&nbsp;- Frame-to-Frame 팔 각도 변화 알고리즘<br/>- 스케줄링<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 시간 단위 검출 랭킹 갱신<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 하루 단위 검출 랭킹 갱신|
| <div align="center"/>🔗[**클라이언트(client)**](https://github.com/DaMoim-Team/DaMoim-client)|- Firebase 유저 직업 관리<br/>- 검출수 기준 히트맵 및 경로 추천<br/>- 검출수 초기화 및 시간별 검출통계|
| <div align="center"/>🔗[**경로 서버(server)**](https://github.com/DaMoim-Team/DaMoim_server)|- Naver Direction API<br/>- 유저에게 경로 전송
| <div align="center"/>🔗[**Raspberry PI**](https://github.com/DaMoim-Team/Damoim-raspberrypi)|- 구역별 영상 딥러닝 서버에 전송

<br/>
<br/>

<a name="DeepLearning"></a>

## 🎥 데모영상
| <div align="center"/>데모 영상(DeepLearning)| <div align="center">데모 영상(UX)|
| :----------------------------------------- |:----------------------------- |
|🔗[**데모 영상(DeepLearning)**](https://drive.google.com/file/d/1NBmrCbGCv-uRbUIqbFNxQw5h5DR22z7v/view?usp=sharing)|🔗[**데모 영상(UX)**](https://drive.google.com/file/d/1phko7jBVAgpvAYwbGcoiLxRUNEjyyV1l/view?usp=sharing)|
|<img src="https://user-images.githubusercontent.com/90829718/241766271-78b0295e-8af2-4d6c-9e48-bf754b405b3e.jpg" alt="딥러닝 데모영상" width="400"/>|<img src="https://user-images.githubusercontent.com/90829718/242057747-c0b3efe3-dd9f-49dd-bc00-2e9c34995d1b.jpg" alt="클라이언트 데모영상" width="400"/>|

<br/>
<br/>
<a name="tech-stack"></a>

## 🛠 기술 스택

![](https://img.shields.io/badge/%20OpenPose-%2300008B)
<img src="https://img.shields.io/badge/YOLOv8-F79025?style=flat&logo=YOLO&logoColor=white" /> <img src="https://img.shields.io/badge/YOLOv5-000000?style=flat&logo=YOLO&logoColor=white" /> ![](https://img.shields.io/badge/%20SORT-%234B0082)

<img src="https://img.shields.io/badge/OpenCV-v4.7.0-000000?style=flat&logo=OpenCv&logoColor=white" /> <img src="https://img.shields.io/badge/Pytorch-v2.0.0+cu117-000000?style=flat&logo=PyTorch&logoColor=white" />

<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white" /> <img src="https://img.shields.io/badge/Swift-FF4500?style=flat&logo=Swift&logoColor=white" />

<img src="https://img.shields.io/badge/raspberrypi-A22846?style=flat&logo=raspberrypi&logoColor=white" /> <img src="https://img.shields.io/badge/AWS-FF9900?style=flat&logo=amazonaws&logoColor=white" />
![](https://img.shields.io/badge/%20-GoormIDE-blue)
 <img src="https://img.shields.io/badge/Colab-FFDB00?style=flat&logo=Google Colab&logoColor=orange" />

<img src="https://img.shields.io/badge/Flask-98FB98?style=flat&logo=Flask&logoColor=black" /> <img src="https://img.shields.io/badge/NaverMapAPI-2E8B57?style=flat&logo=Naver&logoColor=white" /> <img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat&logo=Firebase&logoColor=white" /> <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=MySQL&logoColor=white" />


<br/>
<a name="structure"></a>

## ⚙ 구조도
<p align="center">
  <img src="https://user-images.githubusercontent.com/90829718/241696820-1fe716a9-c40a-482f-9f3d-1635bcfbd2df.jpg" width="1500" />
</p>
<br/>
<br/>

<a name="detection-process"></a>

## 🔍 검출과정
<p align="center">
  <img src="https://user-images.githubusercontent.com/90829718/243065647-8a328a73-4d98-4c3b-a57b-74da425e15c3.jpg" width="1500" />
</p>
<br/>
<br/>

<a name="UX"></a>

## 📱 UX
<p align="center">
  <img src="https://user-images.githubusercontent.com/90829718/243067198-352d0ee6-1f09-4fa6-82ec-7bd5b88b953f.jpg" width="1500" />
</p>
<br/>
<br/>
   
