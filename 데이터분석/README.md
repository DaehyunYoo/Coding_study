# 데이터 분석 과제테스트 문제 풀이 순서

1. 데이터 확인
    - (data.info(), data.describe())

2. 결측치 처리
    - 평균, 중앙값, 최빈값으로 대체
    - (data['columns'] = data.fillna(data['columns'].mode()[0])) 

3. 이상치처리(IQR)
    - Q1 = data['columns'].quantile(0.25)
    - Q3 = data['columns'].quantile(0.75)
    - IQR = Q3 - Q1
    - data['columns'] = np.where(data['columns'] > (Q3 + 1.5 * IQR), Q3, data['columns'])
    - data['columns'] = np.where(data['columns'] < (Q1 - 1.5 * IQR), Q1, data['columns'])

4. 범주형 변수 처리
    - LabelEncoder() 사용
    - Encoder = LabelEncoder(),
    - Encoder.fit(data['columns'])
    - data['columns'] = Encoder.transform(data['columns'])

5. 데이터 분리
    - train_test_split() 사용 // train, test 파일이 따로 나눠져 있는 경우 train을 validation으로 나누기
    - x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = 0.2, random_state = 42)
    - x, y 변수 설정
        - x_train = train.drop(columns = ['index','y_name'], axis = 1)
        - y_train = train['y_name']

6. StandardScaler 적용
    - scaler = StandardScaler()
    - x_train_scaled = scaler.fit_transform(x_train)
    - x_test_scaled = scaler.fit_transform(x_test)

7. 모델 학습
    - RandomForestClassifer() or RandomForestRegressor() 사용
    - model = RandomForestClassifer()
    - model.fit(x_train_scaled, y_train)

8. 예측(모델 평가)
    - pred = model.predict(x_test_scaled)
    - pred = model.predict_proba(x_test_scaled) # 이진 분류일 경우

9. 모델 평가
    - accuracy_score(y_test, pred)
    - confusion_matrix(y_test, pred)
    - classification_report(y_test, pred)

10. Submission 파일 생성
    - submission 파일에 적용 
    - sample_submission['변수1'] = pred[:, 0] / sample_submission['변수2'] = pred[:, 1]
    - sample_submission.to_csv('submission.csv', index = False)