# 1. Informed search algorithms
 (1) Informed search란?
  - Informed Search(Heuristic Search)는 가장 전도 유망한 방향으로 Search를 진행하는 것을 말한다.
  
    즉, '목표 노드의 위치'를 안 채로 Search 하는 것이다.
  - 장점 : Solution을 좀 더 일찍 효율적으로 찾는다. 전체적으로 Uninformed Search보다 훨씬 효율적이다. 

 (2) Informed search 예시
  - Best-first search
  - A* search
  - Heuristics search

<br>
<hr>
<br>

# 2. Best-first search
 (1) Best-first search란?
  - Informed search의 기본적인 접근방법은 Best-First Search이다.
  
    따라서 기본적으로 모든 Informed search는 다 Best-First Search이다.

 (2) Best-first search의 방법
  - 평가 함수 F(n)을 기반으로, 각 노드를 평가해서 가장 최선의 곳으로 확장한다. (휴리스틱 함수에 따라 대기열을 정리한다.)
  - "Desirability" : 바람직 함
  - Implementation : fringe는 Desirability를 기준으로 내림차순 정렬 되어 있다.
  
    (fringe : 아직 가지 않은 노드를 저장해놓은 Queue)

 (3) Best-first search 예시
  - Greedy search
  - A* search

 (4) Best-first search 수도코드
 ```C
function BEST-FIRST-SEARCH(problem, EVAL-FN) returns a solution sequence
	inputs : problem, a problem
	            Eval-Fn, an evaluation function
	Queueing-Fn <- a function that orders nodes by EVAL-FN
	return GENERAL-SEARCH(problem, Queueing-Fn)
   ```

 (5) Properties of Best-first search
  1) Complete?
   - Not complete. 무한 경로로 빠질 수 있다.
   
     단, Most reasonable heuristic인 경우는 무한 경로에 빠지지 않는다.

  2) Time
   - O(b^m). m은 maximum depth이다.

  3) Space
   - O(b^m). 아직 확장하지 않은 모든 상태를 대기열에 유지해야 한다.

  4) Optimal
   - 좋은 Heuristic을 설계하면 최악의 상황들을 피할 수 있다.


<br>
<hr>
<br>

# 3. Greedy search
 (1) 평가 함수
  - H(n) : Uniform-Cost Search의 G(n)이 현재 노드에서 가장 가까운 거리를 찾았다면, H(n)은 현재 노드에서 목표 노드까지의 거리
를 직빵(직선)으로 계산하는 것이다. 즉, 현재 노드에서 목표 노드까지의 거리를 H(n)이라고 한다.
  - H(n)의 뜻 : 현재 노드에서 Goal 노드까지 가장 빠르게 갔을 때의 Cost이다.
  
  ex) hSLD(n) = n에서 출발하여 목표인 Bucharest까지의 직선 거리(Straight Line Distance)
  - H(n)의 속성
   1) H(n)>=0가 요구 된다.
   2) H(Goal)=0
   3) H(n)은 '실제로 n 부터 goal까지 걸린 cost'보다 작거나 같다 : H(n)은 최선의 방법을 알려주는 거지, 현실 세계에서 늘 최선으로
가지는 못할 수 있기 때문이다.

 (2) Greedy search
  - Greedy search는 평가 함수를 통해서 'goal'을 목표로 가까운 노드를 확장하는 것이다.


<br>
<hr>
<br>

# 4. Greedy search example
 - Greedy search의 예제를 보면 Arad에서 H(n)을 통해 cost가 적은 Sibiu로 이동하고, Sibiu에서 cost가 적은 Fagaras로 이동하며,
Fagaras에서 cost가 적은 Bucharest(cost = 0)로 이동한다.
 - 주의해야 할 점은 Arad에서 Sibiu로 노드를 확장했을 때, Child Node로 Arad가 또 생긴걸 볼 수 있는데 이 때 다시 Arad로 돌아가
면 무한 반복이 일어난다. 따라서 Node를 Expand할 때 자신의 조상 노드들을 확인해서 이미 나온 Node라면 Discarding 해줘야 한
다.

<br>
<hr>
<br>

# 5. Properties of greedy search
 (1) Complete
  - No. 반복문에 빠질 수 있다. (lasi -> Neamt -> lasi -> Neamt ...)
  - repeated-state를 체크하면 반복문에 빠지지 않게 할 수 있다.

 (2) Time
  - O(b^m)
  - 휴리스틱 함수를 잘 짜면 복잡도를 줄여나갈 수 있다.

 (3) Space
  - O(b^m)
  - 모든 노드들을 메모리에 갖고 있다.

 (4) Optimal
  - No


<br>
<hr>
<br>

