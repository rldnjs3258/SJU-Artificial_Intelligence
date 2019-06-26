# 1. Computers vs. Neural Networks
### (1) Standard Computers
  - 1 CPU
  - 빠른 처리 장치
  - 신뢰할 수 있는 units
  - 정적 인프라

### (2) Neural Networks
  - 병렬 처리
  - 느린 처리 장치
  - 신뢰할 수 없는 units
  - 동적 인프라

<br>
<hr>
<br>

# 2. Why Artificial Neural Networks?
 - 인공 신경망(ANN)을 만드는 데 관심이 있는 이유는 기본적으로 두 가지이다.
### (1) 기술적 관점
  - 문자 인식이나 미래 예측과 같은 문제는 대량 병렬 처리(parallel) 및 적응 처리(adaptive)가 필요하다.

### (2) 생물학적 관점
  - 인공 신경망(ANN)은 인간 뇌의 구성 요소를 복제 및 시뮬레이션하여 자연의 정보 처리의 과정을 이용할 수 있다.


<br>
<hr>
<br>


# 3. Why Artificial Neural Networks?
### (1) Explicit
  - 앞에서 '상징적 인공 지능'은 쇄퇴 해 버렸고, 새로운 패러다임이 필요하다고 배웠다. 왜일까?
  - Explicit : '상징적 인공 지능'은 명시적(Explicit)인 지식을 표현하는데에만 적절한 형식을 제공한다.

### (2) Implicit
  - Implicit : 생물학적 시스템은 대부분 암묵적(Implicit)인 것이다. 불확실한 정보를 추론에 의해 배우기 때문이다.

### (3) Efficiently (효율적)
  - Efficiently : ANN은 본질적으로 병렬이며 병렬 하드웨어에서 매우 효율적으로 작동한다.


<br>
<hr>
<br>



# 4. How do NNs and ANNs work?
### (1) NN과 ANN에서 뉴런
  - NN에서 신경 네트워크를 구성하는 'building blocks'가 뉴런이다.
  - ANN에서는 뉴런을 units(단위) 또는 노드라고 한다.
  - NN에서 하나의 뉴런은 10,000개의 다른 뉴런과 연결될 수 있다.

### (2) ANN 작업 과정

  1) 각각의 뉴런은 다른 뉴런들로부터 입력을 받는다.
  
   - 생물학적 뉴런은 다른 뉴런들로부터 정보를 받을 때, 수용 영역(receptive field)에서 정보를 받는다.
   
  2) 활성화 : 들어온 입력을 기반으로 내부 상태를 변경한다.
  
  3) 출력하여 많은 다른 뉴런(입력 뉴런, recurrent network 포함)에게 보낸다.
  
   - 생물학적 뉴런은 정보를 전기 충격(spikes)를 통해 전달한다. 이러한 spike의 frequency 및 phase을 통해 정보를 인코딩 한다.


<br>
<hr>
<br>



# 5. History of Artificial Neural Networks
 - 1938 : Rashevsky는 미분 방정식을 통해 신경 활성화 동역학을 설명했다.
 - 1943 : McCulloch & Pitts는 생물학적 뉴런에 대한 최초의 수학적 모델을 제안했다.
 - 1949 : Hebb는 학습 규칙을 제안했다. 하나의 뉴런을 반복적으로 다른 뉴런과 활성화 하면 그들의 연결이 강화된다.
 - 1958 : Rosenblatt는 McCulloch & Pitts 모델에 학습 알고리즘을 추가하여 퍼셉트론을 발명했다.
 - 1960 : Widrow & Hoff는 Gradient Descent를 통해 훈련된 간단한 네트워크인 Adaline을 소개했다.
 - 1960 : Rosenblatt은 Multi layer networks를 교육하기 위한 계획을 제안했지만, non-differentiable node function 때문에 약한 기능이었다.
 - 1962 : Hubel & Wiesel은 self-organizing 신경 네트워크 모델을 자극하는 시각 피질의 특성을 발견했다.
 - 1962 : Novikoff는 퍼셉트론 convergence 정리를 증명했다.
 - 1964 : Taylor는 출력 unit 간의 억제 기능을 갖춘 winner-take-all 뉴럴 회로를 구축했다.
 - 1969 : Minsky & Papert는 퍼셉트론이 이론적으로 보편화 될 수 없다는 것을 설명했다. 이후 Neural Network에 대한 관심이 감소했다.
 - 1982 : Hopfield는 auto-association 네트워크를 제안했다.
 - 1985 : Ackley, Hinton & Sejnowski가 볼츠만 기계라는 확률론적 네트워크를 고안했다.
 - 1986 : Rumelhart, Hinton & Williams는 현대적인 형태의 backpropagation 알고리즘을 고안하여 많은 관심을 불러일으켰다.
 - 1986 : Hecht-Nielsen이 counterpropagation 네트워크를 개발했다.
 - 1988 : Carpenter & Grossberg는 적응 공명 이론(Adaptive Resonance Theory)를 고안했다.
 - 이후 ANN에 대한 연구가 활발하게 진행되어 왔고, 새로운 네트워크 유형 및 변화가 등장했다.
 
   또한, 뉴런 정보 처리를 위한 hybrid 알고리즘 및 하드웨어가 개발되었다.


