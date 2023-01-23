#Create arithmetics class to calculate avg, mean, mode and standard deviation
from statistics import stdev

class Arithmetics:
    def __init__(self,li):
        self.li=li
    
    def avg(self):
        return sum(self.li)/len(self.li)
    
    def mean(self):
        return self.avg()
    
    def mode(self):
        dict={}
        for i in li:
            if i in dict:
                dict[i]+=1
            else:
                dict[i] = 1
        return [k for k,v in dict.items() if v==max(dict.values())]
    
    def median(self):
        le=len(li)
        if(le%2==0):
            return (sorted(li)[le//2] + sorted(li)[le//2-1]) / 2
        else:
            return sorted(li)[le//2]
    
    def standard_deviation(self):
        return stdev(self.li)
        


li=[1,2,3,4,5,6,6]
a=Arithmetics(li)
print("this is the average of the provided data "+str(a.avg()))
print("this is the mode of the provided data "+str(a.mode()))
print("this is the mean of the provided data "+str(a.mean()))
print("this is the median of the provided data "+str(a.median()))
print("this is the standard_deviation of the provided data "+str(a.standard_deviation()))