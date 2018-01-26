## Load Library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.DataFrame()
signal_suuden_rise_fall=[]

## Pattern 1
## 100 denotes the number of samples It will generate
for i in range(100):

    #Noise creation numpy.random.normal(loc=0.0, scale=1.0, size=None)
    Noise=np.random.normal(0,1,90)
    #Consider avg temp is 30 and add noise
    signal= 30 + Noise
    ## Generatd 10 random number between 1 to 90
    random=np.random.randint(1,90, size=10)
    ## Making Value at above generated points to 0
    signal_sensor_fail=np.insert(signal,random,0)
    ## Plot the signal
    plt.plot(signal_sensor_fail)
    plt.title("Signal due to sensor failure")
    plt.show()
    ## Apeending into one DataFrame all the samples
    tempdf=pd.DataFrame({'Pattern': ["signal_sensor_fail"]})
    tempdf=tempdf.join(pd.DataFrame([signal_sensor_fail]))
    df=df.append(tempdf, ignore_index=True)

## Pattern 2
## 100 denotes the number of samples It will generate
for i in range(100):

    ## Noise creation numpy.random.normal(loc=0.0, scale=1.0, size=None)
    Noise=np.random.normal(0,1,100)
    ## Consider avg temp is 30 and add noise
    signal_suuden_rise_fall[:]=30+Noise
    ## Generate a random number between 1 to 50 && 55 to 90
    a=np.random.randint(1,50)
    b=np.random.randint(55,90)
    ## Insert any value between 65 to 70 over the points between a & b
    signal_suuden_rise_fall[a:b]=np.random.randint(65,70, size=b-a)
    ## Plot the signal
    plt.plot(signal_suuden_rise_fall)
    plt.title("failure")
    plt.show()
    ## Appending into Dataframe all the samples
    tempdf=pd.DataFrame({'Pattern': ["signal_suuden_rise_fall"]})
    tempdf=tempdf.join(pd.DataFrame([signal_suuden_rise_fall]))
    df=df.append(tempdf, ignore_index=True)



## Convert Dataframe to Csv
df.to_csv('Pattern.csv',index=False)