<br>
<hr>
<br>


# 6. Neural Network : A Neuron
 - 뉴런은 서로 메시지(정보)를 교환하는 Neural Network의 계산 단위이다.
 
 1) Input layer
 
  - Bias, Weight가 계산된다.
  - Activation Function을 통해 다음 레이어로 출력된다. (Step function, Threshold function, Sigmoid function 등)
  
 2) Hidden layer
 
 3) Output


<br>
<hr>
<br>


# 7. Feed forward / Backpropagation Neural Network
 (1) Feed forward algorithm
  - Input 레이어부터 Output 레이어까지 뉴런을 활성화시키며 진행한다.

 (2) Backpropagation
  - 무작위로 parameters를 초기화한다.
  - Output 레이어에서 총 오류를 계산한다.
  - 이전 레이어로 돌아가며 오류들을 계산한다.


<br>
<hr>
<br>



# 8. Limitations of Neural Networks
 - 랜덤 초기화와 densely connected layer에 의한 한계점 
 
   (dense layer = fully connected layer = 각 노드가 후속 히든 레이어의 모든 노드에 연결된 히든 레이어)
   
### (1) 고비용
  - 뉴럴 네트워크의 각 뉴런은 logistic regression으로 간주 될 수 있다.
  - 전체 Neural Networks를 훈련시키는 것은 모든 상호 연결 된 logistic regression을 훈련시키는 것과 같다.
  
    즉, 비용이 크다.

### (2) Hidden layer의 수가 증가하면 학습시키기 어렵다.
  - Logistic regression은 gradient descent에 의해 훈련된다.
  - Backpropagation에서 Gradient는 점차 옅어진다.
  - Output layer에서 보정 신호는 최소가 된다.

### (3) Local optima에 갇힐 수 있다.
  - Neural network의 목적 함수는 일반적으로 볼록하지 않다.
  - 랜덤 초기화의 초기값은 Global optima를 보장하지 않는다.

### (4) Solution
  - Deep Learning
  - Multiple levels of representation 학습


<br>
<hr>
<br>


# 9. Deep Learning Overview
 - 많은 Hidden layers들을 통해 feature를 잘 추출하고, Output을 만들어 낸다.
 - Feature : 얼굴에서 눈, 코, 입과 같은 Edge를 뜻한다.
 
   Combination Feature : 눈과 코의 조합 Edge, 눈썹과 눈의 조합 Edge 등
   
  1) 첫 번째 레이어는 1차 feature를 학습한다. (Edge 등)
  
  2) 두 번째 레이어는 고차원 feature를 학습한다. (첫 번째 레이어의 feature와의 조합, Combination Feature 등)
  
   - 어떤 모델들은 Unsupervised로 학습하여, input 공간의 일반적인 feature를 학습한다.
   
     즉, Unsupervised 인스턴스와 관련된 여러 작업(이미지 인식 등)을 한다.
     
  3) 마지막 레이어의 변환된 feature를 supervised layer로 공급된다.
  
  4) 전체 네트워크는 Supervised 훈련을 토대로 tuned 된다.
   - Unsupervised 단계에서 배운 초기 가중치를 이용하여 Supervised 훈련


<br>
<hr>
<br>


# 10. Deep Net Feature Transformation

 1) Original Feature
 
  - 원래의 특징
  
 2) New Feature Space
  - New Feature Space를 통해 새로운 특징들을 찾아낸다.
  - Supervised / Unsupervised Learning
  
 3) ML Model에 새로운 특징을 반영
  - Supervised Learning


