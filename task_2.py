#Fibonacci dizisindeki değerleri dört milyonu geçmeyen terimleri dikkate alarak çift değerli terimlerin toplamını bulunuz.

sum=0
fib=0
point=2
previous=1

for i in range(1,4000000):
    #fibonacci mi ?

    fib=point+previous
    if(fib>4000000):
        break
    if(fib%2==0):
        sum+=fib
    previous=point
    point=fib
    print(fib)

print("Sum of Fibonacci",sum+2)
   
