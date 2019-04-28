# 1. Learning
 - Unknown 환경에서는 Learning이 필수적이다.
 - Learning은 시스템을 구축하는 방법으로서 유용하다. (노트로만 구상한 agent를 실제로 만들 수 있게 해준다!)
 - Learning은 agent의 의사 결정 메커니즘을 수정해서, 성능을 향상시킨다.

<br>
<hr>
<br>

# 2. Learning agents
 1) Sensors : Critic을 받아드린다.
 2) Performance element(학습 모델)
  - Learning element 지식을 이용하고, Learning element의 영향을 받아서 Performance element가 바뀐다.
  - Learning element를 실행 중에 Learning goal에 다다르면 Problem generator를 실행시켜 Performance element에 대한 실험을 진행한다.
 3) Effectors
 4) Environment


<br>
<hr>
<br>

# 3. Learning element
 (1) 학습 요소 설계
  - 학습 요소의 설계는 다음과 같이 이루어 진다.
  1) Performance element(학습 모델) : 어떤 Performance element을 사용할 것인가.
  2) Component : 어떤 Functional Component로 학습 할 것인가.
  3) Representation : 데이터를 어떻게 표현 할 것인가. (선형? Neural net? 등)
  4) 어떤 피드백을 줄 것인가.

 (2) Example scenarios
 
| Performance element(학습 모델) |	Component |		Representation(데이터 표현 방법) |	Feedback |
|---|:---:|---:|---:|
| Alpha-beta search |		Eval.fn |			Weighted linear function |		Win/loss |
| Logical agent		| 	Transition model	| Successor-state axioms		| 	Outcome |
| Utility-based agent	|	Transition model |	Dynamic Byes net		| 	Outcome |
| Simple reflex agent	|	Percept-action fn |	neural net		|		Correct action |

 (3) Learning의 종류
  1) Supervised learning
   - 정답을 알려주며 학습시키는 것.
   - input data로 고양이 사진을 주고, 사진이 고양이라고 label을 알려준다.
  2) Unsupervised learning
   - 정답을 알려주지 않고, 비슷한 데이터들을 군집화 하는 것이다.
  3) Semi-supervised learning
   - 정답을 알려준 데이터와 정답을 알려주지 않은 데이터를 동시에 사용해서 학습시킨다.
  4) Reinforcement learning
   - 지도를 하고, 상과 벌이라는 보상(reward)으로 피드백으로 주며 강화시키는 것.
   - 현재 좋은 학습 방법 중 하나이다.

 (4) 예제
  - 날씨에 따라 테니스를 칠 수 있는지 학습시켜보는 예제이다.
  - 학습 방법 : Supervised learning
  
    Performance element : 데이터를 이용해서 Decision Tree 모델로 학습시켰다.
    
    Component : Decision Tree의 내부 함수가 동작해 데이터를 분석했다.
    
    Representation : 데이터를 트리 모양으로 표현했다.
    
    Feedback : 학습시킨 모델의 input에 대한 output으로 outcome을 확인할 수 있었다.


<br>
<hr>
<br>

# 4. Inductive learning (a.k.a Science)
 (1) Inductive learning(귀납적 학습)
  - 귀납적 학습은 사례가 먼저 나오고 이를 토대로 정의나 원리를 스스로 찾는 방법이다.
  - 귀납적 머신러닝에서 모델은 관측된 사례의 집합에서 예제로 학습하여 일반화된 결론을 도출한다.
  - 예를 들어, 화재로 인한 사고나 이미지를 '위험한'것으로 교육시키면, 아이들은 예제를 통해 배우고 불을 피우지 않는다.

 (2) Inductive learning 방법
  - f는 정확한 target 함수로서, 학습해야 할 정의 혹은 원리이다.
  - h는 주어진 데이터를 통해 학습해서, f 함수와 최대한 비슷하게 만든 모델이다.
  1) 주어진 데이터를 최대한 잘 설명할 수 있는 함수인, Hypothesis(h)를 찾는 것이 목표이다.
  2) h = f(x)
  3) 주어진 training set을 통해 h를 찾는다.

 (3) Inductive learning 가정
  - 사전 지식은 무시한다.
  - 경정론적이고, 관찰 가능한 environment(환경)이다.
  - 예제가 주어졌다고 가정한다.
  - agent가 f에 대해 배우고 싶어한다고 가정한다.


<br>
<hr>
<br>

