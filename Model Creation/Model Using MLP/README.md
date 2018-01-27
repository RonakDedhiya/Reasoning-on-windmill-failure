# Model using MLP

Problem Statement :- Creating model to predict the cause of failure seeing the temperature trend/Pattern.  

High Level Requirements :- Python 3.6, Tensorflow 1.4, Keras  

Implemenation :-  

Steps to be followed :-  
    1.Model Description  
    2.Input/output configuration
    3.Model Implementation

      Model Description :-  
      We will be using here Multilayer Perceptron Network. The MLP consists of three or more layers (an input and an output layer with one or more hidden layers). Each Layer with multiple Neurons/node associated with activation function. Since MLPs are fully connected, each node in one layer connects with a certain weights to every node in the following layer. Learning occurs in the perceptron by changing connection weights after each piece of data is processed, based on the amount of error in the output compared to the expected result. This is what called as supervised learning, and is carried out through backpropagation.

      <img src='/Images/MLP_model.png'>  

        Input/output configuration :-
        We have generated Temperature Pattern with each sample having 100 points. These 100 points represent temperature values. These set of 100 points are given as an input to the model. So input dimension is 100 for our model. We have considered 6 causes for Device Failure. Thus our output soft max layer will be having output dimension = 6. Thus we would add last layer with 6 units.  

        We would call this samples of 100 points as Xtrain and its causes as Ytrain. similarly for test data ( Xtest and Ytest).To use our data in model, we have to convert our causes into one hot encoding. Thus we would convert our Ytrain and Ytest into one hot encoded format and then will provide it to model.     

        If we have 600 set of training data and 60 set of testing data. we would have:  
        Xtrain.shape = ( 600,100), Ytrain.shape = (600,6), Xtest.shape = (60,100). Ytest.shape = (60,6)  

        Model Implementation :-    
        We are going with keras framework to build our model. Keras is a high-level neural networks API, written in Python and capable of   running on top of TensorFlow. The core data structure of Keras is a model, a way to organize layers. The simplest type of model is the Sequential model, a linear stack of layers.   

        <img src='/Images/keras_code1.png'>

        Here Dense is a Neural Network layer where units describe number of neurons/nodes in it with activations in each of them. Once we create structure of model by adding layers, we configure loss and optimizer. Loss gives error in predicted result from desired result and optimizer update your weights according to loss. There are different types of loss and optimizer, each having its own way of computing loss and updating weights.  

        Optimizer update weights according to learning rate. Learning rate is one of the most important hyper parameter which should be chosen by trial and error to get best result. Similarly No of Dense layer, Number of units in each Layer are other set of hyper parameter that need to be optimized to get best result.  

        <img src='/Images/keras_code2.png'>
        
