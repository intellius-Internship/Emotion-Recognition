# :tada: **Emotion-Recognition** 

### **Dataset** 

AI Hub 감성 대화 말뭉치의 6가지 감정 분류 (분노, 슬픔, 당황, 상처, 기쁨, 불안) 중
4가지 감정 분류 (분노, 슬픔, 기쁨, 불안) 사용

<br>

### **Evaluation**
Accuracy와 F1 Score로 성능 측정

| CATEGORY | LABEL |
|--|--|
| 분노 | 0 |
| 슬픔 | 1 |
| 불안 | 2 |
| 기쁨 | 3 |

<br>

<details>
<summary><strong>데이터 분포</strong></summary>
<div markdown="1">

| emotion-main-category (dev) | counts |
|--|--|
| 불안 | 9308 |
| 분노 | 8783 |
| 슬픔 | 12140 |
| 기쁨 | 7420 |


| emotion-main-category (test) | counts |
|--|--|
| 불안 | 1193 |
| 분노 | 1105 |
| 슬픔 | 1484 |
| 기쁨 | 920 |


</div>
</details>

<br>

## 📈 **데이터 별 성능 비교**

<br>

### **PLM on Original Data** 

| Model | Accuracy | F1 Score |
|--|--|--|
| `monologg/koelectra-base-v3` | 66.89 | 67.37 | 
| `monologg/kobert` | 62.35 | 65.23 |
| `monologg/kobigbird-bert-base` | 66.75 | 67.50 |

<br>


### **PLM on Preprocessed Data** 

| Model | Accuracy | F1 Score |
|--|--|--|
| `monologg/koelectra-base-v3` | 75.90 | 76.80 | 
| `monologg/kobert` | 31.05 | - |
| `monologg/kobigbird-bert-base` | 76.09 | 76.92 |

<br>

**🧐 BigBird 예측 데이터 분석**  

| Category | Real Cnt | Pred Cnt | Precision | Recall | Predictions | 
|--|--|--|--|--|--|
| 분노 | 1105 | 1438 | 63.42 | 82.53 | {`분노`: 912, `불안`: 95, `슬픔`: 90, `기쁨`: 8} | 
| 슬픔 | 1484 | 1251 | 83.77 | 70.61 | {`슬픔`: 1048, `분노`: 282, `불안`: 147, `기쁨`: 7} | 
| 불안 | 1193 | 1261 | 71.13 | 75.18 | {`불안`: 897, `분노`: 190, `슬픔`: 90, `기쁨`: 16} | 
| 분노 | 920 | 752 | 95.87 | 78.36 | {`기쁨`: 721, `불안`: 122, `분노`: 54, `슬픔`: 23} | 


### **ML Model on Preprocessed Data**


| Model | Accuracy | F1 Score | 
|--|--|--|
| Support Vector Classifier | 67.73 | 68.05 | 
| XGBoost Classifier | 65.54 | 65.48 | 
| Decision Tree | 55.69 | 55.55 | 
| KNeighbors Classifier | 50.76 | 47.85 | 


<br>

