# Model Optimization

Problem Statement :- Tune the Hyper parameters to optimize the model and get the best accuracy.  

High Level Requirements :- Python 3.6, Keras, Tensorflow 1.4  

Implementation :-
In Basic Model Creation, we created simple model. When tuning Neural network, we must consider all the important hyper parameter.  

Few of them are:  

1. No of layers (how many Dense?)  
2. No of Neurons in each layer (how many units in each Dense layer?)  
3. Learning rate, Batch Size, Regularizers.  
4. Other are Loss, Optimizer  
5. We will touch upon all of them randomly. Initially lets consider random model like this  

model 1:  
<img src="/Images/optimize_1.png">  
We have last layer with units 6 since we have 6 causes. Each unit will give probability of occurrence of respective cause.   
Here I have got accuracy of only 17% and it was achieved In few epochs and then it stayed constant. I changed it with higher epochs and different batch size still quite the same result. If accuracy get constant that means weight are no getting updated, thus one should decrease its learning rate.  

model 2:   
<img src="/Images/optimize_2.png">  
Previously we used sgd (stochastic gradient descent ). All optimizer have their own way of updating the weights. One can wisely choose the loss and optimizer if it knows the working behind each type of optimizer. But its out of context to explain how each optimizer work and when to choose what. Other option is to try with many optimizer and to trial and error to best fit the optimizer. Usually Adam optimizer is the best choice to go with as it avoid problem of vanishing/exploding gradient problems. There are much better optimizer as well which can do quite well on some of the applications.    

Soo here I changed to Adam optimizer and kept loss same as previous because categorical_crossentropy works very well when we have classification task. Here we got accuracy of 50%  

model 3:  
<img src="/Images/optimize_3.png">
Here I have reduced the learning rate to a quite small number. When we have low learning rate, then model will need more epochs to learn. Since learning rate is less, weights are updated with small amount. Thus whenever our accuracy is increasing and there are chances it could increase more by increasing epoch. One must increase the epochs.  

model 4:  
<img src="/Images/optimize_4.png">
Okay even by reducing learning rate, if  your accuracy cannot increase further then one need to tune the number of layers and units in it. Here I have used 4 layer and by trial and error I got best accuracy with these units in each layer. Always remember a rule of thumb. Don't change multiple hyper parameter at a time. When your working with 4 layer, try as much as combination of units in neural layer. If you consider one configuration, try all sort of thing with it.  

Yes , here I choose to go with 4 layer since I tried everything with 3 layer network ( used random units value, played with batch size, learning rate) and could not increase much accuracy. So when I went with 4 layer, I tried with some combination of units in it. I found my accuracy could improve if I increase epochs. So I kept on increasing it to the point where my accuracy didn't increase much further. One must not make epochs too large than required because that will cause over training where it will memorize the inputs and wont make intellectual classification.   

model 5:  
<img src="/Images/optimize_5.png">  
We saw in previous model that test and train accuracy have a difference of almost 8%. This is not good sign, because your model doing good at training set but not so good at testing set. This means model has a high variance because test and train accuracy are quite wide. One must keep test and train accuracy quite close ( only 2 or 3 % difference). If given a choice between (98% train, 90 % test) & (92% train, 90% test). The second model would be taken as a best choice, because it is not over fitting the training data and doing well on both test and train data.  

How u can avoid Overfitting?  

1. Don't train for epochs more than it is required - validate it with test data on each epoch ( i.e check both your training and testing accuracy at each epoch and then smartly choose the epoch value).This step is also called validation where some amount of your train data is use instead of test data. which can be specified in model.fit command.  
2. Get more data to train your model.  
3. Use regularizers and dropouts.  

So here I used regularizers, It is out of context to explain how regularizer help in reducing weight but what intuitively it does is tries to simplify the network and push your unwanted weights to zero. Now here we got additional hyper parameter those are the values for regularizer.  

model 6:  
<img src="/Images/optimize_6.png">
We got quite good accuracy here and reduced variance to a great extent. Now lets talk how to choose regularizer value or in general how to tune a value for any hyper parameter. Let consider we had regularizer value 0.3, use a scale of 10 i.e test with value 0.1 and 0.9. Intermediately you could try with 0.5 as well. If you find making value small is better, try value 3-4 value random between 0.1 and 0.01.If we find reducing further can help. Go with value between 0.01 and 0.09. These is one of the smart way of choosing value by seeing the trend in each range of value.  

If this technique don't work, don't use any logic,  try with any value and then again apply above technique for current range.  

model 7:  
<img src="/Images/optimize_7.png">    
when you tried with learning rate, batch size, regularizer , epochs and nothing else is happing. Its the time to change your units value. This was random guess and I got pretty good result almost 96.67% testing accuracy. If you have tried everything, tried almost all kind of permutations and combination and cannot increase your accuracy further then you must do manual error analysis. i.e Check your test data, find where your classifier going wrong, If your result are biased to one cause that means you need to see your distribution of training set, you might need to include data of those category whose mis-classification are quite more.  

At the end you can do really well in modelling only if you love your work and crazy to get best shot out of it.  