# 5. Inductive learning method
 (1) Inductive learning 예제
  - h를 최대한 잘 정의 해서 f(x)와 비슷하게 만든다.
  - h의 그래프가 그리는 방향성이, f(x)의 그래프가 그리는 방향성과 일치한다면 h는 잘 설정된 것이다.

 (2) Inductive learning의 다양한 결과
  1) 훈련이 잘 된 경우
   - Training set에 따라 h가 일반적인 방향성을 잘 그린다.

  2) Overfitting
   - Training set이 너무 많이 학습되어, h가 일반적인 추론을 할 수 있는게 아닌 Training set의 데이터만 잘 찾을 수 있게 된다.

  3) Underfitting
   - h가 Training se에 잘 학습 되지 않았다.

 (3) Inductive learning 문제점 해결
  - Ockham's Razor(오컴의 면도날) 방법을 이용한다. 복잡한 모델 보다는 단순한 모델을 선택해서 과적합(Overfitting)을 피한다.
  
    비선형 모델 보다는 선형 모델을 선호한다.


<br>
<hr>
<br>

# 6. Attribute-based representations
 - 예제는 속성의 상황(Boolean, discrete, continuous)에 따라 사람들이 식당의 테이블을 기다린지, 기다리지 않은지에 대한 데이터이다.
 - Alternate, Bar, Fri/Sat, Hunngry, Patrons, Price, Rain, Res, 식당 종류, Est에 따라 Target인 기다린지, 기다리지 않은지에 대한 정보가 들어 있다.
 - 이 예제는 Target을 positive(T) 혹은 negative(F)로 분류(Classification)한다.


<br>
<hr>
<br>

# 7. Decision trees
 - hypotheses를 찾아가는 알고리즘 중 하나이다.
 - 예제는 앞에 나온 기다릴지 기다리지 않을지에 대한 데이터를 Decision Tree로 나타낸 것이다.
 
   각 속성의 상황(Boolean, discrete, continuous)에 따라 T와 F를 분류(Classification)해 가면서 최종 Decision을 내린다.


<br>
<hr>
<br>

# 8. Expressiveness
 - 의사 결정 트리는 입력 속성의 상황(Boolean, discrete, continuous)들을 전부 트리로 표현해낼 수 있다.
 
  ex) 속성이 Boolean인 경우 T와 F를 통해 leaf 노드까지 도달할 수 있다.
 - 모든 training set에 대해 일관적인 결정을 내리는 의사결정 트리가 있는 경우, 각 training set에 대해 leaf node까지 하나의 경로 씩이 있을 것이다.
 
각 training set의 예제들은 기존의 트리의 흐름에 따라 leaf node까지 갈 것이다. (새로운 흐름을 만들어 내지 않는다!)
 - 탄탄하고 조밀한 의사결정 트리가 선호 된다.


<br>
<hr>
<br>

# 9. Hypothesis spaces
 (1) Boolean 속성의 개수와 Decision tree의 노드 수
  - Boolean 속성이 n개일 때, Decision tree의 노드는 총 몇개일까?
   = Boolean 함수의 수
   = 2^n개의 행을 갖는 Truth table의 수 = 2^2n
  ex) 6개의 Boolean 속성이 있는 경우 18,446,744,073,709,551,616개의 노드를 가진 트리가 생성된다.

 (2) Hypothesis와 논리곱
  - Hungry라는 속성과 Rain이라는 속성t은 in(True인 경우), in(False인 경우), Out 세 개의 결과를 가진다.
  
    이때 논리곱은 3^n이다.

 (3) Hypothesis space
  - Hypothesis space는 찾고자 하는 function들의 set으로 한정시켜 세팅하는 것이다.
  - Hypothesis space를 가정하면 target 함수가 expressed 될 확률이 증가한다.
  - 일관된 training set을 구성해서 Hypothesis의 수를 늘릴 수 있다. (예측이 나빠질 수도 있다!)


<br>
<hr>
<br>

# 10. Decision tree learning 알고리즘
 - 목표 : training set의 예제를 포함하고 있는 small tree를 찾기
 - Idea : 가장 중요한 속성을 재귀적으로 계속 선택해 나가며 sub tree의 루트 노드로 선택한다.
 
 ```C
function DTL(examples, attributes, default) returns a decision tree
	if examples is empty then return default
	else if all examples have the same classification then return the classification
	else if attrubutes is empty then return MODE(examples)
	else
		best <- CHOOSE-ATTRIBUTE(attributes, examples)
		tree <- a new decision tree with root test best
		for each value vi of best do
			examplesi <- {elements of examples with best = vi}
			subtree <- DTL(examplesi, attributes - best, MODE(examples))
			add a branch to tree with label vi and subtree subtree
		return tree
```

