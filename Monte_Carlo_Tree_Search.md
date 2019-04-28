# 1. Heuristic Search
 - Heuristic Search나 Informed Search는 Goal 노드로 확장하기 위해 추가적인 지식을 활용한다.
 - Heuristic 함수인 H(n)은 노드에서 목표까지의 최단의 경로 cost를 예측한다. 노드가 Goal 노드와 같을 경우 0이다.
 
   ex) 도로 탐색 문제에서 현재 위치에서 목표 위치까지의 '직선' 거리
 - 대부분의 Search 문제는 NP-complete 이므로, 최악의 경우에는 시간 복잡성이 기하 급수적일 수 있다.
 - 좋은 Heuristic이란?
  1) Average problem에 대해 효율적인 해결방법을 찾는다.
  2) 최적이 아니더라도, 합리적으로 좋은 솔루션을 찾는다.

<br>
<hr>
<br>

# 2. Beam Search
 (1) Beam Search란?
  - Beam Search는 Best-First Search에서 기억 노드의 수를 제한하는 방법이다.
  - Best-First  Search는 '최적해'를 구하려 한다면, Beam Search는 '그럭저럭'한 해를 구하려 한다.

 (2) Beam Search 장단점
  - '기억하는 공간'을 축소시키는데 좋다.
  - '검색'에 초점을 맞춘다.
  - 가지치기가 지나치게 빠르고, 해를 제거할 가능성도 있다.

 (3) Beam Search 방법
  1) Best-First Search를 이용한다.
  2) 아직 확장하지 않은 노드를 Goal에 가까운 순서대로 Queue에 정렬한다.
  3) Queue에 사전에 설정된 수만큼만 유지하고, 나머지는 잘라낸다.


<br>
<hr>
<br>

# 3. Hill-Climbing
 - Hill-Climbing은 Beam search의 beam-width를 1로 설정한 것이다.
 - 현재 노드와 확장할 노드와의 cost를 계산해서 sort한 후에, 각 확장 노드 선택을 평가한다.
 
   현재 노드에서 가장 좋은 확장 노드를 고른다.
 1) maxima : Global Maximum에 도달하지 못하고 Local Maximum에 갇힐 우려가 있다.
 2) plateaus(평지) : 평평한 곳에 머물러 있으며 어디로 이동할 지 판단 못한다.
 3) ridges(산등성이) : 산등성이인 경우 최적해 혹은 최적해로 오해하는 경우이다.


<br>
<hr>
<br>

# 4. Conventional Game Tree Search
 (1) Perfect-information games
  - 전략적으로 상대가 취한 행동을 관찰할 수 있는 게임이다.
  
    즉, 상대의 수를 볼 수 있는 게임이다.
  - 게임에서 모든 좌표로 뻗어나갈 수 있다.
  - 바둑, 체스, 빙고 등

 (2) Minimax algorithm with alpha-beta pruning
  - Minimax algorithm이란 '상대가 던진 최악의 수 중, 내게 가장 최선이 되는 수'를 고르기 위한 알고리즘이다.
  - 인공지능은 3수, 6수, 1000가지, 10000가지 상황을 내다본다. 이 중 불필요한 연산을 가지치듯 버리는 알고리즘이 알파-베타 가지
치기(Alpha-beta pruning)이다.
  - 이 알고리즘을 위한 좋은 Heuristic 함수가 있다.
  - 가능한 포지션(branching factor)를 조절하는 것이다.


<br>
<hr>
<br>

# 5. Go
 - alpha-beta의 초급~중급 수준이다.
 - 가능한 포지션(branching factor)이 굉장히 많다.
 
    돌 하나가 움직일 때마다 상대방은 250개의 가능한 포지션(branching factor)가 발생한다.
    
    Chess는 35개 정도의 branching factor가 발생한다.
 - Go를 평가하기 위한 좋은 평가 함수가 부족한 상태이다.
 
   바둑은 너무 미묘한 작업을 요구한다. '비슷한 위치'에 놔도 완전히 다른 결과를 가져올 수 있다.


<br>
<hr>
<br>

