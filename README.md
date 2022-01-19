# :tada: **Emotion-Recognition** 

### **Dataset**  
AI-Hub 감성 대화 말뭉치의 6가지 감정 분류 중 *분노, 슬픔, 기쁨 데이터*  
Wellness 정신건강 데이터의 *우울 데이터*  
혐오 발화 분류 데이터의 *혐오 발화 데이터, 일반 발화 데이터*  

> 혐오 분류 데이터는 영화 리뷰 데이터로, "재밌다", "멋있어" 등 특정 발화가 포함된 데이터를 행복 데이터로 사용

감정 분류 데이터 (중립, 놀람, 슬픔, 분노, 행복으로 분류)의 *중립, 슬픔, 분노, 행복 데이터*

### **Evaluation**
Accuracy와 F1 Score로 성능 측정

| CATEGORY | LABEL | COUNT |
|--|--|--|
| 중립 | 0 |40834|
| 행복 | 1 | 30662 |
| 슬픔 | 2 | 24344 |
| 분노 | 3 | 38141 |

<br>


## 📈 **메소드 별 성능 비교**

<br>

### **Performance of PLM** 

| Model | Accuracy | F1 Score |
|--|--|--|
| `monologg/koelectra-base-v3` | 54.21 | 49.59 | 
| `monologg/kobert` | 90.52 | 90.59 |
| `monologg/kobigbird-bert-base` | 28.32 | 11.39 |

<br>


### **Performance of ML Model**


| Model | Accuracy | F1 Score | 
|--|--|--|
| Support Vector Classifier |  |  | 
| XGBoost Classifier |  |  | 
| Decision Tree |  |  | 
| KNeighbors Classifier |  |  | 


<br>