<br>
<hr>
<br>


# 11. Deep Learning Tasks
 - CNN, Unsupervised는 Input이 locally한 경우에 성능이 좋다. (이미지, 언어 등)
 - CNN은 필터를 Sliding window 하여 Feature(Edge)를 찾는다.
 - 예제 : 예제는 학습을 통해 Input Image에서 피쳐를 찾아낸 것이다. Input Image를 100 : 1의 비율로 활성화하여 각 피쳐를 찾았다.


<br>
<hr>
<br>


# 12. Why Deep Learning
### (1) 생물학적 타당성
 
  ex) Visual Cortex

### (2) 깊은 구조
  - 깊은 구조를 통해 다양한 기능을 효율적으로 표현할 수 있다.
  - 얕은 구조들보다 weights/parameters를 적게 업데이드 해도 된다.

### (3) Transfer learning
  - 기존의 만들어진 모델을 사용하여 새로운 모델을 만들시 학습을 빠르게 하며, 예측을 더 높인다.
  - 이미 학습된 weight들을 transfer(전송) 하여 자신의 model에 맞게 학습 시키는 방법이다.
  - 신경망의 이러한 재학습 과정을 세부 조정(fine-tuning)이라고 한다.

### (4) Sub-feautres
  - 깊은 구조에서 생성된 Sub-features들은 여러 작업에서 공유될 수 있다.
  - 전송 / 다중 작업


<br>
<hr>
<br>


# 13. Early Work
### (1) Fukushima (1980) : Neo-Cognitron
### (2) LeCun (1998) : Convolutional Neural Networks (CNN)
  - Neo-Cognitron과 비슷함
### (3) Backpropagation을 사용하는 MLP

  1) 일찍 시도를 했지만, 별로 성공하지는 못했다.
   - 아주 느리다.
   - Vanishing Gradient
   
  2) 최근에 Backpropagation을 사용하는 MLP를 GPU로 훈련한 결과 상당히 정확도가 향상됐다.
   - General Learning
   - 기본 BP 알고리즘을 확장하여 2012년 이후 많이 개선되었다.


<br>
<hr>
<br>


# 14. Vanishing(Exploding) Gradient
### (1) Recent Work
  - 오류 감소, GPU를 이용한 오랜 훈련 등
  - Rectified Linear Units, Weight 초기화 개선, 레이어 간 normalization 개선, residual deep learning 등

### (2) Vanishing gradient
  - Sigmoid는 적달된 값을 0과 1 사이로 심하게 변형한다. 이 때문에 값이 현저하게 작아지는 현상이 발생한다.
  - Vanishing gradient는 Sigmoid를 쓸 때, 이전 레이어로 전파될 때 감쇄하여 그래디언트가 사라지는 것이다.
  - 해결법 : Relu


<br>
<hr>
<br>


# 15. Unstable Gradient
 - 딥러닝에서 Vanishing(Exploding) Gradient이 불안정성이다.
 - '반대편'의 레이어가 학습하는 동안, 초기 혹은 후기의 layer가 stuck하게 되는 것이다.


<br>
<hr>
<br>


# 16. Rectified Linear Units(ReLU)
### (1) ReLU
  - 0보다 작을 때는 0을 사용하고, 0보다 큰 값에 대해서는 해당 값을 그대로 사용하는 방법이다.
  - f(x) = max(0, x) : 0과 현재 값(x) 중에서 큰 값을 선택한다.

### (2) ReLU의 장점 : Sparsity
  - Sparse activation : 0 이하의 입력에 대해 0을 출력함으로 부분적으로 활성화 시킬 수 있다.
  - Sparse는 벡터 중 0이 많이 들어있다는 것이다. Sparse한 형태가 연산량을 월등히 줄여준다.

### (3) Leaky ReLU
  - ReLU 함수의 변형으로 음수에 대해 1/10로 값을 줄여서 사용하는 함수이다.
  - f(x) = x if x > 0
  
    else ax where 0 <= a <= 1

### (4) Dropout이란?
  - 네트웍의 일부를 생략하는 것이다.


<br>
<hr>
<br>


