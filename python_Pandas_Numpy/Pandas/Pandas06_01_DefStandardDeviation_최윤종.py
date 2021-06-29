
# coding: utf-8

# In[7]:


import numpy as np


# In[30]:


dataList = [28,31,24,25,30,32,20,30,31,26,31]

def mMean(dataList):
    a = 0
    for i in dataList:
        a = a + i
    return a / len(dataList)

def mMedian(dataList):
    b = len(dataList)
    if b%2==1:
        result = dataList[int((b-1)/2)]
    else:
        result=(dataList[int(b/2)-1]+dataList[int(b/2)])/2
        
    return result

def mDeviation(dataList):
    s = []
    for i in dataList:
        s.append(i- mMean(dataList))
    return s


def mVariance(dataList):
    avg = np.average(dataList)
    var=0
    
    for num in dataList:
        var += (num - avg)**2
        
    return var / (len(dataList)-1)


def mStandardDeviation(dataList):
    avg = np.average(dataList)
    var=0
    
    for num in dataList:
        var += (num - avg)**2
        
    return (var / (len(dataList)-1))**(1/2)

def mRange():
    return max(dataList) - min(dataList)
    
    
    
print("평균값 : {}".format(mMean(dataList)))
print("중앙값 : {}".format(mMedian(dataList)))
print("편차값 : {}".format(mDeviation(dataList)))
print("분산값 : {}".format(mVariance(dataList)))
print("표준편차값 : {}".format(mStandardDeviation(dataList)))
print("최대값과 최소값의 차이 : {}".format(mRange()))

