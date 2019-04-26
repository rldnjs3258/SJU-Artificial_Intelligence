# 1. Uninformed search strategies(무정보 탐색 전략)
 - Uninformed search strategies는 현재 상태에서 목표 상태까지 다다르는 Step(Path cost)의 갯수를 모르는 것들이다.
   해(Solution)를 찾아서, 목표에 대한 고려 없이 목표가 발견될 때 까지 전체 트리를 전부 탐색한다.

(1) Breadth-first search(너비 우선 탐색)

(2) Uniform-cost search(균일 비용 탐색)

(3) Depth-first search(깊이 우선 탐색)

(4) Depth-limited search(깊이 제한 탐색)

(5) Iterative deepening search(반복 깊이 증가 탐색)

<br>
<hr>
<br>

# 2. Breadth-first search(너비 우선 탐색)
 - 루트 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법.
 
   시작 정점으로부터 가장 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법이다.

   깊게(deep) 탐색 하기 전에 넓게(wide) 탐색하는 것이다.

- Implementation : Queueing FN = 큐의 끝에 insert
 - 예제 : Arad와 근접한 도시인 Zerind, Sibiu, Timisoara를 먼저 살펴보고, 그 이후에 Zerind, Sibiu, Timisoara와 가까운 지역들을
   살펴본다.


<br>
<hr>
<br>

# 3. Properties of breadth-first search
 (1) Complete
  - Yes. 노드가 유한하면 솔루션을 찾을 수 있다.

 (2) Time
  - 1 + b + b^2 + b^3 + ... b^d = O(b^d)

 (3) Space(메모리가 얼마나 필요한가)
  - O(b^d)
  - 메모리에 모든 노드를 갖게 된다.
    노드는 1mb/sec의 속도로 생성 가능하므로, 24hrs에 86GB의 메모리가 필요하다. 따라서 메모리(space)가 중요하다. 

 (4) Optimal(최적)
  - Yes. 목표에 도달하기 까지 가장 인접한 곳(가장 적은 수의 단계)부터 찾기 때문에 최적이다. 
  - 1 step 당 1 cost인 경우 최적화 되어 있다.
    그 외의 경우는 최적화 되어 있지 않다.


<br>
<hr>
<br>

# 4. Uniform-cost search(균일 비용 탐색)
 - 인접한 노드 중 소요되는 비용(cost)이 가장 적은 노드를 탐색한다.
 - Implementation : Queueing FN = Path cost가 증가하는 순서대로 Insert
 - 예제 : Arad에서 Zerind, Sibiu, Timisoara로 가는 cost가 각각 75, 140, 118일 때, Zerind를 선택한다.


<br>
<hr>
<br>

# 5. Properties of uniform-cost search
 (1) Complete
  - Yes. step cost >= ￠인 경우 Complete하다.

 (2) Time
  - 최적의 솔루션을 찾기 위한 g<=cost 노드들

 (3) Space
  - 최적의 솔루션을 찾기 위한 g<=cost 노드들

 (4) Optimal
  - Yes


<br>
<hr>
<br>

# 6. Depth-first search(깊이 우선 탐색)
 - 루트 노드에서 시작해서 다음 branch로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법.
 
   즉 넓게 탐색하기 전에 깊게 탐색하는 것이다.
 - Implementation : Queueing FN = queue의 맨 앞에 insert
 - 예제 : Arad에서 출발하여 Zerind에서 갈 수 있는 지역 3개를 다 완벽하게 탐색하고, Sibiu의 탐색을 시작한다.


<br>
<hr>
<br>

# 7. DFS on a depth-3 binary tree
 - Depth-first search와 같은 탐색 방법인데, 트리가 binary 즉 자식 노드가 모두 2개로 이루어져 있고 깊이가 3인 트리이다.



<br>
<hr>
<br>

# 8. Properties of depth-first search
 (1) Complete
  - No. Depth가 무한이거나 loop가 있는 곳에서 error가 발생할 수 있다.
  
    (loop가 있는 공간은 수정해야 한다.)
  - Yes. Depth가 유한한 곳에서는 Complete 하다.

 (2) Time
  - O(b^m)
  - m이 d보다 훨씬 클 경우 엄청난 time을 형성한다.
  
    Solution이 근접한 곳에 있는 경우, breadth-first보다 더 빠르게 찾을 수 있다.

 (3) Space
  - O(bm)
  - 선형 공간 등

 (4) Optimal
  - No. 솔루션을 얻지 못할 수도 있다.


<br>
<hr>
<br>

# 9. Depth-limited search
 - DFS의 무한 depth 문제를 피하기 위해, depth의 limit을 정해서 search한다.
 
   즉, depth-first search에 limit인 l이 있는 것이다.
 - Implementation : l의 깊이에 있는 노드는 자식이 없다.


<br>
<hr>
<br>

# 10. Iterative deepening search
 - Iterative deepening search는 Depth-limited search에서 limit을 점차 증가시키면서 반복 탐색 한다.
 - BFS와 DFS의 장점을 합체한 것이다.
 
   깊이에 제한이 있으니까 한쪽 경로로 무한히 빠질 일이 없고, 깊이를 점차 늘려나가면서 찾으므로 가장 가까운 최적해를 찾는다.

```C
function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution sequence
	inputs : problems, a problem
	for depth<- 0 to infinite do
		result <- DEPTH-LIMITED-SEARCH(problem, depth)
		if result != cutoff then return result
	end
```

<br>
<hr>
<br>

# 11. Iterative deepening search 예제
 - 깊이인 l을 0부터 1씩 늘려간다. 깊이가 0, 1, 2... 일 때 각각 다음 branch로 넘어가기 전에 l 전까지의 해당 분기를 완벽하게 
탐색한다.


<br>
<hr>
<br>


# 12. Properties of iterative deepening search
 (1) Complete
  - Yes

 (2) Time
  - O(b^d)
  - d는 depth를 뜻한다.

 (3) Space
  - O(bd)

 (4) Optimal
  - Yes. (Step cost가 1인 경우)
  - Uniform-cost tree로 수정할 수 있다.


<br>
<hr>
<br>

# 13. Summary
 - Problem formulation은 실제 세계(real world)를 모델링 하여 추상화하여 이루어 진다.
 
   추상화란 상세한 정보는 무시하고 필요성에 의해 있어야할 정보들만 간추려서 구성하는 것인데, 탐구하기에 좋은 공간이다.
 - 다양한 Uninformed search strategies 기억하기.
 - Iterative deepening search는 오직 선형 공간만을 사용한다.
 
   또한 다른 uninformed algorithms보다 훨씬 적은 시간이 걸린다.


<br>
<hr>
<br>

# 14. Summary of algorithms
| |		Breadth First	| Uniform Cost	| Depth First |	Depth Limited |	Iterative Deepening |
|---|:---:|---:|:---:|---:|---:|
| Complete		 |     Yes		 |    Yes		|     No		|   Yes, if l>=d	  |       Yes |
| Time		|   b^(d+1)		|    b^[C*/ε]	 |    b^m		   |    b^l		    |     b^d |
| Space		|   b^(d+1)		|    b^[C*/ε]	 |    bm		   |    bl		    |     bd |
| Optimal		 |     Yes		 |    Yes		 |    No		   |    No		   |      Yes |
