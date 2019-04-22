# 1. Example : Romania
 (1) 예제 : 현재는 Arad에 있는데 Romania(Bucharest)에서 휴일을 즐기고 싶다.
     내일 Bucharest로 출발하는 항공편을 탈 예정이다.

 (2) Formulate goal : Bucharest에 가기

 (3) Formulate problem
  - States : 도시가 여러개 있다.
  - Operators : 도시 간 운전

 (4) Find solution
  - Arad, Sibiu, Fagaras, Bucharest 같은 도시들의 순서

<br>
<hr>
<br>

# 2. Example : Romania
 - 그림은 Arad 부터 Bucharest까지 갈 때 거쳐 갈 수 있는 도시들의 경우의 수 이다.
 - Arad에서 출발해서 Zerind, Sibiu, Timisoara와 같은 도시 중 어느 방향으로 Bucharest까지 갈 것인지 정해야 한다.
<br>
<hr>
<br>

# 3. Problem types
 (1) Deterministic(결정론적), accessible(접근 가능) : single-state problem

 (2) Deterministic(결정론적), inaccssible(접근 불가능) : multiple-state problem

 (3) Nondeterministic(비결정론), inaccessible(접근 불가능) : contingency problem(우발적 문제)
  - 실행 중에 센서를 사용해야 한다.
  - 솔루션은 tree 혹은 policy이다.
  - 인터리브 search, execution

 (4) Unknown state : exploration problem(검색 문제, "online")
<br>
<hr>
<br>

# 4. Single-state problem formulation
 - 문제는 4가지 항목으로 정의된다.
 - 솔루션은 initial state에서 goal state로 이끄는 일련의 연산자(operators)이다.
 
 (1) Initial state(초기 상태) : Arad

 (2) Operators(혹은 후속 함수S(x))
  - Arad -> Zerind
  - Arad -> Sibiu

 (3) Goal test
  - expliciy(명시적) : x = "Bucharest"
  - implicit(암묵적) : NoDirt(x)

 (4) Path cost(additive)
  - 거리의 합, 실행 된 연산자의 수 등
  
<br>
<hr>
<br>

# 5. Selecting a state space
 - 실제 세계(real world)는 복잡하기 때문에 문제 해결을 위해 모델링 하여 추상화 되어야 한다.
   (abstract한 것은 real world보다 문제를 풀기 쉽다.)
   추상화란 상세한 정보는 무시하고 필요성에 의해 있어야할 정보들만 간추려서 구성하는 것인데, 탐구하기에 좋은 공간이다.
   
 (1) (Abstract) State = set of real states

 (2) (Abstract) Operator = 실제 actions의 복잡한 조합
  - "Arad -> Zerind"로 가는 경우, 우회 도로, 휴게소 등의 복잡한 경로가 있을 수 있다.

 (3) (Abstract) Solution = real wrold의 해답인 real paths의 집합
<br>
<hr>
<br>

# 6. Problem Solving
 - Rational Agent는 목표를 달성하기 위해 작업들을 수행 한다.
 
 (1) 에이전트에게 룩업 테이블 또는 reactive policy를 사용하여 Intelligent behavior(지능형 동작)을 설정할 수 있다.
  - 에이전트에게 룩업 테이블과 reactive policy를 통해 모든 상황에서 수행 할 작업을 알려준다.
    (그러나 table이나 policy를 구축하는 작업은 어렵다.)
  - 모든 '우연의 일'을 예측해야 한다.

 (2) 보다 일반적인 접근 방법은 에이전트가 '세계에 대한 지식'과 '행동이 미치는 영향'을 파악하고, 목표를 달성하기 위해
모델링된 공간에서 행동을 시뮬레이션 하는 것이다.

<br>
<hr>
<br>

# 7. Problem Solving Task
 (1) Given
  - 세계의 initial state(초기 상태)
  - 수행할 수 있는 actions 혹은 operators
  - Goal test : single-state에 이용해서 목표에 도달했는지 확인할 수 있는 goal test이다.

 (2) Find
  - 해결책을 위한 path of states와 operators.
    즉, Initial 상태를 goal test를 만족시키게 변환시키는 것들.

 - Initial state와 operators는 암묵적으로 states of the world의 상태를 갖고 있다. operator들 끼리의 전환은 무한히 가능하다.
 
<br>
<hr>
<br>

# 8. Measuring Performance
 (1) Path cost
  - Path에 cost를 할당하는 function이다.
  - 일반적으로 Path의 각 Operators의 cost를 합산한다.
  - 최소 cost의 솔루션을 찾는 것이 목표이다.

 (2) Search cost
  - 솔루션을 찾기 위해 필요한 계산 시간과 메모리 공간

 - 일반적으로 Path cost와 Search cost 사이에는 상반 관계가 있으므로, 사용할 수 있는 시간안에 가장 적합한 솔루션을 찾아야 한다.
