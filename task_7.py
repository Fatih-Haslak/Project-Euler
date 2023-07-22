#10001. prime number
import time

i=1
count=0
find_n_prime_number=int(input("Deger giriniz->"))
start=time.time()
def asal_mi(sayi):
    for i in range(2,int(sayi**0.5)+1):
        if(sayi%i==0):
            return False
    return True    
    

while(True):
    i+=2
    if(asal_mi(i)==True):
            
        count+=1
    if(count==(find_n_prime_number-1)):
        print("{}. asal sayi {} dir/dür ".format(find_n_prime_number,i))
        break

end=time.time()

print("The time of execution of above program is :",
      (end-start) , "sn")