# 6. Monte Carlo
 - 몬테 카를로 알고리즘은 난수를 이용하여 함수의 값을 확률적으로 계산하는 random sampling의 알고리즘이다.
 - 몬테 카를로 알고리즘은 컴퓨터 바둑 게임에서 혁명을 일으켰다.
 
   이 알고리즘은 deterministic games에 적용되었다. (10년 미만)
 - 게임의 영역 뿐 아닌 컴퓨터 모의 실험, 영상 등의 영역에서도 폭발적인 관심을 불러 일으켰다.
 - 기획, 모션 계획, 최적화, 재무, 에너지 관리
 - Monte Carlo를 이용해 알파고의 알고리즘을 구현했다.


<br>
<hr>
<br>

# 7. MCTS for computer Go and MineSweeper

 (1) 바둑 : Deterministic transitions(결정론적 이동)
 
 (2) MineSweeper(지뢰찾기) : Probabilistic transition(확률적 이동)


<br>
<hr>
<br>

# 8. Basic Monte Carlo Simulation
 - 평가 함수가 없다면, 아래의 방법을 평가 함수로 사용하여 이겼던/졌던 방법을 잘 기록해 나간다.
  1) 랜덤으로 움직여 게임을 시뮬레이션 한다.
  2) 게임의 끝에 스코어를 기록한다. 계속 기록을 이겨 나간다.
  3) 가장 자주 이겼던 방식 대로 플레이 한다.
  4) 반복


<br>
<hr>
<br>

# 9. Basic Monte Carlo Search
 (1) 몬테 카를로 알고리즘이란?
  - 몬테 카를로 알고리즘은 난수를 이용해 확률적인 계산을 하는 알고리즘이다.
  ex) 원의 넓이를 구할 때, 원과 원을 외접하는 정사각형을 그리고 그 위에 임위의 점을 막 생성한다. 그리고 전체 찍힌 점 중 원 위에
찍힌 점의 비율을 구하면 확률적으로 원의 넓이를 대략적으로 구할 수 있다.
  ex) 바둑 게임을 구현할 때, 이 알고리즘으로 컴퓨터가 둘 수 있는 각각의 수에 대해 랜덤으로 막 둬 본다. 그리고 그 중 승률이 높은
곳을 고른다.

 (2) 몬테 카를로 알고리즘 방법
  1) Selection
   - 현재 트리 중 어떤 노드를 골라서 타고 가장 아래까지 내려간다.
  2) Expansion
   - 고른 노드에 대해 자식 노드를 만든다.
  3) Simulation(Play-out)
   - 자식 노드에 대해 random simulation 해서 게임을 진행한다.
  4) Backpropagation
   - Simulation 결과를 root 노드에 전달한다.
  5) Outcomes
   - 앞의 1)부터 4)를 반복해서, Simulation 한 Outcomes들 중 승률이 높았던 방법을 고른다.


<br>
<hr>
<br>

# 10. Monte Carlo Tree Search
 - MCTS는 통계트리를 구축해서 전체 게임 트리에 부분적으로 매핑된다.
 - MCTS는 통계트리를 통해 AI가 전체 게임 트리 중 일부 노드에 집중할 수 있도록 도와준다.
 - 시뮬레이션을 통해 노드의 값을 구한다.


<br>
<hr>
<br>

# 11. Naive Approch
 - 시뮬레이션을 평가함수의 aB로 이용해서 평가한다.
 - 문제점
  1) 시뮬레이션을 한 번 실행하는 것은 좋지 않다. 오직 하나의 0/1 신호만 얻게 된다.
  2) 평가 한 번 하기 위해, 굉장히 많은 시뮬레이션을 실행하는 것도 좋지 않다. 아주 느리기 때문이다.
   ex) 체스 프로그램은 1초에 백만 번의 평가를 할 수 있다.
   
       바둑 프로그램은 1백만 moves/sec, 400 moves/simulation, 100 simulation/eval이다. 즉, 1초에 25번만 평가 할 수 있다.
 - 이러한 문제점 때문에 Monte Carlo는 바둑의 영역에서 10년 이상 무시당해왔다.


<br>
<hr>
<br>