<br>
<hr>
<br>

# 9. Sample Route Finding Problem
 - Arad부터 Bucharest로 가는 길의 예제이다.
 - Initial state : Arad
 - Goal state : Bucharest
 - Path cost : 경유하는 도시의 수, 이동 거리, 예상 소요 시간
<br>
<hr>
<br>

# 10. Sample "Toy" Problems
 - 1~8까지의 퍼즐을 맞추는 예제이다.
 - Start state : 어지럽혀져 있는 퍼즐
 - Goal state : 1~8까지 맞춰진 퍼즐
 - Cryptarithmetic(암호 해독)
 - 40 + 10 + 10 = 60
 - 29786 + 850 + 850 = 31486
 - F = 2, O = 9, R = 7, T = 8
<br>
<hr>
<br>

# 11. "Toy" Problems
 - 8-queens problem(N-queens problem) 예제 : 체스와 비슷한 8-queens 게임을 풀어보는 예제이다.
 
 (1) Missionaries와 cannibals, boats 각각의 말을 (M, C, B)로 생각한다.
  - M = left bank의 missionaries 수
  - C = left bank의 cannibals 수
  - B = left bank의 boats 수 (0 or 1)

 (2) Operators의 이동 : 1M, 1C, 2M, 2C, 1M1C

 (3) Goal state : (0, 0, 0)

<br>
<hr>
<br>

# 12. More realistic problems
 - 경로 찾기
 - Traveling salesman problem
 - NLSI 레이아웃
 - 로봇 네비게이션
 - 웹 검색

<br>
<hr>
<br>

# 13. Searching Concepts
 (1) 기본 지식
  - 인공지능에서 State는, State(Initial state)에서 state들 사이의 이동을 통해서 목표한 State(Goal state)를 찾아가는 것이다.
  - Optimal solution : 가장 코스트가 적게 드는 solution이다.

 (2) Search tree
  - 현재 state에 operator(successor function)를 적용하면 새로운 state가 발생한다.(노드가 확장, 즉 자식 노드가 생긴다.)
    이 행위를 반복하여 목적지에 달성하면 solution을 찾는 것이다.
    이러한 행위들로 인해 서치 트리가 만들어진다.
  - state를 어떤 방식으로 확장하는지는, Search strategy(서치 전략)을 이용해 정할 수 있다.

 (3) 탐색 트리(Search tree)
  - Search tree는 Initial state를 루트로 하고, states를 연속적으로 확장하여 search nodes들을 만들면서 만들어 진다.
  - Search Tree의 구성 요소
  - Corresponding state(해당 상태)
  - Parent node
  - Action(Operator)
  - Depth(깊이. 루트에서 노드까지 path의 길이)
  - Path cost

<br>
<hr>
<br>

# 14. Expanding Nodes and Search
 (1) 함수
 ```c
function GENERAL-SEARCH(problem, strategy) returns a solution, or failure
	#문제의 initial state를 이용하여 탐색 트리를 초기화 한다.
	loop do
		if expansion 할 만한 노드가 없는 경우 return failure
		expansion을 위한 leaf node 선택
		if 노드가 goal state를 포함하고 있는 경우 return 현재의 솔루션
		else 노드를 확장하고 서치 트리에 반영한다. 
	end
 ```


<br>
<hr>
<br>

# 15. Search Algorithm
 - 확장 되지 않은 서치 노드 queue를 통해 다양한 search strategies들을 구현할 수 있다. 
 - Search Strategy의 종류에 따라, Queue에 새 노드를 삽입하는 방법이 다르다. 
 ```c
function GENERAL-SEARCH(problem,QUEUING-FN) returns a solution, or failure
	nodes <- MAKE-QUEUE(MAKE-NODE(INITIAL-STATE[problem]))
	loop do
		if 노드가 비었다면 return failure
		node <- REMOVE-FRONT(nodes)
		if GOAL-TEST[problem]이 STATE(node)에 성공적으로 적용된다면 return node
		nodes <- QUEUING-FN(nodes, EXPAND(node, OPERATORS[problem]))
	end
  ```

<br>
<hr>
<br>

# 16. Search Strategies
 (1) Search strategies의 평가 방법
  - 완전성(Completeness)
  - 시간 복잡성(Time Complexity)
  - 공간 복잡성(Space Complexity)
  - 최적성(Optimality)

 (2) Uninformed search strategies
  - Uninformed search strategies는 현재 상태에서 목표 상태까지 다다르는 Step(Path cost)의 갯수를 모르는 것들이다.
  - 속성
  - Blind(맹목적)
  - Exhaustive
  - Bruteforce(무차별적)

 (3) Informed search strategies
  - Informed search strategies는 현재 상태에서 어떤 상태로 가야 Goal에 다가가기 수월한지 아는 것들이다.
  - 속성
  - Heuristic(경험적)
  - Intelligent(지능적)
