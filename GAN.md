# 1. What are GANs?
 - Adversarial : 서로 경쟁하는 두 개의 신경망 시스템.
 - 인풋 데이터와 유사한 데이터를 생성해낼 수 있다.
 - Unsupervised Learning

<br>
<hr>
<br>

# 2. 그림 예제
 - Generator : 임의의 noise를 입력 받아, 실제 데이터와 유사한 데이터를 생성해 낸다.
 - Discriminator : 데이터가 실제 데이터인지, Generator가 생성해 낸 데이터인지 판별한다.


<br>
<hr>
<br>


# 3. Discriminative Models
 - Discriminative Models : 입력 데이터 (x)를 원하는 출력 클래스 라벨(y)에 매핑하는 함수를 학습한다.
 - 조건부 분포 P(y|x)를 학습한다.


<br>
<hr>
<br>



# 4. Generative Models
 - Generative Models : 입력 데이터 및 라벨의 동시 확률, 즉 P(x,y)를 동시에 학습하려고 한다.
 - 라벨이 없는 경우에도 입력 데이터의 기본 구조를 이해하고 잘 설명할 수 있는 잠재력을 가지고 있다.


<br>
<hr>
<br>


# 5. How GANs are being used?
 - 자연 이미지 모델링에 적용 된다.
 - GAN은 다른 생성 모델과 비교할 때 성능이 상당히 좋다. cf) Naive Bayes 등
 - Unsupervised learning에서 유용하다.


<br>
<hr>
<br>



# 6. Why GANs?
 - latent code를 사용한다.
 - 변형 방법과는 달리 점근적으로 일관성(Asymptotically consistent)이 있다.
 - Markov chain이 필요하지 않다.
 - 종종 최고의 샘플을 만들어 낸다!


<br>
<hr>
<br>



# 7. 그림 예제
 - 선글라스를 낀 남자 사진 - 선글라스를 안 낀 남자 사진 + 선글라스를 안 낀 여자 사진 = 선글라스를 낀 여자 사진



<br>
<hr>
<br>


# 8. How to train GANs?
### (1) 목표
  - Generative network의 목표 : Discriminative network의 오류를 높인다. (생성된 데이터가 교육 데이터처럼 보이게 하는 매개변수를 찾는다.)
  - Discriminative network의 목표 : 분류를 잘 한다.

### (2) 학습
  - Generator의 훈련 : Discriminator의 2진 분류 손실의 부정을 역행
  - Discriminator의 훈련 : 2진 분류 손실로부터 역행

### (3) 모델
  - Generator : Deconvolution Neural Network
  - Discriminator : CNN


<br>
<hr>
<br>


# 9. GAN의 다양한 종류
### (1) InfoGAN
  - 데이터 분포를 대략적으로 이해하고, 해석 가능하고 유용한 벡터 표현을 배운다.

### (2) Conditional GANs
  - 외부 정보(클래스 라벨, 텍스트, 다른 이미지 등)를 고려하여 샘플을 생성한다. G가 특정 유형의 출력을 생성하도록 한다.


<br>
<hr>
<br>


# 10. Major Difficulties
 - 네트워크는 converge 하기 어렵다.
 - 목표는 생성자와 판별자가 평형에 도달하는 것이지만, 어렵다.
 - GAN은 큰 문제를 converge하고 있다. (ImageNet 등)


<br>
<hr>
<br>


# 11. Common Failure Cases
 - 판별자가 너무 강력해서 생성자가 아무 것도 배우지 못한다.
 - 생성자가 판별자의 매우 구체적인 취약점만을 학습한다.
 - 생성자는 실제 데이터 분포의 아주 작은 하위 집합만을 학습한다.


<br>
<hr>
<br>


# 12. So what can we do?
 - Input을 Normalize 하기
 - loss function 수정하기
 - Spherical Z 사용하기
 - BatchNorm
 - Sparse Gradient 피하기 (ReLU, MaxPool)
 - Soft and Noisy 라벨 사용하기
 - DCGAN / Hybrid Models
 - 초기에 오류 추적하기
 - 라벨이 있다면 사용하기
 - 입력에 노이즈 추가하기(시간에 따라 감소)


<br>
<hr>
<br>


# 13. Conclusions
 - 판별자를 transfer learning의 base model로 사용하거나, production model의 미세 조정을 위해 사용한다.
 - 잘 훈련된 생성자를 production model의 교육에 사용되는 데이터 소스로 사용한다.
