# Algorithm 5.3
# monte-carlo estimate for n-queens
import random
global col
n=8
col=range(n+1)
def monte_carlo(n):   #probabalistic algorithm
    i=0
    numnodes=1
    m=1
    mprod=1
    prom_children=[]
    while(m!=0 and i!=n):
          mprod=mprod*m
          numnodes =numnodes+(mprod*n)
          i+=1
          m=0
          del prom_children[:]
          for j in range(0,n):
              col[i]=j
              if promising(i):
                  m+=1
                  prom_children.append(j)
          if(m!=0):
             j=random.choice(prom_children)
             col[i]=j
    return numnodes
            
      

def promising(i):  #check if column is safe to put a queen
    k=1
    sw=True
    while(k<i and sw):
        if((col[i]==col[k]) or abs(col[i]-col[k])==abs(i-k)):
            sw=False
        k+=1
            
    return sw

def main():
    sum=0
    for i in range(20):
        sum+=monte_carlo(8)
    print(sum/20)