from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
from keras import regularizers
from keras.models import load_model

import pandas as pd
import numpy as np



def read_data():
    df_train=pd.read_csv('./dataset/train_data_one_to_one.csv')
   
    df_x=df_train.iloc[:,1:101]
    x_train=np.array(df_x)
    x_train=np.expand_dims(x_train, axis=2) 
    
    df_y_train=df_train.iloc[:,101]
    
    df_test=pd.read_csv('./dataset/test_data.csv')
    df_x_test=df_test.iloc[:,1:101]
    x_test=np.array(df_x_test)
    x_test=np.expand_dims(x_test, axis=2)
    
    df_y_test=df_test.iloc[:,101]
    
    y_df_all=df_y_train.append(df_y_test,ignore_index=True)
    y_encode=pd.get_dummies(y_df_all)
    s2 = y_encode.idxmax()
    print(s2)
    print(y_encode[:10])
    print(y_encode[630:])
    y_all=np.array(y_encode)
    y_train=y_all[:580]
    y_test=y_all[580:]

    return x_train,y_train,x_test,y_test
    
    
def create_model(x_train,y_train,x_test,y_test):
    model = Sequential()
    model.add(Conv1D(64, 3, activation='relu', input_shape=(100,1)))
    model.add(Conv1D(64, 3, activation='relu'))
    model.add(MaxPooling1D(3))
    model.add(Conv1D(128, 3, activation='relu'))
    model.add(Conv1D(128, 3, activation='relu'))
    model.add(GlobalAveragePooling1D())
    model.add(Dropout(0.5))
    model.add(Dense(6, activation='softmax'))
    
    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    
    model.fit(x_train, y_train, batch_size=16, epochs=150)
    score = model.evaluate(x_test, y_test, batch_size=1)
    print('Model saved: ',score)
    model.save('conv1d_model.h5')
    return model

def load_saved_model():
    return load_model('conv1d_model.h5')

x_train,y_train,x_test,y_test=read_data()
model=create_model(x_train,y_train,x_test,y_test)
#model=load_saved_model()
score = model.evaluate(x_test, y_test, batch_size=1)
print(score)

result=model.predict(x_test, batch_size=1)
indexes = np.argmax(result, axis=1)
print(indexes) 
array=['Anemometer errors','BladeAccumulatorPressureIssues',  'CoolingSystemIssues', 'Generator speed discrepancies',  'Oil Leakage',  'Overheated oil']
res=[]
for i in  indexes:
    res=np.append(res,array[i])
print(list(res))

#print(result)