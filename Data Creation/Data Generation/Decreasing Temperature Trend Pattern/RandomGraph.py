## Load Library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## X-Axis (make 1 to 100 values in inc order)
x = np.linspace(0, 1, 100)
#print(x)

## Different Noise
G1 = np.random.normal(0, 1, 100)
G2 = np.random.normal(0,1,100)
s1 = list(range(0,100))
#print(s1)
#binomial=np.random.binomial(10,0.5,100)
# chisquare=np.random.chisquare(2,100)
# dirichlet = np.random.dirichlet((10, 5, 3), 20).transpose()
# exponential = np.random.exponential(scale=1.0, size=100)
# laplace = np.random.laplace(0, 1, 100)

## Noise added to ascending data
noise= G1
n=40+G1
n1=40+G1

n[20:100]=np.random.randint(20,25, size=80)######## 1

# n[20:30]=np.random.randint(20,30, size=10)
# n1[30:50]=np.random.randint(40,60, size=20)

#n2=n1+n


#out = np.log(noise)
# signal=x+noise
# out = np.log(signal)
# out1=np.square(signal)
# out2=np.reciprocal(signal)
# out3=np.power(signal,3)
# out4=out1+0.3 * out3 + out
## Plot Data

# plt.subplot(131)
# plt.plot(n)
# plt.title('signal')
df=pd.DataFrame()
# G2 = np.random.normal(0, 0.5, 100)
# #noise= G2
# n3=30+G2
n4=30+G2
#signal=n3.round().astype(int)

# n3[20:30]=np.random.randint(20,30, size=10)
# n3[30:40]=np.random.randint(25,50, size=10)
# n3[40:100]=np.random.randint(35,40, size=60)

graph=[]
for i in range(3):
    G2 = np.random.normal(0, 0.5, 100)
    n3 = 30 + G2
    #signal[:]=signal
    a=np.random.randint(20,30)
    b=np.random.randint(50,90)
    #print(a,b)
    #signal[a:b]=np.random.randint(35,50, size=b-a)
    #n3[20:40] = np.random.randint(a, b, size=20)
    #Xaxis.........................Yaxis
    G4 = np.random.normal(0, 1, 100)
    G5 = np.random.normal(0,3,100)
    n3[25:30] = np.random.randint(22.5, 25, size=5)
    n3[30:100] = np.random.randint(22.5, 25, size=70)
   # n3[20:30]=np.random.randint(20,30, size=10)
   #  n3[30:40]=np.random.randint(35,45, size=10)
   #  n3[40:60]=np.random.randint(33,43, size=20)
   #  n3[60:100] = np.random.randint(23, 36, size=40)
    print(n3)
    tempdf=pd.DataFrame({'Pattern1': ["SteepDecrease"]})
    tempdf=tempdf.join(pd.DataFrame([n3]))
    df=df.append(tempdf, ignore_index=True)
    #df = []
    #df[i] = pd.DataFrame({i:n3})
    #df.append(df[i])
    #print(df)
   # df = pd.DataFrame({str(i): n3})
    #df.to_csv("graph" + str(i)+ ".csv", index=False)
    graph.append(n3)
    plt.plot(n3)
    plt.title("DecreasingTemp")
    plt.show()


for i in range(3):
    G2 = np.random.normal(0, 0.5, 100)
    n4 = 30 + G2
    a1 = np.random.randint(5, 60)
    n4[a1:100] = np.random.randint(22.5, 25, size=100-a1)
    # n3[20:30]=np.random.randint(20,30, size=10)
    #  n3[30:40]=np.random.randint(35,45, size=10)
    #  n3[40:60]=np.random.randint(33,43, size=20)
    #  n3[60:100] = np.random.randint(23, 36, size=40)
    print(n4)
    tempdf = pd.DataFrame({'Pattern1': ["SteepDecreaseForward"]})
    tempdf = tempdf.join(pd.DataFrame([n4]))
    df = df.append(tempdf, ignore_index=True)
    # df = []
    # df[i] = pd.DataFrame({i:n3})
    # df.append(df[i])
    # print(df)
    # df = pd.DataFrame({str(i): n3})
    # df.to_csv("graph" + str(i)+ ".csv", index=False)
    graph.append(n4)
    plt.plot(n4)
    plt.title("failure")
 #   plt.show()

for i in range(4):
    G2 = np.random.normal(0, 0.5, 100)
    n5 = 30 + G2
    a11 = np.random.randint(5, 60)
    b11= np.random.randint(23, 29)
    print(b11)
    n5[a11:100] = np.random.randint(b11-2, b11, size=100-a11)
    # n3[20:30]=np.random.randint(20,30, size=10)
    #  n3[30:40]=np.random.randint(35,45, size=10)
    #  n3[40:60]=np.random.randint(33,43, size=20)
    #  n3[60:100] = np.random.randint(23, 36, size=40)
    #print(n5)
    tempdf = pd.DataFrame({'Pattern1': ["SteepDecreaseVariations"]})
    tempdf = tempdf.join(pd.DataFrame([n5]))
    df = df.append(tempdf, ignore_index=True)
    # df = []
    # df[i] = pd.DataFrame({i:n3})
    # df.append(df[i])
    # print(df)
    # df = pd.DataFrame({str(i): n3})
    # df.to_csv("graph" + str(i)+ ".csv", index=False)
    graph.append(n5)
    plt.plot(n5)
    plt.title("failure")
   # plt.show()


df.to_csv('TestData1.csv')
print(graph)
#df = pd.DataFrame({i: n3})
#df.to_csv("graph1.csv", index=False)


#
# print(n3)
# import numpy
# import pandas as pd
#
#
# plt.subplot(132)
# plt.plot(n3)
# plt.title('signal')
#
# G2 = np.random.normal(0, 4, 100)
# #noise= G2
# n4=20+G2
# n4[20:30]=np.random.randint(20,30, size=10)
# n4[30:40]=np.random.randint(25,50, size=10)
# n4[40:100]=np.random.randint(35,40, size=60)
#
# # df = pd.DataFrame({"1" : n3, "2" : n, "3" : n4})
# # df.to_csv("graph.csv", index=False)
#
#
# plt.subplot(133)
# plt.plot(n4)
# plt.gca().invert_yaxis()
# plt.title('signal')
#
# # plt.subplot(332)
# # plt.plot(noise)
# # plt.title("noise")
# #
# # plt.subplot(333)
# # plt.plot(out)
# # plt.title("log")
# #
# # plt.subplot(334)
# # plt.plot(out1)
# # plt.title("square")
# #
# # plt.subplot(335)
# # plt.plot(out2)
# # plt.title("reciprocal")
# #
# # plt.subplot(336)
# # plt.plot(out3)
# # plt.title("cube")
# #
# # plt.subplot(337)
# # plt.plot(out4)
# # plt.title("polynomial")
# #
# # plt.subplot(338)
# # plt.plot(x)
# # plt.title('signal')
# plt.show()
