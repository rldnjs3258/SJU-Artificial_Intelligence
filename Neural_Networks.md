# 1. Neural Networks
 - 생물학적으로 Neural(신경) 시스템과 유사하게 만든 시스템으로, 우리가 알고 있는 가장 강력한 학습 방법이다.
 - 자연의 생물학적인 시스템을 Computational한 모델로 이해하려고 시도했다.
 - 방대한 병렬 계산은 Computational의 효율성을 높였다.
 - 신경 표현의 '분산된' 표현을 이해하는데 도움이 된다.
 - 많은 양의 units들로부터 나타나는 Intelligent behavior이다.

<br>
<hr>
<br>

# 2. Neural Speed Constraints
 - 인간의 Neurons는 몇 밀리 초의 순서로, "Switching time"을 갖고 있다.
 
  (컴퓨터 하드웨어의 나노 초와 비교된다.)
 - 인간의 Neural 시스템은 1/10초 만에 복잡한 인지 작업(시각, 음성 인식 등)을 할 수 있다.
 - 반드시 Massive Paralleism(방대한 병렬계산)을 이용해야 한다.
 - 인간의 뇌에는 약 10^11개의 뉴런이 있으며, 각각 평균 10^4개 연결되어 있다.


<br>
<hr>
<br>



# 3. Neural Network Learning
 - 생물학적 신경 시스템의 학습 방법
 
 (1) Perceptron : 1950년대에 개발 된 단순 신경망. 단일 계층을 학습하기 위한 초기 알고리즘이다.
 
 (2) Backpropagation : 1980년대에 개발 된, 다층 신경 네트워크를 학습하기 위한 복잡한 알고리즘이다.


<br>
<hr>
<br>



# 4. Real Neurons

 (1) 생물학적 뉴런 세포 구조(Cell Structures)
  - 세포체(Cell body)
  - 수상 돌기(Dendrites)
  - Axon
  - Syanptic terminals

 (2) Cell과 Neurons
 
  1) Cell : 근육, 뼈 등을 구성
  
  2) Neurons : 뇌 등을 구성. 정보를 갖고 있다. (Computational!)


<br>
<hr>
<br>


# 5. Neural Communication
 (1) 생물학적 뉴런의 신경 전달 물질
  - 신경 전달 물질은 흥분석 또는 억제성일 수 있다.
  - 흥분 입력(Excitatory input) : Input의 신경 전달 물질이 흥분성이고 threshold를 초과한다면, action potential을 발휘한다.
  - 억제 입력(Inhibitory input)

 (2) Analog와 Digital Communication
 
  1) Analog
   - 정보를 많이 담고 있는 커뮤니케이션 방법이다.
   - 인간의 Neural Net은 memory(정보)를 담고 있는 analog의 커뮤니케이션을 한다.
   - 인공 Neural Net도 analog의 커뮤니케이션을 한다.
   
  2) Digital
   - 컴퓨터에서 정보를 전달하기 좋은 방법이다.


<br>
<hr>
<br>


# 6. Real Neural Learning

 (1) 시냅스 (Synapses)
  - 인간의 Neural Net은 뇌에서 시냅스(Synapses)가 변하며 학습을 한다. 
  - 시냅스는 경험(experience)에 따라 크기와 강도를 변경한다.
  - Synapses는 인공 Neural Net의 Weight와 같은 역할을 한다.

 (2) Hebbian Learning
  - 인간의 뉴런 중 연결 된 두 개의 뉴런이 동시에 firing 할 때, 그들 사이의 시냅스의 강도가 증가한다.
  - 함께 fire하는 뉴런은 연결된다!


<br>
<hr>
<br>


