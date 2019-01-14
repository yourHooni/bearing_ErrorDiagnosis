# bearing_ErrorDiagnosis
딥러닝 이용 자동차 베어링 및 타이어 마모 진단


# 실행 환경
 - python 3.5
 - tensorflow(keras)
 
# 파일
 - Diagnosis_control/ : 전체적인 시스템 실행 파일이 있는 폴더
     - DiagnosisSystem_UI.py : 시스템 UI
     - Diagnosis_control.py : 진단 실행
     - recording.py : 소음 녹음
     - predict.py : 예측 결과 출력
     
- Diagnosis_control/preprocessing : 전처리 실행 파일이 있는 폴더
     - BandpassFiltering.py : bandpass 실행 (해당 음역대 추출)
     - fft_.py : fft 및 미분 실행
     - original.py : 본래 소음과 주기 추출 및 미분 실행
     - volumeManage_range.py : 소음의 크기 일정하게 조절
     
- Diagnosis_control/models : deep learning 모델 관련 파일이 있는 폴더
     - loadData.py : 데이터를 불러와 모델에 입력할 input size로 조절
     - models.py : 모델 
     - train.py : 모델 훈련 실행
