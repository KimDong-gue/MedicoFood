# MedicoFood
환자 맞춤형 식단 추천 커뮤니티 플랫폼

프로젝트명 . 
MediCoFood
주제
질환별 맞춤형 식단 추천 및 합리적 구매를 위한 통합 커뮤니티

개요 기간/인원/배경/목적
2024-05-30
역할
기술스택
성과 획득 역량

# <b> MediCoFood </b>

### <b>질환별 맞춤형 식단 추천 및 합리적 구매를 위한 통합 커뮤니티 프로젝트</b>


<br><br>

## 1. Collaborator
- 팀장 : 황지원
- 팀원 : 강은지, 김동신, 김태현, 조진우, 정수연

<br><br>

## 2. Tech
- Front-End
<br><br>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white">&nbsp;
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white">&nbsp;
&nbsp;<img src="https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=Figma&logoColor=white">&nbsp;
      <img src="https://img.shields.io/badge/JavaScript-E2BD40?style=flat-square&logo=JavaScript&logoColor=white">&nbsp;
  
- Back-End
<br><br>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white">&nbsp;
  <img src="https://img.shields.io/badge/Mysql-4479A1?style=flat-square&logo=Mysql&logoColor=white">&nbsp;
  <img src="https://img.shields.io/badge/표시할이름-색상?style=for-the-badge&logo=기술스택아이콘&logoColor=white">
  <img src="https://img.shields.io/badge/Django-215732?style=for-the-badge&logo=Django&logoColor=white">&nbsp;
  <br>

  - Edit Tool
  <br><br>
      <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white">&nbsp;
      <img src="https://img.shields.io/badge/Mysql Workbench-4479A1?style=flat-square&logo=Mysql&logoColor=white">&nbsp;
     <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=white">&nbsp;
      <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white">

<br><br>

## 3. Project Management (24.05.15 ~ 24.05.30)
### 프로젝트 개발 방식
  - #### `Front-End`

    `Figma`를 활용하여 UI/UX 설계
    <br>
  - #### `Back-End`

    `Django`를 통한 서버 통신, `MySQL`로 데이터베이스 설계.
    <br>
  - #### `Tech Architecture`
![image](https://github.com/KimDong-gue/MedicoFood/assets/116249934/fb588255-8ebe-49fd-94ca-651fcb9f653b)
    <br>

## 4. 프로젝트 상세 내용
<div align='center'>
  
  |기획 의도|
  |---|
  ![image](https://github.com/KimDong-gue/MedicoFood/assets/116249934/f5d9e6b4-3ad2-4da6-ae51-0d47cc059951)

  <br>
  
  |구현|
  |---|
  |![image](https://github.com/KimDong-gue/MedicoFood/assets/116249934/86d67977-388c-4c0a-9612-8c00e3fc2ec8)|
  |![image](https://github.com/KimDong-gue/MedicoFood/assets/116249934/83ce4de0-14bc-4b21-ab1a-1c93cb9f7ccd)|
  |![image](https://github.com/KimDong-gue/MedicoFood/assets/116249934/93a1a6c7-7d8f-46e9-97df-fb9ae9967885)|
  |![image](https://github.com/KimDong-gue/MedicoFood/assets/116249934/8b52685f-005c-45b6-9770-4569624792d7)|
  |![image](https://github.com/KimDong-gue/MedicoFood/assets/116249934/d0b21d4a-3afb-412f-b4ad-ddf630979e39)|


  <br>
  
  |Gantt Chart & Flow Chart|
  |---|


  <br>
  
  | 운동 자세 검출 예시 |
  |---|


  | 음식 추천 예시 |
  |---|


  | 운동 예시 |
  |---|


  <br>
  
  |시행 착오 / 개선 사항|
  |---|
  |<div align='center'>시행 착오</div>|
  |![image](https://github.com/KimDong-gue/Healthy-Mento/assets/116249934/8abcb693-79d5-466c-b2c4-b9c6624c5c8a)|
  |- `Yolo v8 Small` 모델링시, `Data InBalance` 문제 때문에, 데이터 증강을 수행 후, 어느정도의 `InBalance`를 해결하였습니다.
| - `MediaPipe`로 운동 자세를 검출할 때, 초기에 발생한 다양한 어려움들을 극복하기 위해 끊임없는 실험과 수정 작업이 필요했습니다. 이러한 경험을 통해 데이터 다양성, 후처리 기술의 활용, 적절한 임계값 설정, 모델의 업데이트에 대한 중요성을 깨달았습니다. 이러한 과정을 통해 프로젝트를 성공적으로 완료할 수 있었습니다. 
| - `Motion Transfer` 모델링시, 초기에 프로토타입을 빠르게 구현하고 사용자에게 시각적으로 효과를 보여주는 것이 목표였습니다. 그 후, 데모버젼을 구현하는데 성공하였습니다. 

  <br>
  
  |<div align='center'>참고 문헌</div>|
  |---|
  |https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch|
  ||
  |https://github.com/AliaksandrSiarohin/first-order-model|
  ||
  |https://github.com/svip-lab/impersonator|
  ||
  |https://github.com/Wangt-CN/DisCo?tab=readme-ov-file|
  <br>
  
</div>

