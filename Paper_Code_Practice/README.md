# Transformer
Transformer 모델은 자연어 처리에서 가장 기본이 되고 있기 때문에, 한번 제대로 공부해 보고자 하는 마음에 논문부터 코드 구현까지 해보게 되었다.

코드는 hyunwoongko님 깃허브 자료의 도움을 받았으며, Transformer 모델 구현부터 한영 번역 학습까지 진행하였다. 

논문의 구성 요소들을 바탕으로 공부한 내용과 코드를 리뷰해 보았다.

- Date : 12월 9일 ~ 1월 15일
- Paper: Attention Is All You Need

colab 에서 다음과 같이 시도해볼 수 있다.
```
!git clone https://github.com/angiekim05/study.git
%cd /content/study/Paper_Code_Practice/Transformer
!pip install -r requirements.txt
```
   
- 모델 학습
모델 학습은 config.py 파일을 조절하며 학습시킬 수 있다.
```
!python train.py
```
   
- 한영 번역
```
!python predict.py --input "오늘은 날씨가 좋아요."

# Input: 오늘은 날씨가 좋아요.
# Output: today s weather is good for good weather .

!python predict.py --input "요즘 경제가 나쁘다"

# Input: 요즘 경제가 나쁘다
# Output: the economy is bad news for economic growth .
```
   
- 한계점
    - 데이터의 질과 양의 한계가 있다.
    - 100 epoch 정도에서 valid loss가 4.3 이하로 내려가지 않는 반면, train loss가 계속 감소하는 과적합이 나타났다.

- 배운점
    - 처음 구조부터 직접 구현하고, 기록을 남기며 공부를 하면서 pytorch에서 사용하는 함수 등에 대한 이해도를 크게 높일 수 있었다.
    - colab에서 학습하는데 시간이 제한되어 있어 retrain할 때, 모델 로드뿐만 아니라 스케줄러의 last_epoch까지 고려해볼 수 있었다.