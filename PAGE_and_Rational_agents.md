# 1. AI prehistory
 ##### (1) 철학 : 논리, 추론의 방법, mind as physical system(몸과 분리된 soul이 있다고 믿음), 학습의 기초, 언어, 합리성
 ##### (2) 수학 : 공식 표현과 증명, 알고리즘, 계산, 결정성, 편의성, 확률
 ##### (3) 심리학 : 적응, 지각 현상 및 운동 조절, 실험 기법(정신 물리학 등)
 ##### (4) 언어학 : 지식 표현, 문법
 ##### (5) 신경 과학 : 정신 활동을 위한 물리적 기질
 ##### (6) Control theory(제어 이론) : 항상성 시스템, 안정성, 최적의 에이전트 설계

<br>
<hr>
<br>

# 2. Potted history of AI
 - 1943 : McCulloch & Pitts "뇌의 Boolean circuit 모델"
 - 1950 : Turing의 "Computing Machinery and Intelligence"
 - 1952-69 : Look, Ma, no hands!
 - 1950s : 사무엘의 checkers 프로그램, Newell & Simon의 Logic Theorist, Gelernter's 기하학 엔진을 포함한 초기 AI 프로그램
 - 1965 : Dartmouth meeting "Artificial Intelligence" 채택
 - 1966-74 : 인공지능은 계산상의 복잡성을 발견했다. 신경망 연구가 거의 사라짐.
 - 1969-79 : knowledge-based 시스템의 초기 개발
 - 1980-88 : Expert systems 산업 호황
 - 1988-93 : Expert systems 산업 붕괴 "AI Winter"
 - 1985-95 : 신경망 연구가 다시 인기 있어짐
 - 1988- : 확률론 및 의사결정론의 부활. AI의 기술적 깊이가 급격히 증가
 - "Nouvelle AI" ALife, GAs, soft computing


<br>
<hr>
<br>

# 3. State of the art
 ##### 다음 중 현재 AI가 수행할 수 있는 것은?
 - 탁구 게임 (O)
 - 곡선의 산길을 따라 운전하기 (O)
 - 카이로 중심부에서 운전 (Will do)
 - bridge 게임 하기 (O)
 - 새로운 수학적 정리를 발견하고 증명하기 (O)
 - 재미있는 이야기 쓰기 (O)
 - 법의 전문 분야에서 자문 제공하기 (O)
 - 실시간으로 영어를 스웨덴어로 번역하기 (O)


<br>
<hr>
<br>

# 4. PAGE
##### (1) PAGE란?
  - PAGE는 Percepts(받아드리기), Actions(행동), Goals(목표), Enviornment(환경)의 줄임말이다.
  - 로봇 청소기로 예시를 들면, 버튼으로 명령을 받아드려서 움직이는 행동을 하며 집으로 돌아가는 Goal을 가지고 장애물(환경)을 피해서 간다.

##### (2) PAGE 예제
  - Intelligent agent를 설계하기 위해서는 가장 먼저 설계를 설정해야 한다. 아래는 자동화 된 택시를 설계하는 작업이다.
  - Percepts : 비디오, 가속도계, 게이지, 엔진 센서, 키보드, GPS 등
  - Actions : 조종, accelerate, 브레이크, horn, speak/display 등
  - Goals : 안전, 목적지 도착, 이익 극대화, 법규 준수, 승객 편의 등
  - Environment : 미국 도시의 거리, 고속도로, 교통, 보행자, 날씨, 고객 등


<br>
<hr>
<br>

# 5. Rational agents
 - Rational agents : 일반성을 가지고, 모든 environment에 맞는 goal을 지정할 수 있게 하는 것
 - Rational action : 현재까지의 percept를 고려해서 성능을 최대화 하는 action을 하는 것
 - Rational은 모든 것을 아는 것이 아니다! (부분 부분 아는 것이다.)
 - Rational은 무조건 성공하게 하는 것이 아니다! (가끔 실수도 할 수 있고 잘 할 수도 있는 것이다.)


<br>
<hr>
<br>

# 6. Environment types
 - Environment types가 대부분 agent의 설계를 결정한다.
 - Environment types 예제
 
　 | Solitaire |	주사위 놀이 |	인터넷 쇼핑 |	택시
|---|:---:|---:|---:|:---:|
접근가능	 |  O		 |  O		 |   X		| X
Deterministic	 |  O		|   X		|  Partly	| X
일시적		|   X	|	   X		|    X	|	 X
Static		|   O		| Semi	|	  Semi	|	 X
Discrete	|   O		|   O		 |   O	|	 X


<br>
<hr>
<br>

# 7. Agent functions and programs
##### (1) Agent functions
  - Agent는 완전히 Agent function에 의해 지정된다.
  - Percept 시퀀스를 action에 매핑한다.
  - Agent function은 rational하다.
  - Agent program은 하나의 percept를 input으로 한다.

##### (2) 목표
  - Rational agent의 function을 간결하게 구현하는 것.

##### (3) 수도 코드
```c
 function SKELETON-AGENT(percept) returns action
  static : memory, the agent's memory of the world
  memory <- UPDATE-MEMORY(memory, percept)
  action <- CHOOSE-BEST-ACTION(memory)
  memory <- UPDATE-MEMORY(memory, action)
  return action
```


<br>
<hr>
<br>

# 8. AIMA code
 ##### (1) 코드는 4개의 디렉토리로 구분된다.
  - Agents : agent 유형 및 프로그램을 정의하는 코드
  - Algorithms : agent 프로그램에 사용되는 메소드 코드
  - Environments : Environment types를 정의하는 코드, 시뮬레이션
  - Domains : 알고리즘에 입력하기 위한 문제 유형 및 인스턴스 (종종 알고리즘 코드를 environments가 아닌 domain에서 실행해 본다.)

 ##### (2) 수도 코드
 ```c
 (setq joe (make-agent :name 'joe :body (make-agent-body)
		       :program(make-dumb-agent-program)))
 (defun make-dumb-agent-program ()
  (let ((memory nil))
   #'(lambda (percept)
    (push percept memory)
    'no-op)))
```
