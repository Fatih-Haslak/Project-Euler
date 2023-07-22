#asal çarpanların en büyüğü
import math

b=(600851475143)
c=int(600851475143**0.5)
temp=0



def asal_mi(sayi):
    for i in range(2,sayi-1):
        if(sayi%i==0):
            return False
    return True    
    
for i in range(1,b,2):
    if(i>=c):
        break

    if( b % i==0):
        if(asal_mi(i)==True):
            temp=i
            c=int(c/2)
            
   
   
print("{} sayisinin en büyük asal çarpani {}".format(b,temp))