<br>
<hr>
<br>

# 11. Choosing an attribute
 - Decision tree를 구성하는 속성들을 '좋은 속성'으로 구성하는 것도 중요하다.
 - Idea : 좋은 속성은 예제를 'Positive' 혹은 'Negative'중 하나로 분류한다.
 - 예제는 Patrons 속성과 Type 속성의 예제인데, Patrons는 None/Some/Full중 하나로 분류하고, Type은 French/Italian/Thai/Burger중 하나로 분
류한다. 이 둘 중 Patrons 속성이 더 좋다.


<br>
<hr>
<br>

# 12. Information
 - 정보를 통해 질문에 대한 답을 한다.
 - Answer이 clueless인 경우, Answer는 더 많은 정보를 포함하고 있다.
 - Scale : Boolean의 질문에 대한 답변으로 <0.5, 0.5>를 이용한 경우 1 bit이다.
 - Entropy : <P1, ..., Pn>의 Answer에 들어 있는 정보는 H(<P1, ... Pn>) = ∑(i=1, n) - Pi*log2*Pi이다.


<br>
<hr>
<br>

# 13. Information Contd.
 - 루트에서 p가 양수이고, n이 음수가 아닌 예제가 있을 때 새로운 예제를 분류하기 위해서는 H(<p/p+n), n/(p+n)>) 비트가 필요하다.
 
  ex) 12개의 레스토랑 예제에서, p = n = 6이므로 1 비트가 필요하다.
 - 속성은 예제E를 부분 집합 Ei로 나눈다. 각 부분의 집합 Ei는 classification을 하는데 더 적은 정보가 필요하다.
 - Ei에 양수 pi, 음수 ni의 예제가 있을 때 새 예제를 분류하는 데 필요한 비트는 H<(pi/(pi+ni), ni/(pi+ni)>)이다.
 
   모든 가지에 대해서는 ∑i (Pi+ni)/(p+n)H<(pi/(pi+ni), ni/(pi+ni)>)의 비트가 필요하다.
 - 속성 Patrons의 예제는 0.459 bits가 필요하고, 속성 Type 예제는 1 bit가 필요하다. 추가적으로 필요한 정보를 최소화하는 속성을 선택한다!


<br>
<hr>
<br>

# 14. Example contd.
 - 예제는 Decision tree가 12개의 example을 통해 학습을 하는 것이다.
 - 예제는 단순한 트리의 모습을 하고 있는데, 복잡한 hypothesis의 경우 적은 양의 데이터로는 정의되지 않는다.


<br>
<hr>
<br>

# 15. Performance measurement
 - h = f를 어떻게 확인할 수 있을까? (f는 target 함수이고, h는 주어진 데이터를 통해 학습시켜 f와 최대한 비슷하게 만든 함수이다.)
  1) 계산/통계 학습의 이론을 이용
  2) h에 새로운 예제인 test set를 적용해 본다.
 - Training set의 크기에 따른 test set의 정답률로 Learning curve를 그려서 학습률을 볼 수 있다.


<br>
<hr>
<br>

# 16. Performance measurement contd.
 (1) 학습 곡선 종류
  1) realizable
   - 이 학습 곡선은 Training set의 크기에 따라 정답률이 크게 올라가 일정 부분에서 수렴하는 모습이다.
   - 이 학습 곡선의 hypothesis는 target function을 실현할 수 있다.

  2) non-realizable
   - 이 학습 곡선은 Training set의 크기에 따라 정답률이 올라가지만 수렴하는 지점이 낮다.
   - 이 학습 곡선의 hypothesis는 속성을 몇개 누락했을 수 있다.
   - 이 학습 곡선의 hypothesis는 제한된 클래스 일 수 있다. (임계값이 있는 선형함수 등)

  3) redundant
   - 이 학습 곡선은 Training set의 크기에 따라 정답률이 천천히 일정하게 올라간다.
   - 이 학습 곡선은 관련 없는 속성들을 이용했을 수 있다.


<br>
<hr>
<br>

# 17. Summary
 - Unknown environments나 lazy 설계자의 경우 Learning이 필요하다.
 - Learning agent = Performance element + learning element
 - Learning method는 Performance element, 사용한 feedback, component, representation의 유형에 따라 성능이 다르다.
 - Supervised learning의 목적은 training example과 비슷한 hypothesis를 찾는 것이다. 
 - Decision tree는 획득한 정보를 통해 학습한다.
 - Learning performance = Test set에서 측정 된 예측의 정확도
