# 1. 라이브러리 및 모듈 로드
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras import backend as K
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import numpy as np


# 2. 데이터 셋
seed = 785 # seed for reproducing same results
np.random.seed(seed)

dataset = np.loadtxt('A_Z Handwritten Data.csv', delimiter=',') # load dataset

# split into input and output variables
X = dataset[:,0:784] #input
Y = dataset[:,0] #output

(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size=0.50, random_state=seed) # split the data into training (50%) and testing (50%)

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32') #reshape
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32') #reshape

X_train = X_train / 255
X_test = X_test / 255

# one hot encode outputs
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

num_classes = Y_test.shape[1]


# 3. CNN 모델 구성
# create model
model = Sequential() #Initializing the CNN

# 첫 번째 Convolution layer
model.add(Conv2D(32, (5, 5), input_shape=(28, 28, 1), activation='relu')) #5*5 필터를 이용하여 28*28 영상의 특징을 추출한다. 결과물을 relu를 통해 다음 레이어에 전달한다. relu는 주로 은닉층에 사용!
model.add(MaxPooling2D(pool_size=(2, 2))) # 영상에서의 사소한 변화가 특징 추출에 큰 영향을 미치지 않게 한다.

# 드랍아웃
model.add(Dropout(0.2)) # 과적합을 방지하기 위해서 학습 시에 지정된 비율만큼 임의의 입력 뉴런(1차원)을 제외시킵니다.

# Flattening
model.add(Flatten()) # 2차원의 특징맵을 전결합층으로 전달하기 위해서 1차원 형식으로 바꿔줍니다.

# Full connection
model.add(Dense(128, activation='relu')) # 모든 입력 뉴런과 출력 뉴런을 연결하는 전결합층입니다. 결과물을 relu를 통해 다음 레이어로 전달한다.  relu는 주로 은닉층에 사용!
model.add(Dense(num_classes, activation='softmax')) # 모든 입력 뉴런과 출력 뉴런을 연결하는 전결합층입니다. 결과물을 softmax를 통해 확률 값이 가장 높은 클래스로 분류한다. softmax는 주로 출력층에 이용한다!

# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# 4. 모델 학습
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=10, batch_size=200, verbose=2)


# 5. Final evaluation of the model
scores = model.evaluate(X_test,Y_test, verbose=0)
print("CNN Error: %.2f%%" % (100-scores[1]*100))
model.save('weights.model')