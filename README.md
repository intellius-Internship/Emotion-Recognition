# :tada: **Emotion-Recognition** 

### **Evaluation**
Accuracy와 F1 Score로 성능 측정

| CATEGORY | LABEL |
|--|--|
| 불안 | 2 |
| 분노 | 0 |
| 슬픔 | 1 |
| 기쁨 | 5 |
| 상처 | 3 |
| 당황 | 4 |

<br>

<details>
<summary><strong>데이터 분포</strong></summary>
<div markdown="1">

| emotion-main-category (dev) | counts |
|--|--|
| 불안 | 7324 |
| 분노 | 6908 |
| 슬픔 | 6903 |
| 기쁨 | 6725 |
| 상처 | 6617 |
| 당황 | 6350 |

| emotion-main-category (test) | counts |
|--|--|
| 불안 | 904 |
| 분노 | 872 |
| 슬픔 | 860 |
| 기쁨 | 840 |
| 상처 | 831 |
| 당황 | 815 |


</div>
</details>

<br>

### **Deep Learning**

| Model | Accuracy | F1 Score |
|--|--|--|
| `monologg/koelectra-base-v3` | 66.89 | 67.37 | 
| `monologg/kobert` | 62.35 | 65.23 |
| `monologg/kobigbird-bert-base` | 66.75 | 67.50 |


<br>

### **Machine Learning**


| Model | Accuracy |
|--|--|
|  |  |