# 6. A* search
 (1) A* search란?
  - A* search는 H(n)뿐 아니라 G(n)도 사용한다.
  
    즉 F(n) = G(n) + H(n)으로, n을 통한 Solution 중 가장 적은 비용을 추정하는 방법 이다.
  - F(n) = G(n) + H(n)
  
    G(n) = 시작 노드에서 현재 노드까지 걸린 Path Cost이다.
    
    H(n) = 현재 노드에서 Goal 노드까지 가장 빠르게 갔을 때의 Cost이다.
    
    F(n) = 경로의 예상 총 Cost

 (2) H(n)과 Heuristic
  - 평가함수인 H(n)은 Heuristic하게 짜야 한다. Goal state를 아주 최적의 해를 통해서 가는 것이 목표이기 때문이다.

 (3) H(n)의 최적화(Optimal) 조건
  - H(n)의 최적화(Optimal)를 위해서 아래의 조건이 요구된다.
   1) H(n)이 Admissible 휴리스틱이어야 한다.
    - 아주 객관적인 휴리스틱을 설정해서 누구나 인정할 수 있어야 한다.
    
       예를 들어 앞의 H-SLD는 휴리스틱을 직선 거리로 잡았었는데 이는 객관성을 인정받을 만 하다. (과대평가 될 이유가 없다.)
   2) Consistency


<br>
<hr>
<br>

# 7. A* search example
 - A* search의 예제이다. Arad(366=0+366)에서 출발하여 Sibiu(393=140+253), Timisoara(447=118+329), Zerind(449=75+374) 중 F(n)
이 가장 적은 Sibiu를 선택하고, Sibiu에서 Arad(646=280+366), Fagaras(415=239+176), Oradea(671=291+380), Rimnicu Vilcea(413=
220+193) 중 F(n)이 가장 적은 Rimnicu Vilcea를 선택한다. 이러한 방법으로 계속 가서 Bucharest(418=418+0)에 도달한다.
 - 주의해야 할 것은, 시작 상태에서 Goal 상태까지의 F(n)은 항상 일정한 것이 아니라는 것이다. F(n)은 현재 선택한 노드에 따라서
지금까지 거쳐 온 cost인 G(n)과, 현재 선택한 노드에서 Goal까지 최선일 때의 cost인 H(n)을 각 노드마다 항상 계산하기 때문에 
일정하지 않다.


<br>
<hr>
<br>

# 8. A*의 Optimal 증명
 (1) 가정
  - 최선의 goal을 G1, 차선책인 goal을 G2라고 생각한다.
  - 'n'을 최적의 목표인 goal까지 가는 경로상의, 아직 확장되지 않은 노드라고 생각하자.

 (2) 증명
  - F(G2) = G(G2)이고, H(G2) = 0이다.
  
    즉 G2는 '차선책' Goal로 선택되어 Goal에 다다른 것이기 때문에 F(G2) = G(G2)이고,  더 가지 않을 것이기 때문에 H(G2)=0이다.
  - F(G2) > G(G1)
  
    G2는 '차선책'이기 때문에 원래 goal인 G1에서 드는 cost보다 더 큰 cost가 든다.
  - F(G2) >= F(n)
  
    차선책으로 선택된 F2는 'n'일 수도 있고, 'n'에서 확장된 노드일 수도 있다.

 (3) 결론
  - F(G2) >F(n)이기 때문에 A*의 이론상 당연히 G2보다 N이 먼저 Expand 된다. 
  
    따라서 A* 알고리즘은 절대 차선책인 G2로 확장하지 않을 것이고, 이는 A*이 Optimal 하다는 것을 증명한다.


<br>
<hr>
<br>

# 9. A*의 Optimal 증명 추가
 (1) F(n)의 특성
  - 시작 노드에서 Goal 노드까지 가까워 질 때마다 F(n)은 점진적으로 증가하게 된다.
  - 경로가 완전히 일직선이면 F(n)이 일정할 수도 있긴 하다. 다만, 절대로 감소하는 일은 없다.
  - 즉, Goal 노드와 가까워 질 때마다 F(n)은 증가하거나 같아야 한다. 

 (2) 수식
  - 노드가 점진적으로 Goal에 가까워지는 걸 f-contours가 증가한다고 표현한다. 
  - f-contours를 i로 두면 f(i)<f(i+1)이다.


<br>
<hr>
<br>

# 10. Properties of A*
 (1) Complete
  - Yes. F<=F(G)여서 노드가 무한히 존재하지 않는 이상 Complete하다.

 (2) Time
  - O(b^m)
  - 휴리스틱 함수에 근거하여 Exponential(지수적인)하다.
  - h x 길이의 상대 오차

 (3) Space
  - 모든 노드를 메모리에 저장한다.
  - O(b^m)

 (4) Optimal
  - Yes. F(i)가 끝날 때 까지 F(i+1)을 확장할 수 없다.

 (5) 그 외
  - C*을 '최적의 F(n) 비용'이라고 할 때, A*은 F(n) < C*에 기반하여 노드를 확장한다.
  - A*은 가끔 F(n) = C*에 기반하여 노드를 확장한다.
  - A*은 F(n) > C*에 기반하여 노드를 확장하지 않는다.