# 12. Monte Carlo Tree Search
 (1) MCTS와 게임 트리
  - MCTS의 시뮬레이션 결과들을 통해서 승률이 높았던 방법을 고르고, 게임 트리를 성장시키자!

 (2) Exploitation과 Exploration
  - Exploitation(착취) : 가능성이 있는 곳으로의 움직임에 집중한다.
  
    Exploration(탐험) : 불확실성이 높은 곳으로의 움직임에 집중한다.
  - 착취와 탐험이라는 두 가지 Goal은 모순되어 보인다.
  
    Bandit 알고리즘을 통해 자세히 이해할 수 있다.


<br>
<hr>
<br>

# 13. Multi-Armed Bandit Problem
 - 카지노에 여러 대의 슬롯 머신이 있다고 하자. 슬롯 머신들 중 어느 슬롯 머신이 돈을 가장 많이 줄까?
 (1) Assumptions
  - 여러 슬롯 머신들을 고를 수 있다.
  - 슬롯 머신의 레버를 당기는 각 행동들은 독립적이다.
  - 슬롯 머신들은 '고정된, 알려지지 않은' payoff를 한다.


<br>
<hr>
<br>

# 14. Consider a row of three slot machines
 - 슬롯 머신의 레버를 당길 때 마다 Win 혹은 Loss를 한다.
 
   Win : payoff 1
   
   Loss : payoff 0
 - A, B, C 슬롯 머신들의 승률은 각각 다음과 같다. 하지만 우리는 그걸 알지 못하는 상태이다.
 
   P(A wins) = 60%
   
   P(B wins) = 55%
   
   P(C wins) = 40%


<br>
<hr>
<br>

# 15. Exploration vs. Exploitation
 (1) Exploration(탐구)
  - 모든 슬롯 머신들을 탐구하고 싶다.
  - 하지만 탐구를 너무 많이 하면, 현재 가지고 있는 돈을 많이 잃을 수 있다.

 (2) Exploitation(착취)
  - 가능성 있는 슬롯 머신들 위주로 이용하고 싶다.
  - 너무 Exploit 위주로 하면, 최적화된 값을 얻지 못하고 sub-optimal 값에 갇힐 수 있다.

 (3) 결론
  - non-optimal 슬롯 머신을 이용하면서 생기는 손실을 최소화 해야 한다. 
  - exploration과 exploitation 사이의 균형이 필요하다.


<br>
<hr>
<br>

# 16. How do we determine best arm to play?
 (1) Policy
  - time step t에서 슬롯 머신을 고르기 위한 전략
  - t번째 선택 이전의 1, 2 ... t-1번의 시도 동안 선택했던 슬롯 머신과 그 결과를 활용한다.

 (2) Policy 종류
  1) Uninform policy
   - 최소로 이용한 슬롯 머신을 이용한다. ties를 랜덤하게 끊는다.
  2) Greedy
   - 경험적으로 가장 높은 payoff를 줬던 슬롯 머신을 이용한다.


<br>
<hr>
<br>

# 17. Upper Confidence Bound
 (1) UCB1(Upper Confidence Bounds)
  - MCTS의 UCB1알고리즘은 특별한 방법을 통해 계산식의 값이 가장 큰 것을 selection하게 해 준다.

 (2) Policy
  1) 각 슬롯 머신을 한 번씩 시도한다.
  2) 각 time step에서 UCB를 최대화 하는 슬롯머신을 고른다.

 (3) UCB 식
  - vi + C*((sqtr)(ln(N)/ni))
  
    vi : 추정 값
    
    C : 수정할 수 있는 파라미터
    
    N : 총 시도한 횟수
    
    ni : 슬롯머신 i를 시도한 횟수


<br>
<hr>
<br>

# 18. UCB Intuition
 - UCB 식을 최대화 할 수 있는 슬롯머신을 고른다.
 - Exploit : 추정 값(vi)이 reward를 많이 얻을 수록 좋다.
 - True value가 vi 주변의 confidence 구간에 있을 것으로 기대된다.


<br>
<hr>
<br>

# 19. UCB Intuition
 - 슬롯머신 i를 시도한 횟수인 ni가 적을 수록 Confidence 구간이 커진다. 
 
   (sqrt)ni의 비율로 축소한다.
   
   이동에 대한 불확실성이 높을수록 exploration 기간이 더 길어진다.
   
 - 총 trials 수 보다 훨씬 적은 시도를 했다면 children을 더 탐험해야 한다.