# 7. Artificial Neuron Model
 (1) Artificial Neuron Model
  - 인간의 Neural Net의 구조를 본따서 모델링 한다.
  
  1) Cell : 셀(뉴런)을 노드로 한다.
  
  2) Synaptic connection : 노드 i에서 j로 갈 때, wji를 가중치(syanptic connectionc)로 하여 연결한다.
  
  3) 학습을 하며 Weight가 바뀐다.
  
  4) 각각의 weights들을 sum 하여 output을 구한다.

 (2) Artificial Neuron Model의 셀에 input
 
  - net(j) = ∑(i) w(ji)o(i)

 (3) Artificial Neuron Model의 셀 output
 
  - T(j)는 유닛 j에 대한 threshold이다.
  
    o(j) = 0 if net(j) < T(j)
    
    o(j) = 1 if net(i) >= T(j)



<br>
<hr>
<br>

# 8. Neural Computation
 - McCollough와 Pitts(1943)는 Artificial Neuron Model이 어떻게 논리적 함수를 계산하는지를 보였다.
 
 (1) 논리 게이트 : 시뮬레이션 해보기
  - AND : 모든 wji를 Tj/n이라고 둘 때, n은 input의 갯수이다.
  - OR : 모든 wji가 Tj가 되게 한다.
  - NOT : threshold를 0으로 설정하고, 단일 입력에 음수 weight를 준다.
  - 음수 입력과 AND-OR의 2 layer network를 사용하면 모든 boolean 함수를 계산할 수 있다.

 (2) 논리 게이트 : 응용 영역
  - 임의의 논리 회로 (arbitrary logic circuits)
  - 순차적 기계 (sequential machines)
  - computers


<br>
<hr>
<br>


# 9. Perceptron Training

 1) Supervised training 예제가 주어졌다고 가정한다.
 
  - Input에 대한 Output의 라벨을 안 채로 학습한다.
  
 2) 각 Unit이 각 예제에 대해 정확한 라벨을 출력할 수 있도록, 시냅스 가중치를 배운다.
 
 3) 퍼셉트론은 반복 업데이트 알고리즘을 통해 올바른 가중치를 학습시킬 수 있도록 조정한다.


<br>
<hr>
<br>


# 10. Perceptron Learning Rule
 (1) 가중치 업데이트
 
  - w(ji) = w(ji) + η(t(j) - o(j)) * o(i)
  
  - η은 'Learning Rate'이다.
  
  - t(j)는 유닛 j에 대해 학습된 출력 라벨이다.

 (2) 규칙
  - output이 원하던 값과 정확히 일치한다면 그대로 둔다.
  - output이 높으면, active inputs의 가중치를 낮춘다.
  - output이 낮으면, active inputs의 가중치를 높인다.

 (3) threshold 조정
  - T(j) = Y(j) - η(t(j) - o(j))
  - 보완하기 위해 임계 값을 조정한다.

 (4) Hyper parameter
  - Learning rate : 학습율. 가중치가 업데이트 될 때 조정되는 비율이다.
  - Threshold
  - Epoch : 각 자료가 몇 번 학습될 것인가 설정한다.



<br>
<hr>
<br>


# 11. Perceptron Learning Algorithm
 - output이 원하던 값과 정확히 수렴할 때 까지 반복적으로 가중치를 업데이트 한다.
 
 ```python
 Initialize weights to random values
 Until outputs of all training examples are correct
	For each training pair, E, do:
		Compute current output o(j) for E given its inputs
		Compute current output to target value, t(j), for E
		Update synaptic weights and threshold using learning rule
```


<br>
<hr>
<br>


# 12. Perceptron as a Linear Separator
 - 퍼셉트론은 Linear threshold function(선형 임계 값 함수)를 사용하여 클래스를 구별하는 linear separator를 찾는다.
 - w(12)o(2) + w(13)o(3) > T1
 
   o(3) > -w(12)/w(13) * o(2) + T1 / w(13)
   
   또는 n차원 공간에서의 ★초평면(hyperplane)!
 - 초평면 : 초평면은 n차원에서 class들을 분류하는 n-1차원의 subspace이다.


<br>
<hr>
<br>