<br>
<hr>
<br>


# 11. Proof of lemma : Consistency
 (1) Consistency란?
  - Monotonicity(단조성)이라는 뜻이다.

 (2) Consistent의 Heuristic
  - 현재 노드를 N이라고 하고, 자식 노드 중 하나를 N'라고 생각하자. 
  
    이 때 현재 노드 N에서 Goal까지의 거리인 H(N)은 현재 노드 N에서 자식 노드 N'까지의 거리와 자식 노드 N'에서 Goal까지의 거
리인 H(N')의 합보다 작거나 같아야 한다. 자식 노드인 N'가 Goal까지 가는 최선의 경로 중의 노드일지 아닐지 모르기 때문이다. 
  - H(N) <= 현재 노드 N에서 자식 노드 N'까지의 거리 + 자식 노드 N'에서 Goal까지의 거리
  
    H(N) <= c(N,a,N') + H(N')

 (2) 정리
  - 노드 N과 그 자식 노드 N'이 있을 때 Consistency가 보장되기 때문에 아래의 식을 만족한다.
  
    F(N') = G(N') + H(N')
    
            = G(N) + C(N,A,N') + H(N')
            
            >= G(N) + H(N)
            
            = F(N)
            
  - 이는 노드가 Goal과 가까워질 때 F(N)이 감소할 수 없음을 의미하기 때문에 A*이 Optimal 하다는 것을 증명한다.


<br>
<hr>
<br>


# 12. Admissible heuristics
 (1) 퍼즐 예제
  - Admissible heuristics를 1~8까지의 퍼즐 예제를 통해 알아보자. Start State로 어지럽혀진 퍼즐과, Goal State로 정돈된 퍼즐이 있
다.

 (2) 수식
  - h1(n) = 잘못 배치 된 타일 수
  
    h2(n) = 총 Manhattan 거리(각 타일의 Goal 위치까지의 cost)

 (3) 결과
  - h1(S) = 6
  
    h2(S) = 4 + 0 + 3 + 3 + 1 + 0 + 2 + 1 = 14


<br>
<hr>
<br>


# 13. Dominance 
 - 모든 n에 대해 h2(n) >= h1(n)이고 둘은 admissible하다.
 
    이때 h2가 h1을 dominates하고, 서치에 더 좋다.
 - Typical search costs :
 
  d = 14	IDS = 3,473,941 nodes
  
	A*(h1) = 539 nodes
  
	A*(h2) = 113 nodes
  
  d = 24	IDS = 54,000,000,000 nodes
  
	A*(h1) = 39,135 nodes
  
	A*(h2) = 1,641 nodes
  
 - admissible heuristics인 ha, hb에 대해서
 
   h(n) = max(ha(n), hb(n))이며 ha와 hb 또한 admissible 하고 dominate 하다.


<br>
<hr>
<br>


# 14. Relaxed problems
 (1) Relaxed problems란?
  - Relaxed problems는 말 그대로, 문제를 풀기 쉽게 좀 더 Relaxed 한 problems이다. Action에 있어서 더 제약이 없다.
  - 실제 문제를 relaxed 해서 얻은 solution cost는 Admissible heuristics하다.

 (2) Relaxed problems 예제
  - 8-puzzle의 문제가 Relaxed 되어 각 타일이 제약 없이 어디로든 움직일 수 있으면
  
    h1(n)을 통해 shortest solution을 얻을 수 있다.
  - 8-puzzle의 문제가 Relaxed 되어 각 타일이 어느 인접한 곳으로든 움직일 수 있으면
  
    h2(n)을 통해 shortest solution을 얻을 수 있다.

 (3) 정리
  - Relaxed problems의 optimal solution cost는 실제 문제의 optimal solution cost보다 크지 않다.


<br>
<hr>
<br>


# 15. Relaxed problems contd.
 - Relaxed problems의 예제로 'Traveling Salesperson Problem(TSP)'가 있다.
 
   모든 도시를 한 번씩 방문하는 가장 짧은 투어 루트를 찾는 것이다.
 - Minimum spanning tree : O(n^2)
 
    최단 투어 공식이다.


<br>
<hr>
<br>


# 16. Summary
 - Heuristic 함수는 최단 경로 비용을 계산한다.
 - 좋은 heuristic은 탐색 비용을 크게 줄일 수 있다.
 - Greedy best-first search는 H(n)을 계산하여 확장해 나간다.
 
    이는 incomplete하고, 항상 optimal하지 않다.
 - A* search는 G(n) + H(n)을 계산하여 확장해 나간다.
 
    이는 complete하고, optimal하다.
    
    최적의 효율성이다. (정방향 서치에서 up to tie-break이다.)
 - 실제 문제를 relaxed 해서 얻은 solution cost는 Admissible heuristics하다.
