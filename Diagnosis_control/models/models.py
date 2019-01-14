from keras.models import Sequential
from keras.layers.core import Flatten, Dense, Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.utils import plot_model # for model description png
import os

from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint
from keras import backend as K

import numpy as np

"""
<Error>
ValueError: Negative dimension size caused by subtracting 2 from 1 for 'max_pooling2d_2/MaxPool' (op: 'MaxPool') with input shapes: [?,1,112,128].

<Solve>
Quoting an answer mentioned in github, you need to specify the dimension ordering:

Keras is a wrapper over Theano or Tensorflow libraries. Keras uses the setting variable image_dim_ordering to decide if the input layer is Theano or Tensorflow format. This setting can be specified in 2 ways -

specify 'tf' or 'th' in ~/.keras/keras.json like so -  image_dim_ordering: 'th'. Note: this is a json file.
or specify the image_dim_ordering in your model like so: model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="th"))
Appendix: image_dim_ordering in 'th' mode the channels dimension (the depth) is at index 1 (e.g. 3, 256, 256). In 'tf' mode is it at index 3 (e.g. 256, 256, 3). Quoting @naoko from comments.

* model.add(MaxPooling2D((2,2), strides=(2,2)) ==> model.add(MaxPooling2D((2,2), strides=(2,2), dim_ordering="th"))

<Reference>
https://github.com/fchollet/keras/issues/3945
https://stackoverflow.com/questions/39815518/keras-maxpooling2d-layer-gives-valueerror

"""

"""
<Error>
ImportError: `load_weights` requires h5py.

<Solve>
Have you tried directly installing h5py? http://docs.h5py.org/en/latest/build.html

Try running pip install h5py

* pip install h5py

<Reference>
https://github.com/fchollet/keras/issues/3426

"""
# K.set_image_data_format('channels_last')  # TF dimension ordering in this code
def deepModel(width, height):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(1, 44100, 1), data_format = "channels_first"))
    model.add(Conv2D(32, (3, 3), activation='relu', data_format = "channels_first"))

    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

def testModel():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(1, 44100, 1), data_format='channels_first'))

    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])



def tireModel():
    model = Sequential()
    #Sequential : 인공신경망 모델을 생성하기 위해 쓰이는 linear layer stack
    model.add(ZeroPadding2D((1, 1), input_shape=(1, 44100, 1)))
    #input_shape=(행, 열 //입력 이미지 사이즈, 색상 //색상)
    # 흑백 -> 색상=1, RGB -> 색상=3
    model.add(Conv2D(32, (3, 3), activation="relu"))
    model.add(MaxPooling2D((4, 4), strides=(2, 2), data_format="channels_first"))
    #Con2D(filter_num, kernel_size, activation)
    # filter_num : filter_num개의 filter를 적용
    # kernel_size : filter의 크기
    # activation : 활성화 함수
    model.add(ZeroPadding2D((1, 1)))
    model.add(Conv2D(32, (3, 3), activation="relu"))
    model.add(MaxPooling2D((4, 4), strides=(2, 2), data_format="channels_first"))
    #model.add(ZeroPadding2D((1, 1)))
    #model.add(Conv2D(32, (3, 3), activation="relu"))

    #model.add(MaxPooling2D((4, 4), strides=(2, 2), data_format="channels_first"))
    #MaxPooling2D : 정해진 영역 안에서 가장 큰 값만 남기고 나머지는 버리는 방식

    #model.add(ZeroPadding2D((1, 1)))
    #model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(MaxPooling2D((4, 4), strides=(2, 2), data_format="channels_first"))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(MaxPooling2D((4, 4), strides=(2, 2), data_format="channels_first"))

    model.add(Flatten())
    #Flatten : 1차원 배열로 변환
    model.add(Dense(1024, activation='relu'))
    #은닉층
    model.add(Dropout(0.5))
    #Dropout : 랜덤하게 일부 노드 close(특정 노드에 학습이 지나치게 몰리는 것 방지)
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax'))
    #출력층

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    #모델 학습과정 설정
    model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])

    return model

def loadModel(weightPath):
    #model = deepModel(1, 40000)
    model = tireModel()
    if os.path.exists(weightPath):
       model.load_weights(weightPath)

    return model

def saveModel(model, path):
    model.save(path)
    #model.save_weights(path)
    print ('Saving model: ' + model.name)
    print ('Path: ' + path)
    K.clear_session()

def saveModelDescription(model, path):
    plot_model(model, to_file=path, show_shapes=True)