# 17. Softmax and Cross-Entropy
### (1) Softmax
  - Softmax는 입력 받은 값을 출력으로 0~1 사이의 값으로 모두 정규화 하여 출력 값들의 총합이 1이 되도록 하는 함수이다.
  - 분류하고 싶은 클래스의 수 만큼 출력을 구성하여, 가장 큰 출력 값을 받은 클래스가 확률이 가장 높게 된다.

### (2) 손실 함수(Cost Function)
  - 손실 함수란 신경망이 학습할 수 있도록 해주는 지표이다. 머신러닝 모델의 출력값과 사용자가 원하는 출력값의 차이, 즉 오차를 말한
다. 이 손실 함수 값이 최소화 되도록 하는 가중치와 편향을 찾는 것이 바로 학습이다.
  - 손실 함수로 평균 제곱 오차나 교차 엔트로피 오차를 많이 사용한다.

### (3) 교차 엔트로피 오차
  - E = -∑(k)t(k) * log * y(k)
  - 교차 엔트로피 오차는 기본적으로 분류 문제에서 원-핫 인코딩을 했을 경우에만 사용할 수 있는 오차 계산법이다.
  - 교차 엔트로피 오차는 정답일 때의 모델 값에 자연로그를 계산하는 식이다.
  - 정답에 근접하는 경우에는 오차가 0에 수렴한다. 정답에 멀어지면 멀어질수록 오차가 기하급수적으로 증가한다.

### (4) Softmax and Cross-Entropy
  - 분류 문제에서, 크로스 엔트로피 오차를 사용하고 output에서 softmax 활성화 함수를 사용하는 방법이 많이 쓰인다.


<br>
<hr>
<br>


# 18. Convolutional Neural Networks
 - CNN(Convolutional Neural Network)이란 딥러닝의 일종으로 이미지 분류를 위한 인공지능에서 가장 많이 사용된다.
### (1) CNN 과정

  1) Convolution : Input 이미지에 filter(찾고 싶은 특징)를 sliding window 한다.
  
  2) filter와 이미지의 벡터와 합성곱 한 결과를 통해 Feature map을 찾는다.
  
  3) 피쳐 맵에서 피쳐가 나타나는 대략적인 위치, 빈도를 확인한다.
  
  4) Pooling
  
  5) 각 노드의 컨볼루션 된 스칼라 값들은 비선형 활성화 함수(ReLU, tanh 등)를 통해 다음 레이어로 전달된다.
  
  6) Fully-connected layer : 이전 레이어의 모든 활성화와 완전 연결 된 레이어
  
  7) BP!


<br>
<hr>
<br>


# 19. CNN - Translation Invariance
### (1) 불변성(Invarinace)
  - 이미지에서 고양이 얼굴을 찾는다고 하면, 이미지 내의 어느 위치에 있는지 무관하게 찾을 수 있어야 한다.

### (2) 피처 맵

  1) 입력 이미지는 빨간색, 파란색, 초록색, 검은색 등 여러 채널로 이루어질 수 있다.
  
  2) 입력 이미지가 여러 채널을 갖는 경우 필터는 Sliding windows를 하며 합성곱을 계산한 후, 채널별로 피처맵을 만든다.
  
  3) 각 채널의 피처맵을 합산하여 최종 피처맵을 반환한다.


<br>
<hr>
<br>


# 20. Sub-Sampling(Pooling)
### (1) Pooling이란?
  - 컨볼루셔널 레이어에서 추출된 특징에 Pooling 과정을 거친다.
  - 방법 : Max Pooling, Average Pooling, L2-norm Pooling 등
  - 장점 : 전체 데이터의 사이즈가 줄어서, 연산에 들어가는 컴퓨팅 리소스가 적어진다.
  
	   소실이 발생해서 오버피팅을 방지할 수 있다.

### (2) Max Pooling
  - 맥스 풀링은 피쳐 맵을 M*N의 크기로 잘라낸 후 그 안에서 가장 큰 값을 뽑아내는 방법이다.


<br>
<hr>
<br>


# 21. CNN Hyperparameters
### (1) Hyperparameters
  - 구조 자체, layers 수, 필터 크기, feature map 수, layers간 연결성, 활성화 함수, 최종 supervised layers 등

### (2) Drop-out
  - 오버피팅을 피하기 위해 fully-connected layers에서 자주 사용된다.

### (3) Stride
  - Input Image를 모두 꼭 1 step으로 stride 하지 않아도 된다.

### (4) Zero-padding
  - 피쳐 맵의 크기가 줄어드는 것을 방지한다.
