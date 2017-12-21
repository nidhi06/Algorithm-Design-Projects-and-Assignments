#0-1 knapsack
# Algorithm 5.7
global W
W=9
global n
n=6
global p
p=[0,20,30,35,12,3]
global w
w=[0,2,5,7,3,1]
global include
include=[""]*10
bestset=[""]*10
maxprofit=0
numbest=0
def knapsack(i,profit,weight):
    global maxprofit,numbest, bestset
    if(weight<=W and profit >maxprofit):
        maxprofit = profit
        numbest = i
        bestset = include
        print ("bestest1:"+str(bestset))
    if(promising(i,profit,weight)):
        include[i+1]="yes"
        knapsack(i+1,profit+p[i+1],weight+w[i+1])
        include[i+1]="no"
        knapsack(i+1,profit,weight)
def promising(i,profit,weight):
    if(weight>=W):
        return False
    else:
        j=i+1
        print j
        bound=profit
        print("bound1:"+str(bound))
        totweight=weight
        while(j<n and totweight+w[j]<=W):

            totweight =totweight +w[j]
            print("totweight:"+str(totweight))
            bound=bound+p[j]
            print("bound2:"+str(bound))
            j+=1
        k=j
        if(k<n):

            bound=bound +(W-totweight)*p[k]/w[k]
            print ("bound3:"+str(bound))
            print("maxprofit:"+str(maxprofit))
        return bound>maxprofit

def main():
    knapsack(0,0,0)
    print ("Maximum Profit: "+str(maxprofit))
    print("Numbest:"+str(numbest))
    print ("Include:"+str(include))
    for j in range(1,numbest+1):
        print bestset[j]
    print ("Bestset:"+str(bestset))

    

    
        
