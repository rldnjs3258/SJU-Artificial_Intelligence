# 1. Agent types
 1) Simple reflex agents
 
 2) Reflex agents with state
 
 3) Goal-based agents
 
 4) Utility-based agents

<br>
<hr>
<br>

# 2. Simple reflex agents

 - 구조
 
  1) Sensors(Input)
  
  2) 현재의 환경 파악
  
  3) Condition-action rules : 조건에 따라 해야할 Action 파악
  
  4) Effectors(Output)
  
  5) Environment
  
 - 예제 : 파블로의 개는 주인이 밥을 줄 때마다 종을 울려서, 종을 울리기만 해도(Input) 개가 침을 흘리는(Output) 실험이었다.


<br>
<hr>
<br>

# 3. Reflex agents with state

 - 구조
 
  1) Sensors(Input)
  
  2) State : 세상이 어떻게 발전하고 있는지, 내 행동이 어떤 것을 의미하는지, 현재의 환경 파악.
  
  3) Condition-action rules : 조건에 따라 해야할 Action 파악
  
  4) Effectors(Output)
  
  5) Environment
  
 - 내용 : Reflex agents with state에는 input에 따른 output만 있는 것이 아니라, input -> state -> output과 같이 state를 고려한다.


<br>
<hr>
<br>

# 4. Goal-based agents

 - 구조
 
  1) Sensors(Input)
  
  2) State : 세상이 어떻게 발전하고 있는지, 내 행동이 어떤 것을 의미하는지, 현재의 환경 파악. 내가 행동 A를 하면 어떻게 될 것인가.
  
  3) Goals : 조건에 따라 해야할 Action 파악
  
  4) Effectors(Output)
  
  5) Environment
  
 - 내용 : Goal-based agents는 실패 했을 경우도 고려하며 Goal에 다가간다.


<br>
<hr>
<br>

# 5. Utility-based agents

 - 구조
 
  1) Sensors(Input)
  
  2) State : 세상이 어떻게 발전하고 있는지, 내 행동이 어떤 것을 의미하는지, 현재의 환경 파악. 내가 행동 A를 하면 어떻게 될 것인가.
  
  3) Utility : 그 상태에서 얼마나 행복할 수 있을지 생각. 조건에 따라 해야할 Action 파악
  
  4) Effectors(Output)
  
  5) Environment
  
 - 내용 : Agent가 Happiness, Fairness, Ethical 등을 최대화 하는 것을 고려한다.


<br>
<hr>
<br>

# 6. The vacuum world

 (1) Percepts : 부딛힘, 먼지, Home
 
 (2) Actions : 앞으로 가서 빨아들인다. 좌측 이동, 우측 이동
 
 (3) Goals : Agent에 Reward를 준다. Reward Function만 잘 설계해도 좋은 Agent를 만들 수 있다.
 
  - 먼지 조각을 치울 때마다 100점 추가!
  
  - 각 action마다 -1점!
  
  - Home과 멀리서 전원이 꺼지면 -1000점!
  
 (4) Environment
 
  - Grid, 벽/장애물, 먼지 분포 및 생성, agent body
  
  - 벽에 부딪히지 않은 경우 movement actions을 한다.
  
  - suck actions는 agent body에 먼지를 넣는다.
  


<br>
<hr>
<br>

# 7. Example : vacuum world

 - 그림을 통해 vaccum world를 이해해 보자.
 
 - Single-state
 
 - Multiple-state
 
 - Contingency(비상사태) : 5번에서 머피의 법칙처럼 깨끗한 카펫을 vacuum해서 더럽힐 수 있다.
 
 - Local sensing : 먼지, 위치


<br>
<hr>
<br>

# 8. Example : vacuum world state space graph

 - 그림은 먼지의 수와 vacuum의 위치에 따라 vacuum이 이동할 수 있는 경로(연산)를 나타낸 것이다.
 
 - States : 먼지의 수 및 로봇의 위치
 
 - Operators : 왼쪽, 오른쪽, Suck
 
 - Goal test : 먼지 없음
 
 - Path cost : 한 번 움직일 때마다 1