# 13. Concept Perceptron Cannot Learn
 - Perceptron은 Exclusive-or과 Parity 함수를 학습할 수 없다.
 - Exclusive-or(XOR) : x1과 x2 중 어느 한쪽이 1일 때만 1을 출력한다.
 - Parity 함수 : 입력패턴이 홀수 개의 1을 포함한 경우에만 1을 출력한다.



<br>
<hr>
<br>


# 14. Perceptron Limits
 - 시스템을 통해 '분명히 표현하지 못하는' 개념을 학습하지 못한다.
 - Minksy와 Papert(1969)는 퍼셉트론을 분석하여 퍼셉트론이 학습하지 못하는 많은 기능에 대해 책을 썼다.
 - 퍼셉트론을 사용할 수 있는 분야가 적다는 결론이 도출되며 이 시기에는 신경망에 대한 추가 연구가 이루어지지 않았다.
 - 전문가 시스템(Expert System)이 발전하며 다시 인공지능의 관심도가 급증하게 된다!


<br>
<hr>
<br>


# 15. Perceptron as Hill Climbing
 (1) 개념
  - hypothesis space : input에 대한 output을 실제 값과 가장 비슷하게 만들 수 있도록 돕는 가상 공간이다. 
  
    가상 공간은 Weights와 threshold의 세트로 이루어져 있다.
  - Perceptron의 목표 : Training set의 분류 오류를 최소화 하는 것

 (2) Perceptron as Hill Climbing
  - Hill-climbing(Gradient Descent) : 퍼셉트론은 hypothesis space에서 힐-클라이밍을 수행하며 Training set의 오류를 줄이기 위해,
  
    Backpropagate를 통해 조금씩 weights를 변경한다.
  - 단일 뉴런 모델의 경우, 공간은 single-minima로 잘 동작한다.
  - 일정 횟수 이상의 학습에서는 성능이 더 안 좋아지기도 한다!


<br>
<hr>
<br>


# 16. Multi-Layer Networks
 - 일반적인 Multi-Layer Networks는 Input Layer - Hidden Layer - Output Layer로 구성되어 있다.
 
   딥러닝은 Hidden Layer의 수가 2개 이상인 것이다!
 - 각 레이어는 다음 레이어와 완전히 연결(fully-connected)되어 있으며, activation 함수를 통해 다음 레이어로 전달된다.
 - Weights(가중치)를 통해 계산 값이 결정 된다. 임의의 수의 hidden units가 주어질 때, 모든 boolean 함수는 단일 hidden layer를 통해 계산될 수 있다.


<br>
<hr>
<br>


# 17. Differentiable Output Function
 (1) 배경 지식
  - 딥러닝 네트워크에서는 노드에 들어오는 값을 바로 다음 레이어로 전달하지 않고, 활성화 함수로 비선형 함수를 통과시킨 후 전달한다.
  - 비선형 함수를 사용하는 이유는, 선형함수를 사용할 시 층을 깊게 하는 의미가 줄어들기 때문이다!

 (2) Multi-Layer 'Linear' Networks와 활성화 함수
  - Multi-Layer 'Linear' Networks는 선형 네트워크이다. 하지만 출력은 Non-linear 함수를 통해 출력해야 한다!
  - 시그모이드 함수 (Sigmoid) : Logistic 함수라 불리며, 선형인 멀티퍼셉트론에서 비선형 값을 얻기 위해 사용하기 시작했다.
  
    O(j) = 1 / (1+e^-(net(j) - T(j)))
  - 비선형 값을 얻기 위해 Sigmoid 뿐 아니라, tanh 혹은 Gaussian output을 쓸 수도 있다.


<br>
<hr>
<br>