<br>
<hr>
<br>

# 20. UCB1의 이론적 성질
 (1) 이론적 성질
  - 각기 다른 bandit 알고리즘과 그 속성에 대한 많은 논문들이 있다.

 (2) 주요 문제
  - Main question : 최적화 된 머신러닝을 찾는 속도
  - 일반적인 Goal : n번의 시도에 대한 regret O(logn)

 (3) 점근적 분석
  - 많은 문제들을 해결할 때 이 방법보다 더 좋은 점근적 분석은 없다. (Lai and Robbins 1985)
  - UCB1은 많은 입력 분포들에 대해 점근선을 달성하는 간단한 알고리즘이다.


<br>
<hr>
<br>

# 21. The case of Trees : From UCB to UCT
 (1) UCB
  - UCB는 단 하나의 decision만을 내린다.
  - 그렇다면 게임계획과 같은 여러 decision을 내려야 할 때는 어떻게 할까?
  
    look-ahead tree를 이용하라!

 (2) UCT(Upper Confidence Bounds for Trees)
  - UCB를 기반으로 만든 알고리즘이다.

 (3) 시나리오
  - Single Agent : 단일 agent가 모든 planning과 action을 컨트롤한다.
  - Adversarial(적대적) : 게임이나 분석에서의 최악의 상황 등
  - Probabilistic(확률론적) : 일반적인 경우, '중립적인' 환경이다.


<br>
<hr>
<br>

# 22. Bandits to Games
 - Bandit arm : 게임에서의 move
 - Payoff : move의 퀄리티
 - Regret : 최적의 move와의 차이


<br>
<hr>
<br>

# 23. Monte Carlo Tree Search
 (1) 기본 아이디어
  1) Look-ahead tree를 만든다. 
   ex) 게임트리
  2) 시뮬레이션을 통해 reward를 생성하고 확인한다.
  3) UCB 알고리즘을 Tree의 내부 노드에 적용한다.
  4) 확장할 노드를 'optimistically'하게 선택한다.


<br>
<hr>
<br>

# 24. Monte Carlo Tree Search
 (1) MCTL 순서
  1) Selection
  2) Expansion
  3) Play-out(시뮬레이션)
  4) Backpropagation

 (2) Selection
  - Selection은 리프 노드(막단 노드)에 도착할 때 까지 재귀적으로 이루어진다.

 (3) Expansion
  - 막단 노드에서부터 1개 혹은 여러 개의 노드가 확장된다.

 (4) Simulation
  - 시뮬레이션으로 한 번의 게임이 플레이 된다.

 (5) Backpropagation
  - 시뮬레이션의 결과를 트리를 타고 올라가서 root 노드에 전달한다.


<br>
<hr>
<br>

# 25. Move Selection for UCT
 (1) Scenario
  - UCT를 실행할 수 있는만큼 최대한 실행한다.
  - 시뮬레이션을 실행해서 트리를 확장시킨다.

 (2) 시간이 없다면 어떤 move를 취해야 할까?
  - mean이 가장 높은 것
  - UCB가 가장 높은 것
  - 가장 시뮬레이션을 많이 한 move
  - MCTS는 좀 더 가능성 있는 move를 더 취한다.



<br>
<hr>
<br>


# 26. Sample MCTS Tree
 - MCTS의 샘플 그림이다. 루트 노드부터 시작해서 각 막단노드에 시뮬레이션을 하고, 결과를 기록해 둔 것을 볼 수 있다.



<br>
<hr>
<br>


# 27. Summary - MCTS So far
 - MCTS에서 UCB와 UCT의 두 알고리즘은 매우 중요한 알고리즘들이다.
 
   두 알고리즘은 상대적으로 약한 조건에서 잘 설립된 convergence guarantee일 때 효과적이다.
 - MCTS의 장점중 하나는 도메인에 독립적이기 때문에 다양한 게임에 적용 가능하다는 것이다.
 - 게임 및 기타 응용 프로그램들을 성공적으로 만들기 위한 기초가 되는 알고리즘이다.
