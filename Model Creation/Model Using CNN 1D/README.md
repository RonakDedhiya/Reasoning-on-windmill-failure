# Model Using Convolution 1D  

Problem Statement :  
Creating model to predict the cause of failure seeing the temperature trend/Pattern.   

High Level Requirements :   

Python 3.6, Tensorflow 1.4, Keras    

Implemenation :     

Steps to be followed :      
      1.Model Description    
      2.Input/output configuration    
      3.Model Implementation    

1.Model Description :  
The figure below provides the CNN model architecture that we are going to implement using Keras. The model will consist of one   convolution layer followed by max pooling and another convolution layer. After that, the model will have fully connected layer   which is connected to Softmax layer. Remember that the convolution and max-pool layers will be 1D or temporal.    

<img src='/Dataset/Images/Conv1D.png'>  

2.Input/output configuration :      
We have generated Temperature Pattern with each sample having 100 points. These 100 points represent temperature values.         These set of 100 points are given as an input to the model. So input dimension is [100,1] for our model.
We have considered 6 causes for Device Failure. Thus our output soft max layer output dimension will be 6.      
For training we required 3D data means data in 3 dimensional array. So we converted input data in dimension           [data_sample,100,1], refer below code for data conversion:        

<img src='/Dataset/Images/Conv1D_code1.png'>  

3.Model Implementation :   
We have used Keras ( high level machine learning  API with Tensorflow at back-end ). For convolution Keras provides  
keras.layers.Conv1D(), so we can easily define and add layer to our model.    

We used Sequential Model, The Sequential model is a linear stack of layers. Then we have added two convolution layer with     output filler size of 64 for each layer, the we have added MaxPooling1D() to select maximum point for output. After that we   have   added another two convolution layers with filter size of 128 each, then we have used GlobalAveragePooling1D() to select    average of points for output. At the last for final output we used Dense() with output size of 6 because we have 6 different   classes and 'Softmax'activation function.    

<img src='/Dataset/Images/Conv1D_code2.png'>   