# 18. Gradient Descent
 - 오류를 최소화하기 위한 정의 : E(W) = ∑(d∈D)∑(k∈K)(t(kd) - O(kd))^2
 
   D : Training set
   
   K : Output set
   
   t(kd) : d 예제의 k 유닛에 대한 지도된 출력값
   
   O(kd) : d 예제의 k 유닛에 대한 예측값
 - 입력에 대한 시그모이드 단위 미분 : ∂o(j) / ∂net(j) = o(j)(1-o(j))
 - 오류를 최소화하기 위해 가중치를 변경하는 학습 규칙 : △w(ji) = -η * ∂E / ∂w(ji)
 - Gradient Descent를 통해 weight를 변경한다.


<br>
<hr>
<br>


# 19. Backpropagation Learning Rule
 - 각 Weight는 다음의 규칙에 의해 변경된다.
 
   △w(ji) = ηδ(j)o(i)
   
   δ(j) = o(j)(1-o(j))(t(j) - o(j)), if j가 output 유닛인 경우
   
   δ(j) = o(j)(1-o(j))∑(k)δ(k)w(kj), if j가 hidden 유닛인 경우
 - η는 Learning rate라고 하는 상수이다.
 
   t(j)는 유닛 j에 대한 올바른 출력 값이다
   
   δ(j)는 유닛 j에 대한 오차 척도이다.



<br>
<hr>
<br>


# 20. Error Backpropagation
 (1) Backpropagation 과정
 
  1) Output 유닛의 오류를 계산하고, 이를 이용하여 그 윗 hidden layer 까지의 weights를 변경한다.
   - Current output : o(j) = 0.2
   - Correct output : t(j) = 1.0
   - Error δ(j) = o(j)(1-o(j))(t(j)-o(j)) = 0.2(1-0.2)(1-0.2) = 0.128
   - j에 Weights Update : △w(ji) = ηδ(j)o(i)

  2) Output 유닛의 오류를 통해 Hidden 유닛의 오류를 계산한다.
   - δ(j) = o(j)(1-o(j))∑(k)δ(k)w(kj)

  3) Hidden 유닛의 오류를 통해, 그 윗 Input layer 까지의 weights를 변경한다.
   - δ(j) = o(j)(1-o(j))∑(k)δ(k)w(kj)
   - j에 Weights Update : △w(ji) = ηδ(j)o(i)

 (2) Spiking Neural Network
  - 스파이킹 인공 신경망과 일반 인공 신경망의 가장 큰 차이는 시간 축이 존재한다는 것이다.
  - 뉴런 별로 한 번씩 이전 뉴런들의 값을 받아오며, '시간'에 따라 뉴런의 값이 지속적으로 변한다.


<br>
<hr>
<br>


# 21. Backpropagation Training Algorithm
 - Hidden layer(H)를 포함한 3 layer network를 full connectivity 하게 생성한다.
 - 가중치는 임의의 작은 실수 값으로 설정한다.
 
 ```python
 모든 training examples가 correct value에 다다르거나(within ε), 혹은 mean squared error가 감소하거나, 혹은 다른 종료 기준에 다다를 때 까지 :
	Begin epoch
	For 각 training example, d, do:
		d의 인풋 값에 따른 예측 값 계산
		d의 정답 값과 예측 값 사이의 에러 계산
		Backpropagating error와, learning rule에 따라 Weights 업데이트
	End epoch
```


<br>
<hr>
<br>


# 22. Comments on Training Algorithm
 - 오류가 0으로 수렴된다고 꼭 보장되지 않는다. local optima로 빠지거나, 발산할 수 있다.
 - 실제로는, 이 알고리즘을 통해 계산한 많은 대형 네트워크와 실제 데이터에서 낮은 오류를 수렴했다.
 - 큰 네트워크의 경우, 여러 epochs(수 천번!)이 필요할 수 있다.
 - local-minima 문제를 피하려면, 초기 가중치를 랜덤하게 설정해서 임의로 몇 번 실행 해보며 시험해 본다.
 
   Training set에서 오류가 가장 적게 나온 것의 결과를 취한다!
   
   여러 번의 시도를 통해 결과를 구성한다. (Training set 정확도에 따라 가중치를 부여 할 수도 있다.)
